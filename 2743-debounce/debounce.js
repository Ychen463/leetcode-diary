/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
 // 这个问题要求你实现防抖高阶函数。
 // 在调用防抖函数后，提供的函数应该在延迟 t 毫秒后以相同的参数调用。
 // 然而，如果在 t 毫秒内再次调用防抖函数，那么提供的函数执行应该被取消，并且计时器重新启动。

// // Approach 1: setTimeout + clearTimeout
// var debounce = function(fn, t) {
//     let timeoutId;
//     return function(...args) {
//         // 如果已有定时器，取消它
//         if (timeoutId){
//             clearTimeout(timeoutId);
//         }
//         // 设置新的定时器
//         timeoutId = setTimeout(()=>{
//             fn(...args);
//         }, t);
//     }
// };
// ============================================
// Approach 2: setInterval + clearInterval
var debounce = function(fn, t) {
    let intervalId;
    return function(...args) {
        const lastCall = Date.now();
        if (intervalId) {
            clearInterval(intervalId)
        }
        
        intervalId = setInterval(()=>{
            if (Date.now() - lastCall >= t){
                fn(...args);
                clearInterval(intervalId)
            }
        }, 1);
     
    }
}

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */