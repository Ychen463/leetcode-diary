/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
 // Method 1:  Using Closure
// var cancellable = function(fn, args, t) {
//     const timeoutId = setTimeout(()=>{
//         fn.apply(null,args); // Executed in global scope
//     },t)
//     const cancelFn = ()=>{ //innerScope function
//         clearTimeout(timeoutId); 
//     }
//     return cancelFn;

// };


// =============================================
// Method 2:  Using Boolean flag
var cancellable = function(fn, args, t) {
    let isCancelled = false;

    setTimeout(() => {
        
        if(!isCancelled){
            fn(...args);
        }  
    },t);
    return () =>{
        isCancelled = true;
    };
};








/**
 *  const result = [];
 *
 *  const fn = (x) => x * 5;
 *  const args = [2], t = 20, cancelTimeMs = 50;
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
 *  const maxT = Math.max(t, cancelTimeMs);
 *           
 *  setTimeout(cancel, cancelTimeMs);
 *
 *  setTimeout(() => {
 *      console.log(result); // [{"time":20,"returned":10}]
 *  }, maxT + 15)
 */