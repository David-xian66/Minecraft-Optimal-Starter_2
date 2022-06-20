/****************************************************************************
**
** Copyright (C) 2020 The Qt Company Ltd.
** Copyright (C) 2018 Intel Corporation.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the QtCore module of the Qt Toolkit.
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

#ifndef QSIMD_H
#define QSIMD_H

#include <QtCore/qglobal.h>

/*
 * qconfig.h defines the QT_COMPILER_SUPPORTS_XXX macros.
 * They mean the compiler supports the necessary flags and the headers
 * for the x86 and ARM intrinsics.
 *
 * Supported instruction set extensions are:
 *   Flag      | Arch
 *  neon       | ARM
 *  mips_dsp   | mips
 *  mips_dspr2 | mips
 *  sse2       | x86
 *  sse4_1     | x86
 *  sse4_2     | x86
 *  avx        | x86
 *
 * Code can use the following constructs to determine compiler support & status:
 * - #if QT_COMPILER_USES(XXX) (e.g: #if QT_COMPILER_USES(neon) or QT_COMPILER_USES(sse4_1)
 *   If this test passes, then the compiler is already generating code using the
 *   given instruction set. The intrinsics for those instructions are
 *   #included and can be used without restriction or runtime check.
 *
 * Code that requires runtime detection and different code paths at runtime is
 * currently not supported here, have a look at qsimd_p.h for support.
 */

#define QT_COMPILER_USES(feature) (1/QT_COMPILER_USES_##feature == 1)

#if defined(Q_PROCESSOR_ARM) && defined(__ARM_NEON) || defined(__ARM_NEON__)
#  include <arm_neon.h>
#  define QT_COMPILER_USES_neon 1
#else
#  define QT_COMPILER_USES_neon -1
#endif

#if defined(Q_PROCESSOR_MIPS) && (defined(__MIPS_DSP__) || (defined(__mips_dsp) && defined(Q_PROCESSOR_MIPS_32)))
#  define QT_COMPILER_USES_mips_dsp 1
#else
#  define QT_COMPILER_USES_mips_dsp -1
#endif

#if defined(Q_PROCESSOR_MIPS) && (defined(__MIPS_DSPR2__) || (defined(__mips_dspr2) && defined(Q_PROCESSOR_MIPS_32)))
#  define QT_COMPILER_USES_mips_dspr2 1
#else
#  define QT_COMPILER_USES_mips_dspr2 -1
#endif

#if defined(Q_PROCESSOR_X86)
#if defined(Q_CC_MSVC)
// MSVC doesn't define __SSE2__, so do it ourselves
#  if (defined(_M_X64) || _M_IX86_FP >= 2)
#    define __SSE__ 1
#    define __SSE2__ 1
#  endif
#if (defined(_M_AVX) || defined(__AVX__))
// Visual Studio defines __AVX__ when /arch:AVX is passed, but not the earlier macros
// See: https://msdn.microsoft.com/en-us/library/b0084kay.aspx
#    define __SSE3__                        1
#    define __SSSE3__                       1
#    define __SSE4_1__                      1
#    define __SSE4_2__                      1
#    ifndef __AVX__
#      define __AVX__                       1
#    endif
#  endif
#  ifdef __SSE2__
#    define QT_VECTORCALL __vectorcall
#  endif
#endif
#endif

#if defined(Q_PROCESSOR_X86) && defined(__SSE2__)
#  include <immintrin.h>
#  define QT_COMPILER_USES_sse2 1
#else
#  define QT_COMPILER_USES_sse2 -1
#endif

#if defined(Q_PROCESSOR_X86) && defined(__SSE3__)
#  define QT_COMPILER_USES_sse3 1
#else
#  define QT_COMPILER_USES_sse3 -1
#endif

#if defined(Q_PROCESSOR_X86) && defined(__SSSE3__)
#  define QT_COMPILER_USES_ssse3 1
#else
#  define QT_COMPILER_USES_ssse3 -1
#endif

#if defined(Q_PROCESSOR_X86) && defined(__SSE4_1__)
#  define QT_COMPILER_USES_sse4_1 1
#else
#  define QT_COMPILER_USES_sse4_1 -1
#endif

#if defined(Q_PROCESSOR_X86) && defined(__SSE4_2__)
#  define QT_COMPILER_USES_sse4_2 1
#else
#  define QT_COMPILER_USES_sse4_2 -1
#endif

#if defined(Q_PROCESSOR_X86) && defined(__AVX__)
#  define QT_COMPILER_USES_avx 1
#else
#  define QT_COMPILER_USES_avx -1
#endif

#ifndef QT_VECTORCALL
#define QT_VECTORCALL
#endif

QT_BEGIN_NAMESPACE
QT_END_NAMESPACE

#endif // QSIMD_H
