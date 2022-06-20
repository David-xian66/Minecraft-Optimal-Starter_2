/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the Qt Quick Layouts module of the Qt Toolkit.
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

#ifndef QQUICKLINEARLAYOUT_P_H
#define QQUICKLINEARLAYOUT_P_H

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

#include <QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include "qquicklayout_p.h"
#include "qquickgridlayoutengine_p.h"

QT_BEGIN_NAMESPACE

/**********************************
 **
 ** QQuickGridLayoutBase
 **
 **/
class QQuickGridLayoutBasePrivate;

class Q_QUICKLAYOUT_PRIVATE_EXPORT QQuickGridLayoutBase : public QQuickLayout
{
    Q_OBJECT

    Q_PROPERTY(Qt::LayoutDirection layoutDirection READ layoutDirection WRITE setLayoutDirection
               NOTIFY layoutDirectionChanged REVISION(1, 1))
    QML_ANONYMOUS
    QML_ADDED_IN_VERSION(1, 1)

public:

    QQuickGridLayoutBase();

    explicit QQuickGridLayoutBase(QQuickGridLayoutBasePrivate &dd,
                                  Qt::Orientation orientation,
                                  QQuickItem *parent = 0);

    ~QQuickGridLayoutBase();
    void componentComplete() override;
    void invalidate(QQuickItem *childItem = 0) override;
    Qt::Orientation orientation() const;
    void setOrientation(Qt::Orientation orientation);
    QSizeF sizeHint(Qt::SizeHint whichSizeHint) const override;
    Qt::LayoutDirection layoutDirection() const;
    void setLayoutDirection(Qt::LayoutDirection dir);
    Qt::LayoutDirection effectiveLayoutDirection() const;
    void setAlignment(QQuickItem *item, Qt::Alignment align) override;

    /* QQuickItemChangeListener */
    void itemDestroyed(QQuickItem *item) override;
    void itemVisibilityChanged(QQuickItem *item) override;

protected:
    void updateLayoutItems() override;
    QQuickItem *itemAt(int index) const override;
    int itemCount() const override;

    void rearrange(const QSizeF &size) override;
    virtual void insertLayoutItems() {}

signals:
    Q_REVISION(1, 1) void layoutDirectionChanged();

private:
    void removeGridItem(QGridLayoutItem *gridItem);
    Q_DECLARE_PRIVATE(QQuickGridLayoutBase)
};

class QQuickLayoutStyleInfo;

class QQuickGridLayoutBasePrivate : public QQuickLayoutPrivate
{
    Q_DECLARE_PUBLIC(QQuickGridLayoutBase)

public:
    QQuickGridLayoutBasePrivate() : m_recurRearrangeCounter(0)
                                    , m_rearranging(false)
                                    , m_updateAfterRearrange(false)
                                    , m_layoutDirection(Qt::LeftToRight)
                                    {}

    void mirrorChange() override
    {
        Q_Q(QQuickGridLayoutBase);
        q->invalidate();
    }

    QQuickGridLayoutEngine engine;
    Qt::Orientation orientation;
    unsigned m_recurRearrangeCounter : 2;
    unsigned m_rearranging : 1;
    unsigned m_updateAfterRearrange : 1;
    QVector<QQuickItem *> m_invalidateAfterRearrange;
    Qt::LayoutDirection m_layoutDirection : 2;

    QQuickLayoutStyleInfo *styleInfo;
};

/**********************************
 **
 ** QQuickGridLayout
 **
 **/
class QQuickGridLayoutPrivate;
class Q_QUICKLAYOUT_PRIVATE_EXPORT QQuickGridLayout : public QQuickGridLayoutBase
{
    Q_OBJECT

    Q_PROPERTY(qreal columnSpacing READ columnSpacing WRITE setColumnSpacing NOTIFY columnSpacingChanged)
    Q_PROPERTY(qreal rowSpacing READ rowSpacing WRITE setRowSpacing NOTIFY rowSpacingChanged)
    Q_PROPERTY(int columns READ columns WRITE setColumns NOTIFY columnsChanged)
    Q_PROPERTY(int rows READ rows WRITE setRows NOTIFY rowsChanged)
    Q_PROPERTY(Flow flow READ flow WRITE setFlow NOTIFY flowChanged)
    QML_NAMED_ELEMENT(GridLayout)
    QML_ADDED_IN_VERSION(1, 0)
public:
    explicit QQuickGridLayout(QQuickItem *parent = 0);
    qreal columnSpacing() const;
    void setColumnSpacing(qreal spacing);
    qreal rowSpacing() const;
    void setRowSpacing(qreal spacing);

    int columns() const;
    void setColumns(int columns);
    int rows() const;
    void setRows(int rows);

    enum Flow { LeftToRight, TopToBottom };
    Q_ENUM(Flow)
    Flow flow() const;
    void setFlow(Flow flow);

    void insertLayoutItems() override;

signals:
    void columnSpacingChanged();
    void rowSpacingChanged();

    void columnsChanged();
    void rowsChanged();

    void flowChanged();
private:
    Q_DECLARE_PRIVATE(QQuickGridLayout)
};

class QQuickGridLayoutPrivate : public QQuickGridLayoutBasePrivate
{
    Q_DECLARE_PUBLIC(QQuickGridLayout)
public:
    QQuickGridLayoutPrivate(): columns(-1), rows(-1), flow(QQuickGridLayout::LeftToRight) {}
    int columns;
    int rows;
    QQuickGridLayout::Flow flow;
};


/**********************************
 **
 ** QQuickLinearLayout
 **
 **/
class QQuickLinearLayoutPrivate;
class QQuickLinearLayout : public QQuickGridLayoutBase
{
    Q_OBJECT
    Q_PROPERTY(qreal spacing READ spacing WRITE setSpacing NOTIFY spacingChanged)
public:
    explicit QQuickLinearLayout(Qt::Orientation orientation,
                                QQuickItem *parent = 0);
    void insertLayoutItem(QQuickItem *item);
    qreal spacing() const;
    void setSpacing(qreal spacing);

    void insertLayoutItems() override;

signals:
    void spacingChanged();
private:
    Q_DECLARE_PRIVATE(QQuickLinearLayout)
};

class QQuickLinearLayoutPrivate : public QQuickGridLayoutBasePrivate
{
    Q_DECLARE_PUBLIC(QQuickLinearLayout)
public:
    QQuickLinearLayoutPrivate() {}
};


/**********************************
 **
 ** QQuickRowLayout
 **
 **/
class Q_QUICKLAYOUT_PRIVATE_EXPORT  QQuickRowLayout : public QQuickLinearLayout
{
    Q_OBJECT
    QML_NAMED_ELEMENT(RowLayout)
    QML_ADDED_IN_VERSION(1, 0)

public:
    explicit QQuickRowLayout(QQuickItem *parent = 0)
        : QQuickLinearLayout(Qt::Horizontal, parent) {}
};


/**********************************
 **
 ** QQuickColumnLayout
 **
 **/
class Q_QUICKLAYOUT_PRIVATE_EXPORT QQuickColumnLayout : public QQuickLinearLayout
{
    Q_OBJECT
    QML_NAMED_ELEMENT(ColumnLayout)
    QML_ADDED_IN_VERSION(1, 0)

public:
    explicit QQuickColumnLayout(QQuickItem *parent = 0)
        : QQuickLinearLayout(Qt::Vertical, parent) {}
};

QT_END_NAMESPACE

#endif // QQUICKLINEARLAYOUT_P_H
