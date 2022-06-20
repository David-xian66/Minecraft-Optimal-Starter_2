/****************************************************************************
**
** Copyright (C) 2021 The Qt Company Ltd.
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

#ifndef QTLSBACKEND_OPENSSL_P_H
#define QTLSBACKEND_OPENSSL_P_H

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

#include <private/qtnetworkglobal_p.h>

#include "qssldiffiehellmanparameters.h"
#include "qsslcertificate.h"
#include "qtlsbackend_p.h"

#include <QtCore/qglobal.h>
#include <QtCore/qlist.h>

#include <openssl/ssl.h>

QT_BEGIN_NAMESPACE

class QTlsBackendOpenSSL final : public QTlsBackend
{
public:

    static QString getErrorsFromOpenSsl();
    static void logAndClearErrorQueue();
    static void clearErrorQueue();

    static bool ensureLibraryLoaded();
    // Index used in SSL_get_ex_data to get the matching TlsCryptographerOpenSSL:
    static bool s_libraryLoaded;
    static bool s_loadedCiphersAndCerts;
    static int s_indexForSSLExtraData;

    static QString msgErrorsDuringHandshake();
    static QSslCipher qt_OpenSSL_cipher_to_QSslCipher(const SSL_CIPHER *cipher);
private:

    QString backendName() const override;
    bool isValid() const override;
    long tlsLibraryVersionNumber() const override;
    QString tlsLibraryVersionString() const override;
    long tlsLibraryBuildVersionNumber() const override;
    QString tlsLibraryBuildVersionString() const override;

    void ensureInitialized() const override;
    void ensureCiphersAndCertsLoaded() const;
    static void resetDefaultCiphers();

    QList<QSsl::SslProtocol> supportedProtocols() const override;
    QList<QSsl::SupportedFeature> supportedFeatures() const override;
    QList<QSsl::ImplementedClass> implementedClasses() const override;

    // QSslKey:
    QTlsPrivate::TlsKey *createKey() const override;

    // QSslCertificate:
    QTlsPrivate::X509Certificate *createCertificate() const override;
    QList<QSslCertificate> systemCaCertificates() const override;

    QTlsPrivate::TlsCryptograph *createTlsCryptograph() const override;
    QTlsPrivate::DtlsCookieVerifier *createDtlsCookieVerifier() const override;
    QTlsPrivate::DtlsCryptograph *createDtlsCryptograph(QDtls *q, int mode) const override;

    QTlsPrivate::X509ChainVerifyPtr X509Verifier() const override;
    QTlsPrivate::X509PemReaderPtr X509PemReader() const override;
    QTlsPrivate::X509DerReaderPtr X509DerReader() const override;
    QTlsPrivate::X509Pkcs12ReaderPtr X509Pkcs12Reader() const override;

    // Elliptic curves:
    QList<int> ellipticCurvesIds() const override;
    int curveIdFromShortName(const QString &name) const override;
    int curveIdFromLongName(const QString &name) const override;
    QString shortNameForId(int cid) const override;
    QString longNameForId(int cid) const override;
    bool isTlsNamedCurve(int cid) const override;

    // DH parameters:
    using DHParams = QSslDiffieHellmanParameters;
    int dhParametersFromDer(const QByteArray &derData, QByteArray *data) const override;
    int dhParametersFromPem(const QByteArray &pemData, QByteArray *data) const override;
};

QT_END_NAMESPACE

#endif // QTLSBACKEND_OPENSSL_P_H


