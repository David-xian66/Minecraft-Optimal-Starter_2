/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the QtQml module of the Qt Toolkit.
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

#ifndef QQMLDIRPARSER_P_H
#define QQMLDIRPARSER_P_H

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

#include <QtCore/QUrl>
#include <QtCore/QHash>
#include <QtCore/QDebug>
#include <QtCore/QTypeRevision>
#include <private/qtqmlcompilerglobal_p.h>
#include <private/qqmljsdiagnosticmessage_p.h>

QT_BEGIN_NAMESPACE

class QQmlEngine;
class Q_QMLCOMPILER_PRIVATE_EXPORT QQmlDirParser
{
public:
    void clear();
    bool parse(const QString &source);

    bool hasError() const;
    void setError(const QQmlJS::DiagnosticMessage &);
    QList<QQmlJS::DiagnosticMessage> errors(const QString &uri) const;

    QString typeNamespace() const;
    void setTypeNamespace(const QString &s);

    static void checkNonRelative(const char *item, const QString &typeName, const QString &fileName)
    {
        if (fileName.startsWith(QLatin1Char('/'))) {
            qWarning() << item << typeName
                       << "is specified with non-relative URL" << fileName << "in a qmldir file."
                       << "URLs in qmldir files should be relative to the qmldir file's directory.";
        }
    }

    struct Plugin
    {
        Plugin() = default;

        Plugin(const QString &name, const QString &path, bool optional)
            : name(name), path(path), optional(optional)
        {
            checkNonRelative("Plugin", name, path);
        }

        QString name;
        QString path;
        bool optional = false;
    };

    struct Component
    {
        Component() = default;

        Component(const QString &typeName, const QString &fileName, QTypeRevision version)
            : typeName(typeName), fileName(fileName), version(version),
            internal(false), singleton(false)
        {
            checkNonRelative("Component", typeName, fileName);
        }

        QString typeName;
        QString fileName;
        QTypeRevision version = QTypeRevision::zero();
        bool internal = false;
        bool singleton = false;
    };

    struct Script
    {
        Script() = default;

        Script(const QString &nameSpace, const QString &fileName, QTypeRevision version)
            : nameSpace(nameSpace), fileName(fileName), version(version)
        {
            checkNonRelative("Script", nameSpace, fileName);
        }

        QString nameSpace;
        QString fileName;
        QTypeRevision version = QTypeRevision::zero();
    };

    struct Import
    {
        enum Flag {
            Default  = 0x0,
            Auto     = 0x1, // forward the version of the importing module
            Optional = 0x2  // is not automatically imported but only a tooling hint
        };
        Q_DECLARE_FLAGS(Flags, Flag)

        Import() = default;
        Import(QString module, QTypeRevision version, Flags flags)
            : module(module), version(version), flags(flags)
        {
        }

        QString module;
        QTypeRevision version;     // invalid version is latest version, unless Flag::Auto
        Flags flags;
    };

    QMultiHash<QString,Component> components() const;
    QList<Import> dependencies() const;
    QList<Import> imports() const;
    QList<Script> scripts() const;
    QList<Plugin> plugins() const;
    bool designerSupported() const;

    QStringList typeInfos() const;
    QStringList classNames() const;

private:
    bool maybeAddComponent(const QString &typeName, const QString &fileName, const QString &version, QHash<QString,Component> &hash, int lineNumber = -1, bool multi = true);
    void reportError(quint16 line, quint16 column, const QString &message);

private:
    QList<QQmlJS::DiagnosticMessage> _errors;
    QString _typeNamespace;
    QMultiHash<QString,Component> _components;
    QList<Import> _dependencies;
    QList<Import> _imports;
    QList<Script> _scripts;
    QList<Plugin> _plugins;
    bool _designerSupported = false;
    QStringList _typeInfos;
    QStringList _classNames;
};

using QQmlDirComponents = QMultiHash<QString,QQmlDirParser::Component>;
using QQmlDirScripts = QList<QQmlDirParser::Script>;
using QQmlDirPlugins = QList<QQmlDirParser::Plugin>;
using QQmlDirImports = QList<QQmlDirParser::Import>;

QDebug &operator<< (QDebug &, const QQmlDirParser::Component &);
QDebug &operator<< (QDebug &, const QQmlDirParser::Script &);

QT_END_NAMESPACE

#endif // QQMLDIRPARSER_P_H
