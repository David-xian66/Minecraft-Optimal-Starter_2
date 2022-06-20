/****************************************************************************
**
** Copyright (C) 2019 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the Qt Gui module
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or (at your option) the GNU General
** Public license version 3 or any later version approved by the KDE Free
** Qt Foundation. The licenses are as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-2.0.html and
** https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef QSHADERDESCRIPTION_H
#define QSHADERDESCRIPTION_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists for the convenience
// of a number of Qt sources files.  This header file may change from
// version to version without notice, or even be removed.
//
// We mean it.
//

#include <QtGui/qtguiglobal.h>
#include <QtCore/QString>
#include <QtCore/QList>
#include <array>

QT_BEGIN_NAMESPACE

struct QShaderDescriptionPrivate;
class QDataStream;

class Q_GUI_EXPORT QShaderDescription
{
public:
    QShaderDescription();
    QShaderDescription(const QShaderDescription &other);
    QShaderDescription &operator=(const QShaderDescription &other);
    ~QShaderDescription();
    void detach();

    bool isValid() const;

    void serialize(QDataStream *stream) const;
    QByteArray toJson() const;

    static QShaderDescription deserialize(QDataStream *stream, int version);

    enum VariableType {
        Unknown = 0,

        // do not reorder
        Float,
        Vec2,
        Vec3,
        Vec4,
        Mat2,
        Mat2x3,
        Mat2x4,
        Mat3,
        Mat3x2,
        Mat3x4,
        Mat4,
        Mat4x2,
        Mat4x3,

        Int,
        Int2,
        Int3,
        Int4,

        Uint,
        Uint2,
        Uint3,
        Uint4,

        Bool,
        Bool2,
        Bool3,
        Bool4,

        Double,
        Double2,
        Double3,
        Double4,
        DMat2,
        DMat2x3,
        DMat2x4,
        DMat3,
        DMat3x2,
        DMat3x4,
        DMat4,
        DMat4x2,
        DMat4x3,

        Sampler1D,
        Sampler2D,
        Sampler2DMS,
        Sampler3D,
        SamplerCube,
        Sampler1DArray,
        Sampler2DArray,
        Sampler2DMSArray,
        Sampler3DArray,
        SamplerCubeArray,
        SamplerRect,
        SamplerBuffer,
        SamplerExternalOES,

        Image1D,
        Image2D,
        Image2DMS,
        Image3D,
        ImageCube,
        Image1DArray,
        Image2DArray,
        Image2DMSArray,
        Image3DArray,
        ImageCubeArray,
        ImageRect,
        ImageBuffer,

        Struct
    };

    enum ImageFormat {
        // must match SPIR-V's ImageFormat
        ImageFormatUnknown = 0,
        ImageFormatRgba32f = 1,
        ImageFormatRgba16f = 2,
        ImageFormatR32f = 3,
        ImageFormatRgba8 = 4,
        ImageFormatRgba8Snorm = 5,
        ImageFormatRg32f = 6,
        ImageFormatRg16f = 7,
        ImageFormatR11fG11fB10f = 8,
        ImageFormatR16f = 9,
        ImageFormatRgba16 = 10,
        ImageFormatRgb10A2 = 11,
        ImageFormatRg16 = 12,
        ImageFormatRg8 = 13,
        ImageFormatR16 = 14,
        ImageFormatR8 = 15,
        ImageFormatRgba16Snorm = 16,
        ImageFormatRg16Snorm = 17,
        ImageFormatRg8Snorm = 18,
        ImageFormatR16Snorm = 19,
        ImageFormatR8Snorm = 20,
        ImageFormatRgba32i = 21,
        ImageFormatRgba16i = 22,
        ImageFormatRgba8i = 23,
        ImageFormatR32i = 24,
        ImageFormatRg32i = 25,
        ImageFormatRg16i = 26,
        ImageFormatRg8i = 27,
        ImageFormatR16i = 28,
        ImageFormatR8i = 29,
        ImageFormatRgba32ui = 30,
        ImageFormatRgba16ui = 31,
        ImageFormatRgba8ui = 32,
        ImageFormatR32ui = 33,
        ImageFormatRgb10a2ui = 34,
        ImageFormatRg32ui = 35,
        ImageFormatRg16ui = 36,
        ImageFormatRg8ui = 37,
        ImageFormatR16ui = 38,
        ImageFormatR8ui = 39
    };

    enum ImageFlag {
        ReadOnlyImage = 1 << 0,
        WriteOnlyImage = 1 << 1
    };
    Q_DECLARE_FLAGS(ImageFlags, ImageFlag)

    // Optional data (like decorations) usually default to an otherwise invalid value (-1 or 0). This is intentional.

    struct InOutVariable {
        QByteArray name;
        VariableType type = Unknown;
        int location = -1;
        int binding = -1;
        int descriptorSet = -1;
        ImageFormat imageFormat = ImageFormatUnknown;
        ImageFlags imageFlags;
        QList<int> arrayDims;
    };

    struct BlockVariable {
        QByteArray name;
        VariableType type = Unknown;
        int offset = 0;
        int size = 0;
        QList<int> arrayDims;
        int arrayStride = 0;
        int matrixStride = 0;
        bool matrixIsRowMajor = false;
        QList<BlockVariable> structMembers;
    };

    struct UniformBlock {
        QByteArray blockName;
        QByteArray structName; // instanceName
        int size = 0;
        int binding = -1;
        int descriptorSet = -1;
        QList<BlockVariable> members;
    };

    struct PushConstantBlock {
        QByteArray name;
        int size = 0;
        QList<BlockVariable> members;
    };

    struct StorageBlock {
        QByteArray blockName;
        QByteArray instanceName;
        int knownSize = 0;
        int binding = -1;
        int descriptorSet = -1;
        QList<BlockVariable> members;
    };

    QList<InOutVariable> inputVariables() const;
    QList<InOutVariable> outputVariables() const;
    QList<UniformBlock> uniformBlocks() const;
    QList<PushConstantBlock> pushConstantBlocks() const;
    QList<StorageBlock> storageBlocks() const;
    QList<InOutVariable> combinedImageSamplers() const;
    QList<InOutVariable> storageImages() const;

    std::array<uint, 3> computeShaderLocalSize() const;

private:
    QShaderDescriptionPrivate *d;
    friend struct QShaderDescriptionPrivate;
#ifndef QT_NO_DEBUG_STREAM
    friend Q_GUI_EXPORT QDebug operator<<(QDebug, const QShaderDescription &);
#endif
    friend Q_GUI_EXPORT bool operator==(const QShaderDescription &lhs, const QShaderDescription &rhs) noexcept;
};

Q_DECLARE_OPERATORS_FOR_FLAGS(QShaderDescription::ImageFlags)

#ifndef QT_NO_DEBUG_STREAM
Q_GUI_EXPORT QDebug operator<<(QDebug, const QShaderDescription &);
Q_GUI_EXPORT QDebug operator<<(QDebug, const QShaderDescription::InOutVariable &);
Q_GUI_EXPORT QDebug operator<<(QDebug, const QShaderDescription::BlockVariable &);
Q_GUI_EXPORT QDebug operator<<(QDebug, const QShaderDescription::UniformBlock &);
Q_GUI_EXPORT QDebug operator<<(QDebug, const QShaderDescription::PushConstantBlock &);
Q_GUI_EXPORT QDebug operator<<(QDebug, const QShaderDescription::StorageBlock &);
#endif

Q_GUI_EXPORT bool operator==(const QShaderDescription &lhs, const QShaderDescription &rhs) noexcept;
Q_GUI_EXPORT bool operator==(const QShaderDescription::InOutVariable &lhs, const QShaderDescription::InOutVariable &rhs) noexcept;
Q_GUI_EXPORT bool operator==(const QShaderDescription::BlockVariable &lhs, const QShaderDescription::BlockVariable &rhs) noexcept;
Q_GUI_EXPORT bool operator==(const QShaderDescription::UniformBlock &lhs, const QShaderDescription::UniformBlock &rhs) noexcept;
Q_GUI_EXPORT bool operator==(const QShaderDescription::PushConstantBlock &lhs, const QShaderDescription::PushConstantBlock &rhs) noexcept;
Q_GUI_EXPORT bool operator==(const QShaderDescription::StorageBlock &lhs, const QShaderDescription::StorageBlock &rhs) noexcept;

inline bool operator!=(const QShaderDescription &lhs, const QShaderDescription &rhs) noexcept
{
    return !(lhs == rhs);
}

inline bool operator!=(const QShaderDescription::InOutVariable &lhs, const QShaderDescription::InOutVariable &rhs) noexcept
{
    return !(lhs == rhs);
}

inline bool operator!=(const QShaderDescription::BlockVariable &lhs, const QShaderDescription::BlockVariable &rhs) noexcept
{
    return !(lhs == rhs);
}

inline bool operator!=(const QShaderDescription::UniformBlock &lhs, const QShaderDescription::UniformBlock &rhs) noexcept
{
    return !(lhs == rhs);
}

inline bool operator!=(const QShaderDescription::PushConstantBlock &lhs, const QShaderDescription::PushConstantBlock &rhs) noexcept
{
    return !(lhs == rhs);
}

inline bool operator!=(const QShaderDescription::StorageBlock &lhs, const QShaderDescription::StorageBlock &rhs) noexcept
{
    return !(lhs == rhs);
}

QT_END_NAMESPACE

#endif
