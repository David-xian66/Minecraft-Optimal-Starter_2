/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the QtNetwork module of the Qt Toolkit.
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

#ifndef QNETWORKACCESSMANAGER_P_H
#define QNETWORKACCESSMANAGER_P_H

//
//  W A R N I N G
//  -------------
//
// This file is not part of the Qt API.  It exists for the convenience
// of the Network Access API.  This header file may change from
// version to version without notice, or even be removed.
//
// We mean it.
//

#include <QtNetwork/private/qtnetworkglobal_p.h>
#include "qnetworkaccessmanager.h"
#include "qnetworkaccesscache_p.h"
#include "qnetworkaccessbackend_p.h"
#include "private/qnetconmonitor_p.h"
#include "qnetworkrequest.h"
#include "qhsts_p.h"
#include "private/qobject_p.h"
#include "QtNetwork/qnetworkproxy.h"
#include "qnetworkaccessauthenticationmanager_p.h"

#if QT_CONFIG(settings)
#include "qhstsstore_p.h"
#endif // QT_CONFIG(settings)

QT_BEGIN_NAMESPACE

class QAuthenticator;
class QAbstractNetworkCache;
class QNetworkAuthenticationCredential;
class QNetworkCookieJar;

class QNetworkAccessManagerPrivate: public QObjectPrivate
{
public:
    QNetworkAccessManagerPrivate()
        : networkCache(nullptr),
          cookieJar(nullptr),
          thread(nullptr),
#ifndef QT_NO_NETWORKPROXY
          proxyFactory(nullptr),
#endif
          cookieJarCreated(false),
          defaultAccessControl(true),
          redirectPolicy(QNetworkRequest::NoLessSafeRedirectPolicy),
          authenticationManager(QSharedPointer<QNetworkAccessAuthenticationManager>::create())
    {
    }
    ~QNetworkAccessManagerPrivate();

    QThread * createThread();
    void destroyThread();

    void _q_replyFinished(QNetworkReply *reply);
    void _q_replyEncrypted(QNetworkReply *reply);
    void _q_replySslErrors(const QList<QSslError> &errors);
    void _q_replyPreSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator *authenticator);
    QNetworkReply *postProcess(QNetworkReply *reply);
    void createCookieJar() const;

    void authenticationRequired(QAuthenticator *authenticator,
                                QNetworkReply *reply,
                                bool synchronous,
                                QUrl &url,
                                QUrl *urlForLastAuthentication,
                                bool allowAuthenticationReuse = true);
    void cacheCredentials(const QUrl &url, const QAuthenticator *auth);
    QNetworkAuthenticationCredential *fetchCachedCredentials(const QUrl &url,
                                                             const QAuthenticator *auth = nullptr);

#ifndef QT_NO_NETWORKPROXY
    void proxyAuthenticationRequired(const QUrl &url,
                                const QNetworkProxy &proxy,
                                bool synchronous,
                                QAuthenticator *authenticator,
                                QNetworkProxy *lastProxyAuthentication);
    void cacheProxyCredentials(const QNetworkProxy &proxy, const QAuthenticator *auth);
    QNetworkAuthenticationCredential *fetchCachedProxyCredentials(const QNetworkProxy &proxy,
                                                             const QAuthenticator *auth = nullptr);
    QList<QNetworkProxy> queryProxy(const QNetworkProxyQuery &query);
#endif

    QNetworkAccessBackend *findBackend(QNetworkAccessManager::Operation op, const QNetworkRequest &request);
    QStringList backendSupportedSchemes() const;

#if QT_CONFIG(http) || defined(Q_OS_WASM)
    QNetworkRequest prepareMultipart(const QNetworkRequest &request, QHttpMultiPart *multiPart);
#endif

    void ensureBackendPluginsLoaded();

    // this is the cache for storing downloaded files
    QAbstractNetworkCache *networkCache;

    QNetworkCookieJar *cookieJar;

    QThread *thread;


#ifndef QT_NO_NETWORKPROXY
    QNetworkProxy proxy;
    QNetworkProxyFactory *proxyFactory;
#endif

    bool cookieJarCreated;
    bool defaultAccessControl;
    QNetworkRequest::RedirectPolicy redirectPolicy = QNetworkRequest::NoLessSafeRedirectPolicy;

    // The cache with authorization data:
    QSharedPointer<QNetworkAccessAuthenticationManager> authenticationManager;

    // this cache can be used by individual backends to cache e.g. their TCP connections to a server
    // and use the connections for multiple requests.
    QNetworkAccessCache objectCache;

    Q_AUTOTEST_EXPORT static void clearAuthenticationCache(QNetworkAccessManager *manager);
    Q_AUTOTEST_EXPORT static void clearConnectionCache(QNetworkAccessManager *manager);

    QHstsCache stsCache;
#if QT_CONFIG(settings)
    QScopedPointer<QHstsStore> stsStore;
#endif // QT_CONFIG(settings)
    bool stsEnabled = false;

    bool autoDeleteReplies = false;

    int transferTimeout = 0;

    Q_DECLARE_PUBLIC(QNetworkAccessManager)
};

QT_END_NAMESPACE

#endif
