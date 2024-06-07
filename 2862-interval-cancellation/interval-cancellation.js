/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
//  // Method 1: Using setInterval & clearInterval
// var cancellable = function(fn, args, t) {
//     fn(...args);
//     const intervalId = setInterval(() => fn(...args),t);
//     const cancelFn = () => clearInterval(intervalId);
//     return cancelFn;
// };
// ================================================================
// // Method 2: Using Recursion (1)
// var cancellable = function(fn, args, t) {
//     let isCancelled = false;
//     fn(...args);
//     const startInterval = () => {
//         setTimeout( () => {
//             if (isCancelled) return;
//             fn(...args);
//             startInterval();
//         },t);
//     }
//     startInterval();
//     const cancelInterval = () => {
//         isCancelled = true;
//     }
//     return cancelInterval;
// }

// ================================================================
// Method 2: Using Recursion (2)
var cancellable = function(fn, args, t) {
    let timeId = null;
    fn(...args);
    const startInterval = () => {
        timeId = setTimeout( () => {
            fn(...args);
            startInterval();
        },t);
    }
    startInterval();
    const cancelInterval = () => {
        if (timeId !== null){
            clearTimeout(timeId);
        }
    }
    return cancelInterval;
}
/**
 *  const result = [];
 *
 *  const fn = (x) => x * 2;
 *  const args = [4], t = 35, cancelTimeMs = 190;
 *
 *  const start = performance.now();
 *
 *  const log = (...argsArr) => {
 *      const diff = Math.floor(performance.now() - start);
 *      result.push({"time": diff, "returned": fn(...argsArr)});
 *  }
 *       
 *  const cancel = cancellable(log, args, t);
 *
 *  setTimeout(cancel, cancelTimeMs);
 *   
 *  setTimeout(() => {
 *      console.log(result); // [
 *                           //     {"time":0,"returned":8},
 *                           //     {"time":35,"returned":8},
 *                           //     {"time":70,"returned":8},
 *                           //     {"time":105,"returned":8},
 *                           //     {"time":140,"returned":8},
 *                           //     {"time":175,"returned":8}
 *                           // ]
 *  }, cancelTimeMs + t + 15)    
 */