/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
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

#ifndef QFUTURE_H
#define QFUTURE_H

#include <QtCore/qglobal.h>

#include <QtCore/qfutureinterface.h>
#include <QtCore/qstring.h>

#include <QtCore/qfuture_impl.h>

#include <type_traits>
#include <vector>

QT_REQUIRE_CONFIG(future);

QT_BEGIN_NAMESPACE

template <typename T>
class QFutureWatcher;

template <typename T>
class QFuture
{
    static_assert (std::is_copy_constructible_v<T>
                   || std::is_move_constructible_v<T>
                   || std::is_same_v<T, void>,
                   "Type with copy or move constructors or type void is required");
public:
    QFuture()
        : d(QFutureInterface<T>::canceledResult())
    { }

    template<typename U = T, typename = QtPrivate::EnableForNonVoid<U>>
    explicit QFuture(QFutureInterface<T> *p) // internal
        : d(*p)
    { }

    template<typename U = T, typename = QtPrivate::EnableForVoid<U>>
    explicit QFuture(QFutureInterfaceBase *p) // internal
        : d(*p)
    {
    }

    template<typename U, typename V = T, typename = QtPrivate::EnableForVoid<V>>
    explicit QFuture(const QFuture<U> &other) : d(other.d)
    {
    }

    template<typename U, typename V = T, typename = QtPrivate::EnableForVoid<V>>
    QFuture<void> &operator=(const QFuture<U> &other)
    {
        d = other.d;
        return *this;
    }

#if defined(Q_CLANG_QDOC)
    ~QFuture() { }
    QFuture(const QFuture<T> &) { }
    QFuture<T> & operator=(const QFuture<T> &) { }
#endif

    void cancel() { d.cancel(); }
    bool isCanceled() const { return d.isCanceled(); }

#if QT_DEPRECATED_SINCE(6, 0)
    QT_DEPRECATED_VERSION_X_6_0("Use setSuspended() instead.")
    void setPaused(bool paused) { d.setSuspended(paused); }

    QT_DEPRECATED_VERSION_X_6_0("Use isSuspending() or isSuspended() instead.")
    bool isPaused() const
    {
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
        return d.isPaused();
QT_WARNING_POP
    }

    QT_DEPRECATED_VERSION_X_6_0("Use toggleSuspended() instead.")
    void togglePaused() { d.toggleSuspended(); }

    QT_DEPRECATED_VERSION_X_6_0("Use suspend() instead.")
    void pause() { suspend(); }
#endif
    bool isSuspending() const { return d.isSuspending(); }
    bool isSuspended() const { return d.isSuspended(); }
    void setSuspended(bool suspend) { d.setSuspended(suspend); }
    void suspend() { setSuspended(true); }
    void resume() { setSuspended(false); }
    void toggleSuspended() { d.toggleSuspended(); }

    bool isStarted() const { return d.isStarted(); }
    bool isFinished() const { return d.isFinished(); }
    bool isRunning() const { return d.isRunning(); }

    int resultCount() const { return d.resultCount(); }
    int progressValue() const { return d.progressValue(); }
    int progressMinimum() const { return d.progressMinimum(); }
    int progressMaximum() const { return d.progressMaximum(); }
    QString progressText() const { return d.progressText(); }
    void waitForFinished() { d.waitForFinished(); }

    template<typename U = T, typename = QtPrivate::EnableForNonVoid<U>>
    inline T result() const;

    template<typename U = T, typename = QtPrivate::EnableForNonVoid<U>>
    inline T resultAt(int index) const;

    template<typename U = T, typename = QtPrivate::EnableForNonVoid<U>>
    bool isResultReadyAt(int resultIndex) const { return d.isResultReadyAt(resultIndex); }

    template<typename U = T, typename = QtPrivate::EnableForNonVoid<U>>
    QList<T> results() const { return d.results(); }

    template<typename U = T, typename = QtPrivate::EnableForNonVoid<U>>
    T takeResult() { return d.takeResult(); }

#if 0
    // TODO: Enable and make it return a QList, when QList is fixed to support move-only types
    template<typename U = T, typename = QtPrivate::EnableForNonVoid<U>>
    std::vector<T> takeResults() { return d.takeResults(); }
#endif

    bool isValid() const { return d.isValid(); }

    template<class Function>
    using ResultType = typename QtPrivate::ResultTypeHelper<Function, T>::ResultType;

    template<class Function>
    QFuture<ResultType<Function>> then(Function &&function);

    template<class Function>
    QFuture<ResultType<Function>> then(QtFuture::Launch policy, Function &&function);

    template<class Function>
    QFuture<ResultType<Function>> then(QThreadPool *pool, Function &&function);

    template<class Function>
    QFuture<ResultType<Function>> then(QObject *context, Function &&function);

#ifndef QT_NO_EXCEPTIONS
    template<class Function,
             typename = std::enable_if_t<!QtPrivate::ArgResolver<Function>::HasExtraArgs>>
    QFuture<T> onFailed(Function &&handler);

    template<class Function,
             typename = std::enable_if_t<!QtPrivate::ArgResolver<Function>::HasExtraArgs>>
    QFuture<T> onFailed(QObject *context, Function &&handler);
#endif

    template<class Function, typename = std::enable_if_t<std::is_invocable_r_v<T, Function>>>
    QFuture<T> onCanceled(Function &&handler);

    template<class Function, typename = std::enable_if_t<std::is_invocable_r_v<T, Function>>>
    QFuture<T> onCanceled(QObject *context, Function &&handler);

    class const_iterator
    {
    public:
        static_assert(!std::is_same_v<T, void>,
                      "It isn't possible to define QFuture<void>::const_iterator");

        typedef std::bidirectional_iterator_tag iterator_category;
        typedef qptrdiff difference_type;
        typedef T value_type;
        typedef const T *pointer;
        typedef const T &reference;

        inline const_iterator() {}
        inline const_iterator(QFuture const * const _future, int _index)
        : future(_future), index(advanceIndex(_index, 0)) { }
        inline const_iterator(const const_iterator &o) : future(o.future), index(o.index)  {}
        inline const_iterator &operator=(const const_iterator &o)
        { future = o.future; index = o.index; return *this; }
        inline const T &operator*() const { return future->d.resultReference(index); }
        inline const T *operator->() const { return future->d.resultPointer(index); }
        inline bool operator!=(const const_iterator &other) const { return index != other.index; }
        inline bool operator==(const const_iterator &o) const { return !operator!=(o); }
        inline const_iterator &operator++()
        { index = advanceIndex(index, 1); return *this; }
        inline const_iterator &operator--()
        { index = advanceIndex(index, -1); return *this; }
        inline const_iterator operator++(int)
        {
            const_iterator r = *this;
            index = advanceIndex(index, 1);
            return r;
        }
        inline const_iterator operator--(int)
        {
            const_iterator r = *this;
            index = advanceIndex(index, -1);
            return r;
        }
        inline const_iterator operator+(int j) const
        { return const_iterator(future, advanceIndex(index, j)); }
        inline const_iterator operator-(int j) const
        { return const_iterator(future, advanceIndex(index, -j)); }
        inline const_iterator &operator+=(int j)
        { index = advanceIndex(index, j); return *this; }
        inline const_iterator &operator-=(int j)
        { index = advanceIndex(index, -j); return *this; }
        friend inline const_iterator operator+(int j, const_iterator k)
        { return const_iterator(k.future, k.advanceIndex(k.index, j)); }

    private:
        /*! \internal

            Advances the iterator index \a idx \a n steps, waits for the
            result at the target index, and returns the target index.

            The index may be -1, indicating the end iterator, either
            as the argument or as the return value. The end iterator
            may be decremented.

            The caller is responsible for not advancing the iterator
            before begin() or past end(), with the exception that
            attempting to advance a non-end iterator past end() for
            a running future is allowed and will return the end iterator.

            Note that n == 0 is valid and will wait for the result
            at the given index.
        */
        int advanceIndex(int idx, int n) const
        {
            // The end iterator can be decremented, leave as-is for other cases
            if (idx == -1 && n >= 0)
                return idx;

            // Special case for decrementing the end iterator: wait for
            // finished to get the total result count.
            if (idx == -1 && future->isRunning())
                future->d.waitForFinished();

            // Wait for result at target index
            const int targetIndex = (idx == -1) ? future->resultCount() + n : idx + n;
            future->d.waitForResult(targetIndex);

            // After waiting there is either a result or the end was reached
            return (targetIndex < future->resultCount()) ? targetIndex : -1;
        }

        QFuture const * future;
        int index;
    };
    friend class const_iterator;
    typedef const_iterator ConstIterator;

    template<class U = T, typename = QtPrivate::EnableForNonVoid<U>>
    const_iterator begin() const { return  const_iterator(this, 0); }

    template<class U = T, typename = QtPrivate::EnableForNonVoid<U>>
    const_iterator constBegin() const { return  const_iterator(this, 0); }

    template<class U = T, typename = QtPrivate::EnableForNonVoid<U>>
    const_iterator end() const { return const_iterator(this, -1); }

    template<class U = T, typename = QtPrivate::EnableForNonVoid<U>>
    const_iterator constEnd() const { return const_iterator(this, -1); }

private:
    friend class QFutureWatcher<T>;

    template<class U>
    friend class QFuture;

    template<class Function, class ResultType, class ParentResultType>
    friend class QtPrivate::Continuation;

    template<class Function, class ResultType>
    friend class QtPrivate::CanceledHandler;

#ifndef QT_NO_EXCEPTIONS
    template<class Function, class ResultType>
    friend class QtPrivate::FailureHandler;
#endif

    using QFuturePrivate =
            std::conditional_t<std::is_same_v<T, void>, QFutureInterfaceBase, QFutureInterface<T>>;

#ifdef QFUTURE_TEST
public:
#endif
    mutable QFuturePrivate d;
};

template<typename T>
template<typename U, typename>
inline T QFuture<T>::result() const
{
    d.waitForResult(0);
    return d.resultReference(0);
}

template<typename T>
template<typename U, typename>
inline T QFuture<T>::resultAt(int index) const
{
    d.waitForResult(index);
    return d.resultReference(index);
}

template <typename T>
inline QFuture<T> QFutureInterface<T>::future()
{
    return QFuture<T>(this);
}

template<class T>
template<class Function>
QFuture<typename QFuture<T>::template ResultType<Function>> QFuture<T>::then(Function &&function)
{
    return then(QtFuture::Launch::Sync, std::forward<Function>(function));
}

template<class T>
template<class Function>
QFuture<typename QFuture<T>::template ResultType<Function>>
QFuture<T>::then(QtFuture::Launch policy, Function &&function)
{
    QFutureInterface<ResultType<Function>> promise(QFutureInterfaceBase::State::Pending);
    QtPrivate::Continuation<std::decay_t<Function>, ResultType<Function>, T>::create(
            std::forward<Function>(function), this, promise, policy);
    return promise.future();
}

template<class T>
template<class Function>
QFuture<typename QFuture<T>::template ResultType<Function>> QFuture<T>::then(QThreadPool *pool,
                                                                             Function &&function)
{
    QFutureInterface<ResultType<Function>> promise(QFutureInterfaceBase::State::Pending);
    QtPrivate::Continuation<std::decay_t<Function>, ResultType<Function>, T>::create(
            std::forward<Function>(function), this, promise, pool);
    return promise.future();
}

template<class T>
template<class Function>
QFuture<typename QFuture<T>::template ResultType<Function>> QFuture<T>::then(QObject *context,
                                                                             Function &&function)
{
    QFutureInterface<ResultType<Function>> promise(QFutureInterfaceBase::State::Pending);
    QtPrivate::Continuation<std::decay_t<Function>, ResultType<Function>, T>::create(
            std::forward<Function>(function), this, promise, context);
    return promise.future();
}

#ifndef QT_NO_EXCEPTIONS
template<class T>
template<class Function, typename>
QFuture<T> QFuture<T>::onFailed(Function &&handler)
{
    QFutureInterface<T> promise(QFutureInterfaceBase::State::Pending);
    QtPrivate::FailureHandler<std::decay_t<Function>, T>::create(std::forward<Function>(handler),
                                                                 this, promise);
    return promise.future();
}

template<class T>
template<class Function, typename>
QFuture<T> QFuture<T>::onFailed(QObject *context, Function &&handler)
{
    QFutureInterface<T> promise(QFutureInterfaceBase::State::Pending);
    QtPrivate::FailureHandler<std::decay_t<Function>, T>::create(std::forward<Function>(handler),
                                                                 this, promise, context);
    return promise.future();
}

#endif

template<class T>
template<class Function, typename>
QFuture<T> QFuture<T>::onCanceled(Function &&handler)
{
    QFutureInterface<T> promise(QFutureInterfaceBase::State::Pending);
    QtPrivate::CanceledHandler<std::decay_t<Function>, T>::create(std::forward<Function>(handler),
                                                                  this, promise);
    return promise.future();
}

template<class T>
template<class Function, typename>
QFuture<T> QFuture<T>::onCanceled(QObject *context, Function &&handler)
{
    QFutureInterface<T> promise(QFutureInterfaceBase::State::Pending);
    QtPrivate::CanceledHandler<std::decay_t<Function>, T>::create(std::forward<Function>(handler),
                                                                  this, promise, context);
    return promise.future();
}

inline QFuture<void> QFutureInterface<void>::future()
{
    return QFuture<void>(this);
}

template <typename T>
QFuture<void> qToVoidFuture(const QFuture<T> &future)
{
    return QFuture<void>(future.d);
}

Q_DECLARE_SEQUENTIAL_ITERATOR(Future)

QT_END_NAMESPACE

#endif // QFUTURE_H
