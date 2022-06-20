/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the examples of the Qt Toolkit.
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

#ifndef QQMLSETTINGS_P_H
#define QQMLSETTINGS_P_H

#include "qqmlsettingsglobal_p.h"

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

#include <QtQml/qqml.h>
#include <QtCore/qobject.h>
#include <QtCore/qscopedpointer.h>
#include <QtQml/qqmlparserstatus.h>

QT_BEGIN_NAMESPACE

class QQmlSettingsPrivate;

class Q_LABSSETTINGS_PRIVATE_EXPORT QQmlSettings : public QObject, public QQmlParserStatus
{
    Q_OBJECT
    Q_INTERFACES(QQmlParserStatus)
    Q_PROPERTY(QString category READ category WRITE setCategory FINAL)
    Q_PROPERTY(QString fileName READ fileName WRITE setFileName FINAL)
    QML_NAMED_ELEMENT(Settings)
    QML_ADDED_IN_VERSION(1, 0)

public:
    explicit QQmlSettings(QObject *parent = 0);
    ~QQmlSettings();

    QString category() const;
    void setCategory(const QString &category);

    QString fileName() const;
    void setFileName(const QString &fileName);

    Q_INVOKABLE QVariant value(const QString &key, const QVariant &defaultValue = QVariant()) const;
    Q_INVOKABLE void setValue(const QString &key, const QVariant &value);
    Q_INVOKABLE void sync();

protected:
    void timerEvent(QTimerEvent *event) override;

    void classBegin() override;
    void componentComplete() override;

private:
    Q_DISABLE_COPY(QQmlSettings)
    Q_DECLARE_PRIVATE(QQmlSettings)
    QScopedPointer<QQmlSettingsPrivate> d_ptr;
    Q_PRIVATE_SLOT(d_func(), void _q_propertyChanged())
};

QT_END_NAMESPACE

QML_DECLARE_TYPE(QQmlSettings)

#endif // QQMLSETTINGS_P_H
