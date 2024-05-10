/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */

const createCounter = (init) => {
    cur = init
    return {
        increment: function() {
            return ++cur;
        },
        decrement: function() {
            return --cur;
        },
        reset: function() {
            cur = init
            return cur;
        }
    };
};

// class Counter {
//     constructor(init) {
//         this.init = init;
//         this.count = init;
//     }

//     increment() {
//         return ++ this.count
//     }
    
//     decrement() {
//         return -- this.count
//     }

//     reset() {
//         this.count = this.init
//         return this.count
//     }
    
// }
// var createCounter = function(init) {
//     return new Counter(init)
// };

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */