/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
//  // ========== Implementation 1: Subtraction-Based Comparator ============
// var sortBy = function(arr, fn) {
//     return arr.sort((a,b)=>fn(a)-fn(b));
// };
 // ========== Implementation 2: Comparison-Based Comparator ============
var sortBy = function(arr, fn) {
    var swap = (a, b)=>{
        return (fn(a)<fn(b))? -1 : 1
    }
    return arr.sort(swap)
};