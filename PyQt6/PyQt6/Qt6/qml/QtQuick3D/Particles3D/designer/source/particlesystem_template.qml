/****************************************************************************
**
** Copyright (C) 2021 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of Qt Quick 3D.
**
** $QT_BEGIN_LICENSE:GPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 3 or (at your option) any later version
** approved by the KDE Free Qt Foundation. The licenses are as published by
** the Free Software Foundation and appearing in the file LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick
import QtQuick3D
import QtQuick3D.Particles3D

ParticleSystem3D {
    SpriteParticle3D {
        id: spriteParticle
        color: "#ffffff"
        particleScale: 5.0
        maxAmount: 100
    }
    ParticleEmitter3D {
        id: particleEmitter
        particle: spriteParticle
        particleScale: 1.0
        particleEndScale: 1.5
        particleRotationVariation.x: 180
        particleRotationVariation.y: 180
        particleRotationVariation.z: 180
        particleRotationVelocityVariation.x: 200
        particleRotationVelocityVariation.y: 200
        particleRotationVelocityVariation.z: 200
        VectorDirection3D {
            id: dir3d
            direction.z: -100
            directionVariation.x: 10
            directionVariation.y: 10
        }
        velocity: dir3d
        emitRate: 10
        lifeSpan: 1000
        lifeSpanVariation: 100
    }
}
