/****************************************************************************
**
** Copyright (C) 2018 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the QtGui module of the Qt Toolkit.
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

#ifndef QCOLORTRANSFERTABLE_P_H
#define QCOLORTRANSFERTABLE_P_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists purely as an
// implementation detail.  This header file may change from version to
// version without notice, or even be removed.
//
// We mean it.
//

#include <QtGui/private/qtguiglobal_p.h>
#include "qcolortransferfunction_p.h"

#include <QList>

#include <algorithm>
#include <cmath>

QT_BEGIN_NAMESPACE

// Defines either an ICC TRC 'curve' or a lut8/lut16 A or B table
class Q_GUI_EXPORT QColorTransferTable
{
public:
    QColorTransferTable() noexcept
            : m_tableSize(0)
    { }
    QColorTransferTable(uint32_t size, const QList<uint8_t> &table) noexcept
        : m_tableSize(size), m_table8(table)
    {
        Q_ASSERT(qsizetype(size) <= table.count());
    }
    QColorTransferTable(uint32_t size, const QList<uint16_t> &table) noexcept
        : m_tableSize(size), m_table16(table)
    {
        Q_ASSERT(qsizetype(size) <= table.count());
    }

    bool isEmpty() const
    {
        return m_tableSize == 0;
    }

    bool checkValidity() const
    {
        if (isEmpty())
            return true;
        // Only one table can be set
        if (!m_table8.isEmpty() && !m_table16.isEmpty())
            return false;
        // At least 2 elements
        if (m_tableSize < 2)
            return false;
        // The table must describe an injective curve:
        if (!m_table8.isEmpty()) {
            uint8_t val = 0;
            for (uint i = 0; i < m_tableSize; ++i) {
                if (m_table8[i] < val)
                    return false;
                val = m_table8[i];
            }
        }
        if (!m_table16.isEmpty()) {
            uint16_t val = 0;
            for (uint i = 0; i < m_tableSize; ++i) {
                if (m_table16[i] < val)
                    return false;
                val = m_table16[i];
            }
        }
        return true;
    }

    float apply(float x) const
    {
        x = std::clamp(x, 0.0f, 1.0f);
        x *= m_tableSize - 1;
        const uint32_t lo = static_cast<uint32_t>(std::floor(x));
        const uint32_t hi = std::min(lo + 1, m_tableSize - 1);
        const float frac = x - lo;
        if (!m_table16.isEmpty())
            return (m_table16[lo] * (1.0f - frac) + m_table16[hi] * frac) * (1.0f/65535.0f);
        if (!m_table8.isEmpty())
            return (m_table8[lo] * (1.0f - frac) + m_table8[hi] * frac) * (1.0f/255.0f);
        return x;
    }

    // Apply inverse, optimized by giving a previous result a value < x.
    float applyInverse(float x, float resultLargerThan = 0.0f) const
    {
        Q_ASSERT(resultLargerThan >= 0.0f && resultLargerThan <= 1.0f);
        if (x <= 0.0f)
            return 0.0f;
        if (x >= 1.0f)
            return 1.0f;
        if (!m_table16.isEmpty()) {
            const float v = x * 65535.0f;
            uint32_t i = static_cast<uint32_t>(std::floor(resultLargerThan * (m_tableSize - 1)));
            auto it = std::lower_bound(m_table16.cbegin() + i, m_table16.cend(), v);
            i = it - m_table16.cbegin();
            if (i >= m_tableSize - 1)
                return 1.0f;
            const float y1 = m_table16[i - 1];
            const float y2 = m_table16[i];
            Q_ASSERT(v >= y1 && v <= y2);
            const float fr = (v - y1) / (y2 - y1);
            return (i + fr) * (1.0f / (m_tableSize - 1));

        }
        if (!m_table8.isEmpty()) {
            const float v = x * 255.0f;
            uint32_t i = static_cast<uint32_t>(std::floor(resultLargerThan * (m_tableSize - 1)));
            auto it = std::lower_bound(m_table8.cbegin() + i, m_table8.cend(), v);
            i = it - m_table8.cbegin();
            if (i >= m_tableSize - 1)
                return 1.0f;
            const float y1 = m_table8[i - 1];
            const float y2 = m_table8[i];
            Q_ASSERT(v >= y1 && v <= y2);
            const float fr = (v - y1) / (y2 - y1);
            return (i + fr) * (1.0f / (m_tableSize - 1));
        }
        return x;
    }

    bool asColorTransferFunction(QColorTransferFunction *transferFn)
    {
        Q_ASSERT(transferFn);
        if (m_tableSize < 2)
            return false;
        if (!m_table8.isEmpty() && (m_table8[0] != 0 || m_table8[m_tableSize - 1] != 255))
            return false;
        if (!m_table16.isEmpty() && (m_table16[0] != 0 || m_table16[m_tableSize - 1] != 65535))
            return false;
        if (m_tableSize == 2) {
            *transferFn = QColorTransferFunction(); // Linear
            return true;
        }
        // The following heuristics are based on those from Skia:
        if (m_tableSize == 26 && !m_table16.isEmpty()) {
            // code.facebook.com/posts/411525055626587/under-the-hood-improving-facebook-photos
            if (m_table16[6] != 3062)
                return false;
            if (m_table16[12] != 12824)
                return false;
            if (m_table16[18] != 31237)
                return false;
            *transferFn = QColorTransferFunction::fromSRgb();
            return true;
        }
        if (m_tableSize == 1024 && !m_table16.isEmpty()) {
            // HP and Canon sRGB gamma tables:
            if (m_table16[257] != 3366)
                return false;
            if (m_table16[513] != 14116)
                return false;
            if (m_table16[768] != 34318)
                return false;
            *transferFn = QColorTransferFunction::fromSRgb();
            return true;
        }
        if (m_tableSize == 4096 && !m_table16.isEmpty()) {
            // Nikon, Epson, and lcms2 sRGB gamma tables:
            if (m_table16[515] != 960)
                return false;
            if (m_table16[1025] != 3342)
                return false;
            if (m_table16[2051] != 14079)
                return false;
            *transferFn = QColorTransferFunction::fromSRgb();
            return true;
        }
        return false;
    }
    friend inline bool operator!=(const QColorTransferTable &t1, const QColorTransferTable &t2);
    friend inline bool operator==(const QColorTransferTable &t1, const QColorTransferTable &t2);

    uint32_t m_tableSize;
    QList<uint8_t> m_table8;
    QList<uint16_t> m_table16;
};

inline bool operator!=(const QColorTransferTable &t1, const QColorTransferTable &t2)
{
    if (t1.m_tableSize != t2.m_tableSize)
        return true;
    if (t1.m_table8.isEmpty() != t2.m_table8.isEmpty())
        return true;
    if (t1.m_table16.isEmpty() != t2.m_table16.isEmpty())
        return true;
    if (!t1.m_table8.isEmpty()) {
        for (uint32_t i = 0; i < t1.m_tableSize; ++i) {
            if (t1.m_table8[i] != t2.m_table8[i])
                return true;
        }
    }
    if (!t1.m_table16.isEmpty()) {
        for (uint32_t i = 0; i < t1.m_tableSize; ++i) {
            if (t1.m_table16[i] != t2.m_table16[i])
                return true;
        }
    }
    return false;
}

inline bool operator==(const QColorTransferTable &t1, const QColorTransferTable &t2)
{
    return !(t1 != t2);
}

QT_END_NAMESPACE

#endif // QCOLORTRANSFERTABLE_P_H
