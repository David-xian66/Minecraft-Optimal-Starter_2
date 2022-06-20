/****************************************************************************
**
** Copyright (C) 2020 The Qt Company Ltd.
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
import QtQuick3D.Effects

Effect {
    // there are only here to get the sampler2Ds declared in the shader
    readonly property TextureInput sprite: TextureInput {
        texture: Texture {}
    }
    readonly property TextureInput glowSampler: TextureInput {
        texture: Texture {}
    }

    property real fadeAmount: 0.25  // 0 - 1
    property real blurQuality: 0.25 // 0.1 - 1.0

    Shader {
        id: vblurVert
        stage: Shader.Vertex
        shader: "qrc:/qtquick3deffects/shaders/motionblurvertical.vert"
    }
    Shader {
        id: vblurFrag
        stage: Shader.Fragment
        shader: "qrc:/qtquick3deffects/shaders/motionblurvertical.frag"
    }

    Shader {
        id: hblurVert
        stage: Shader.Vertex
        shader: "qrc:/qtquick3deffects/shaders/motionblurhorizontal.vert"
    }
    Shader {
        id: hblurFrag
        stage: Shader.Fragment
        shader: "qrc:/qtquick3deffects/shaders/motionblurhorizontal.frag"
    }

    Shader {
        id: blend
        stage: Shader.Fragment
        shader: "qrc:/qtquick3deffects/shaders/blend.frag"
    }

    Buffer {
        id: glowBuffer
        name: "glowBuffer"
        format: Buffer.RGBA8
        textureFilterOperation: Buffer.Nearest
        textureCoordOperation: Buffer.ClampToEdge
        bufferFlags: Buffer.SceneLifetime
        sizeMultiplier: blurQuality
    }

    Buffer {
        id: tempBuffer
        name: "tempBuffer"
        format: Buffer.RGBA8
        textureFilterOperation: Buffer.Linear
        textureCoordOperation: Buffer.ClampToEdge
        bufferFlags: Buffer.None
        sizeMultiplier: blurQuality
    }

    passes: [
        Pass {
            shaders: [ hblurVert, hblurFrag ]
            commands: [
                BufferInput {
                    // Expose the initially empty glowBuffer texture under the
                    // sampler2D glowSampler in the shader. Note the
                    // SceneLifetime and that the next pass writes to the same
                    // texture (accumulate).
                    sampler: "glowSampler"
                    buffer: glowBuffer
                }
            ]
            output: tempBuffer
        },
        Pass {
            shaders: [ vblurVert, vblurFrag ]
            commands: [
                // the texture for tempBuffer will be INPUT in this pass
                BufferInput {
                    buffer: tempBuffer
                }
            ]
            output: glowBuffer
        },
        Pass {
            shaders: blend
            commands: [
                // the texture for glowBuffer will be INPUT in this pass
                BufferInput {
                    buffer: glowBuffer
                },
                // the input texture (that would normally be INPUT) for this pass is exposed to the shader as sprite
                BufferInput {
                    sampler: "sprite"
                }
            ]
        }
    ]
}
