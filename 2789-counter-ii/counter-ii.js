/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let curCount = init;
    return{
        increment : () => {
            return ++curCount
        },
        reset : () =>{
            curCount = init
            return curCount
        },
        decrement : () =>{
            return --curCount
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */