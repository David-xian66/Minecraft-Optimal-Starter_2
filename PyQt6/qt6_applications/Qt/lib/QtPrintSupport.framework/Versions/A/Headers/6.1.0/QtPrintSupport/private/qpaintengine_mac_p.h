/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the plugins of the Qt Toolkit.
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

#ifndef QPAINTENGINE_MAC_P_H
#define QPAINTENGINE_MAC_P_H

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

#include <QtPrintSupport/qtprintsupportglobal.h>

#include <QtGui/qpaintengine.h>
#include <QtGui/private/qpaintengine_p.h>
#include <QtGui/private/qfont_p.h>
#include <QtCore/qhash.h>

typedef struct CGColorSpace *CGColorSpaceRef;
typedef struct CGContext *CGContextRef;

QT_BEGIN_NAMESPACE

class QCoreGraphicsPaintEnginePrivate;
class QCoreGraphicsPaintEngine : public QPaintEngine
{
    Q_DECLARE_PRIVATE(QCoreGraphicsPaintEngine)

public:
    QCoreGraphicsPaintEngine();
    ~QCoreGraphicsPaintEngine();

    bool begin(QPaintDevice *pdev);
    bool end();

    void updateState(const QPaintEngineState &state);

    void updatePen(const QPen &pen);
    void updateBrush(const QBrush &brush, const QPointF &pt);
    void updateFont(const QFont &font);
    void updateOpacity(qreal opacity);
    void updateMatrix(const QTransform &matrix);
    void updateTransform(const QTransform &matrix);
    void updateClipRegion(const QRegion &region, Qt::ClipOperation op);
    void updateClipPath(const QPainterPath &path, Qt::ClipOperation op);
    void updateCompositionMode(QPainter::CompositionMode mode);
    void updateRenderHints(QPainter::RenderHints hints);

    void drawLines(const QLineF *lines, int lineCount);
    void drawRects(const QRectF *rects, int rectCount);
    void drawPoints(const QPointF *p, int pointCount);
    void drawEllipse(const QRectF &r);
    void drawPath(const QPainterPath &path);

    void drawPolygon(const QPointF *points, int pointCount, PolygonDrawMode mode);
    void drawPixmap(const QRectF &r, const QPixmap &pm, const QRectF &sr);
    void drawTiledPixmap(const QRectF &r, const QPixmap &pixmap, const QPointF &s);

    void drawTextItem(const QPointF &pos, const QTextItem &item);
    void drawImage(const QRectF &r, const QImage &pm, const QRectF &sr,
                   Qt::ImageConversionFlags flags = Qt::AutoColor);

    Type type() const { return QPaintEngine::CoreGraphics; }

    CGContextRef handle() const;

    static void initialize();
    static void cleanup();

    QPainter::RenderHints supportedRenderHints() const;

    //avoid partial shadowed overload warnings...
    void drawLines(const QLine *lines, int lineCount) { QPaintEngine::drawLines(lines, lineCount); }
    void drawRects(const QRect *rects, int rectCount) { QPaintEngine::drawRects(rects, rectCount); }
    void drawPoints(const QPoint *p, int pointCount) { QPaintEngine::drawPoints(p, pointCount); }
    void drawEllipse(const QRect &r) { QPaintEngine::drawEllipse(r); }
    void drawPolygon(const QPoint *points, int pointCount, PolygonDrawMode mode)
    { QPaintEngine::drawPolygon(points, pointCount, mode); }

protected:
    friend class QMacPrintEngine;
    friend class QMacPrintEnginePrivate;
    QCoreGraphicsPaintEngine(QPaintEnginePrivate &dptr);

private:
    Q_DISABLE_COPY(QCoreGraphicsPaintEngine)
};

/*****************************************************************************
  Private data
 *****************************************************************************/
class QCoreGraphicsPaintEnginePrivate : public QPaintEnginePrivate
{
    Q_DECLARE_PUBLIC(QCoreGraphicsPaintEngine)
public:
    QCoreGraphicsPaintEnginePrivate()
        : hd(nullptr), shading(nullptr), stackCount(0), complexXForm(false), disabledSmoothFonts(false)
    {
    }

    struct {
        QPen pen;
        QBrush brush;
        uint clipEnabled : 1;
        QRegion clip;
        QTransform transform;
   } current;

    //state info (shared with QD)
    CGAffineTransform orig_xform;

    //cg structures
    CGContextRef hd;
    CGShadingRef shading;
    int stackCount;
    bool complexXForm;
    bool disabledSmoothFonts;
    enum { CosmeticNone, CosmeticTransformPath, CosmeticSetPenWidth } cosmeticPen;

    // pixel and cosmetic pen size in user coordinates.
    QPointF pixelSize;
    float cosmeticPenSize;

    //internal functions
    enum { CGStroke=0x01, CGEOFill=0x02, CGFill=0x04 };
    void drawPath(uchar ops, CGMutablePathRef path = nullptr);
    void setClip(const QRegion *rgn = nullptr);
    void resetClip();
    void setFillBrush(const QPointF &origin=QPoint());
    void setStrokePen(const QPen &pen);
    inline void saveGraphicsState();
    inline void restoreGraphicsState();
    float penOffset();
    QPointF devicePixelSize(CGContextRef context);
    float adjustPenWidth(float penWidth);
    inline void setTransform(const QTransform *matrix = nullptr)
    {
        CGContextConcatCTM(hd, CGAffineTransformInvert(CGContextGetCTM(hd)));
        CGAffineTransform xform = orig_xform;
        if (matrix) {
            extern CGAffineTransform qt_mac_convert_transform_to_cg(const QTransform &);
            xform = CGAffineTransformConcat(qt_mac_convert_transform_to_cg(*matrix), xform);
        }
        CGContextConcatCTM(hd, xform);
        CGContextSetTextMatrix(hd, xform);
    }
};

inline void QCoreGraphicsPaintEnginePrivate::saveGraphicsState()
{
    ++stackCount;
    CGContextSaveGState(hd);
}

inline void QCoreGraphicsPaintEnginePrivate::restoreGraphicsState()
{
    --stackCount;
    Q_ASSERT(stackCount >= 0);
    CGContextRestoreGState(hd);
}

QT_END_NAMESPACE

#endif // QPAINTENGINE_MAC_P_H
