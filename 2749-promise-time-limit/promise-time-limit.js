/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    
    return async function(...args) {
        return new Promise((res, rej)=>{
            const timeOutId = setTimeout(()=>{
                rej("Time Limit Exceeded");
            },t);
        fn(...args).then(res).catch(rej).finally(()=>{clearTimeout(timeOutId)});
        })
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */