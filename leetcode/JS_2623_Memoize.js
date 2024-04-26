/**
 * @param {Function} fn
 * @return {Function}
 */



function memoize(fn) {
    cache = {}
    callCount = 0
    return (...args) => {
        let key = ''
        for (i in args) {
            key += args[i]
            key += ','
        }
        if (key in cache) {
            return cache[key]
        }
        cache[key] = fn(...args)
        callCount += 1
        return cache[key]
    }
}