/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
// var timeLimit = function(fn, t) {
    
//     return async function(...args) {
//         return new Promise((res, rej)=>{
//             const timeOutId = setTimeout(()=>{
//                 rej("Time Limit Exceeded");
//             },t);
//         fn(...args).then(res).catch(rej).finally(()=>{clearTimeout(timeOutId)});
//         })
//     }
// };

// // Approach 3: Promise Race
// var timeLimit = function(fn, t) {
    
//     return async function(...args) {
//         const timeLimitPromise = new Promise((res, rej) => {
//             setTimeout(()=>{
//                 rej("Time Limit Exceeded")
//             },t)
//         });
//         const returnedPromise = fn(...args);
//         return Promise.race([timeLimitPromise,returnedPromise]);
//     }
// };

// Approach 4: Async/Await + Clearing Timeout
var timeLimit = function(fn, t) {
    
    return async function(...args) {
        return new Promise( async (res, rej) => {
            const timeoutId = setTimeout(()=>{
                rej("Time Limit Exceeded");
            }, t);

            try{
                const result = await fn(...args);
                res(result);
            }catch(err){
                rej(err);
            }
            clearTimeout(timeoutId);
        })
    }
}

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */