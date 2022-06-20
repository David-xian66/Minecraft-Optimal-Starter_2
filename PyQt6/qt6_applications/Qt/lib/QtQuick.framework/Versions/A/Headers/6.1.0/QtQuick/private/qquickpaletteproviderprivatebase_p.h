/****************************************************************************
**
** Copyright (C) 2020 The Qt Company Ltd.
** Contact: http://www.qt.io/licensing/
**
** This file is part of the QtQuick module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL3$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see http://www.qt.io/terms-conditions. For further
** information use the contact form at http://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPLv3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or later as published by the Free
** Software Foundation and appearing in the file LICENSE.GPL included in
** the packaging of this file. Please review the following information to
** ensure the GNU General Public License version 2.0 requirements will be
** met: http://www.gnu.org/licenses/gpl-2.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/
#ifndef QQUICKPALETTEPROVIDERPRIVATEBASE_H
#define QQUICKPALETTEPROVIDERPRIVATEBASE_H

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

#include <QtQuick/private/qquickpalette_p.h>
#include <QtQuick/private/qquickabstractpaletteprovider_p.h>

#include <QtQml/private/qlazilyallocated_p.h>

QT_BEGIN_NAMESPACE

class QWindow;
class QQuickWindow;
class QQuickWindowPrivate;
class QQuickItem;
class QQuickItemPrivate;
class QQuickPopup;
class QQuickPopupPrivate;

/*!
    \internal

    Implements all required operations with palette.

    I -- is interface class (e.g. QQuickItem).
    Impl -- is implementation class (e.g. QQuickItemPrivate).

    To use this class you need to inherit implementation class from it.
 */
template <class I, class Impl>
class QQuickPaletteProviderPrivateBase : public QQuickAbstractPaletteProvider
{
    static_assert(std::is_base_of<QObject, I>{}, "The interface class must inherit QObject");

public:
    virtual ~QQuickPaletteProviderPrivateBase() = default;

    /*!
        \internal

        Get current palette.

        \note Palette might be lazily allocated. Signal \p paletteCreated()
              will be emitted by an object of interface class in this case.

        \note This function doesn't ask an object of interface class to emit
              paletteChanged() signal in order to avoid problems with
              property bindigns.
    */
    virtual QQuickPalette *palette() const;

    /*!
        \internal

        Set new palette. Doesn't transfer ownership.
    */
    virtual void setPalette(QQuickPalette *p);

    /*!
        \internal

        Reset palette to the default one.
    */
    virtual void resetPalette();

    /*!
        \internal

        Check if everything is internally allocated and palette exists.

        Use before call \p palette() to avoid unnecessary allocations.
    */
    virtual bool providesPalette() const;

    /*!
        \internal

        A default palette for this component.
    */
    QPalette defaultPalette() const override;

    /*!
        \internal

        A parent palette for this component. Can be null.
    */
    QPalette parentPalette() const override;

    /*!
        \internal

        Inherit from \p parentPalette. This function is also called when
        either parent or window of this item is changed.
    */
    void inheritPalette(const QPalette &parentPalette);

    /*!
        \internal

        Updates children palettes. The default implementation invokes
        inheritPalette for all visual children.

        This function is also called when palette is changed
        (signal changed() is emitted).
     */
    virtual void updateChildrenPalettes(const QPalette &parentPalette);

private:
    using PalettePtr = std::unique_ptr<QQuickPalette>;
    using Self = QQuickPaletteProviderPrivateBase<I, Impl>;

    void registerPalette(PalettePtr palette);

    bool isValidPalette(const QQuickPalette *palette) const;

    QQuickPalette *windowPalette() const;

    void setCurrentColorGroup();

    void connectItem();

    const I *itemWithPalette() const;
    I *itemWithPalette();

    QQuickPalette *paletteData() const;

    QPalette toQPalette() const;

private:
    PalettePtr m_palette;
};

template<class I, class Impl>
QQuickPalette *QQuickPaletteProviderPrivateBase<I, Impl>::palette() const
{
    if (!providesPalette()) {
        // It's required to create a new palette without parent,
        // because this method can be called from the rendering thread
        const_cast<Self*>(this)->registerPalette(std::make_unique<QQuickPalette>());
        Q_EMIT const_cast<Self*>(this)->itemWithPalette()->paletteCreated();
    }

    return paletteData();
}

template<class I, class Impl>
bool QQuickPaletteProviderPrivateBase<I, Impl>::isValidPalette(const QQuickPalette *palette) const
{
    if (!palette) {
        qWarning("Palette cannot be null.");
        return false;
    }

    if (providesPalette() && paletteData() == palette) {
        qWarning("Self assignment makes no sense.");
        return false;
    }

    return true;
}

template<class I, class Impl>
void QQuickPaletteProviderPrivateBase<I, Impl>::setPalette(QQuickPalette *p)
{
    if (isValidPalette(p)) {
        palette()->fromQPalette(p->toQPalette());
    }
}

template<class I, class Impl>
void QQuickPaletteProviderPrivateBase<I, Impl>::resetPalette()
{
    paletteData()->reset();
}

template<class I, class Impl>
bool QQuickPaletteProviderPrivateBase<I, Impl>::providesPalette() const
{
    return !!m_palette;
}

template<class I, class Impl>
QPalette QQuickPaletteProviderPrivateBase<I, Impl>::defaultPalette() const
{
    return QPalette();
}

template <class Window>
inline constexpr bool isRootWindow() { return std::is_base_of_v<QWindow, Window>; }

template<class I, class Impl>
void QQuickPaletteProviderPrivateBase<I, Impl>::registerPalette(PalettePtr palette)
{
    if constexpr (!isRootWindow<I>()) {
        // Connect item only once, before initial data allocation
        if (!providesPalette()) {
            connectItem();
        }
    }

    m_palette = std::move(palette);
    m_palette->setPaletteProvider(this);
    m_palette->inheritPalette(parentPalette());

    setCurrentColorGroup();

    // In order to avoid extra noise, we should connect
    // the following signals only after everything is already setup
    I::connect(paletteData(), &QQuickPalette::changed, itemWithPalette(), &I::paletteChanged);
    I::connect(paletteData(), &QQuickPalette::changed, [this]{ updateChildrenPalettes(toQPalette()); });
}

template<class T> struct dependent_false : std::false_type {};
template<class Impl, class I> decltype(auto) getPrivateImpl(I &t) { return Impl::get(&t); }

template <class T>
decltype(auto) getPrivate(T &item)
{
    if constexpr (std::is_same_v<T, QQuickWindow>) {
        return getPrivateImpl<QQuickWindowPrivate>(item);
    } else if constexpr (std::is_same_v<T, QQuickItem>) {
        return getPrivateImpl<QQuickItemPrivate>(item);
    } else {
        static_assert (dependent_false<T>::value, "Extend please.");
    }
}

template<class I, class Impl>
QQuickPalette *QQuickPaletteProviderPrivateBase<I, Impl>::windowPalette() const
{
    if constexpr (!isRootWindow<I>()) {
        if (auto window = itemWithPalette()->window()) {
            if (getPrivate(*window)->providesPalette()) {
                return getPrivate(*window)->palette();
            }
        }
    }

    return nullptr;
}

template<class I, class Impl>
QPalette QQuickPaletteProviderPrivateBase<I, Impl>::parentPalette() const
{
    if constexpr (!isRootWindow<I>()) {
        for (auto parentItem = itemWithPalette()->parentItem(); parentItem;
             parentItem = parentItem->parentItem()) {

            // Don't allocate a new palette here. Use only if it's already pre allocated
            if (parentItem && getPrivate(*parentItem)->providesPalette()) {
                return getPrivate(*parentItem)->palette()->toQPalette();
            }
        }

        if (auto wp = windowPalette()) {
            return wp->toQPalette();
        }
    }

    return defaultPalette();
}

template<class I>
const QQuickItem* rootItem(const I &item)
{
    if constexpr (isRootWindow<I>()) {
        return item.contentItem();
    } else if constexpr (std::is_same_v<QQuickPopup, I>) {
        return nullptr;
    } else {
        return &item;
    }
}

template<class I, class Impl>
void QQuickPaletteProviderPrivateBase<I, Impl>::inheritPalette(const QPalette &parentPalette)
{
    if (providesPalette()) {
        // If palette is changed, then this function will be invoked
        // for all children because of connection with signal changed()
        palette()->inheritPalette(parentPalette);
    } else {
        // Otherwise, just propagate parent palette to all children
        updateChildrenPalettes(parentPalette);
    }
}

template<class I, class Impl>
void QQuickPaletteProviderPrivateBase<I, Impl>::setCurrentColorGroup()
{
    if constexpr (!isRootWindow<I>()) {
        if (paletteData()) {
            const bool enabled = itemWithPalette()->isEnabled();
            paletteData()->setCurrentGroup(enabled ? QPalette::Active : QPalette::Disabled);
        }
    }
}

template<class I, class Impl>
void QQuickPaletteProviderPrivateBase<I, Impl>::updateChildrenPalettes(const QPalette &parentPalette)
{
    if constexpr (std::is_same_v<QQuickWindow, I> && std::is_same_v<QQuickWindowPrivate, Impl>) {
        /* QQuickWindowPrivate instantiates this template, but does not include QQuickItemPrivate
         * This causes an error with the QQuickItemPrivate::inheritPalette call below on MSVC in
         * static builds, as QQuickItemPrivate is incomplete. To work around this situation, we do
         * nothing in this instantiation of updateChildrenPalettes and instead add an override in
         * QQuickWindowPrivate, which does the correct thing.
         */
        Q_UNREACHABLE(); // You are not supposed to call this function
        return;
    } else {
        if (auto root = rootItem(*itemWithPalette())) {
            for (auto &&child : root->childItems()) {
                if (Q_LIKELY(child)) {
                    getPrivate(*child)->inheritPalette(parentPalette);
                }
            }
        }
    }
}

template<class I, class Impl>
void QQuickPaletteProviderPrivateBase<I, Impl>::connectItem()
{
    Q_ASSERT(itemWithPalette());

    if constexpr (!isRootWindow<I>()) {
        // Item with palette has the same lifetime as its implementation that inherits this class
        I::connect(itemWithPalette(), &I::parentChanged , [this]() { inheritPalette(parentPalette()); });
        I::connect(itemWithPalette(), &I::windowChanged , [this]() { inheritPalette(parentPalette()); });
        I::connect(itemWithPalette(), &I::enabledChanged, [this]() { setCurrentColorGroup(); });
    }
}

template<class I, class Impl>
const I *QQuickPaletteProviderPrivateBase<I, Impl>::itemWithPalette() const
{
    static_assert(std::is_base_of<QObjectData, Impl>{},
                  "The Impl class must inherit QObjectData");

    return static_cast<const I*>(static_cast<const Impl*>(this)->q_ptr);
}

template<class I, class Impl>
I *QQuickPaletteProviderPrivateBase<I, Impl>::itemWithPalette()
{
    return const_cast<I*>(const_cast<const Self*>(this)->itemWithPalette());
}

template<class I, class Impl>
QQuickPalette *QQuickPaletteProviderPrivateBase<I, Impl>::paletteData() const
{
    Q_ASSERT(m_palette); return m_palette.get();
}

template<class I, class Impl>
QPalette QQuickPaletteProviderPrivateBase<I, Impl>::toQPalette() const
{
    return palette()->toQPalette();
}

QT_END_NAMESPACE

#endif // QQUICKPALETTEPROVIDERPRIVATEBASE_H
