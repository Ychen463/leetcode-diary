/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
// // =========== Approach 1: Using JSON.stringify ===========
// var isEmpty = function(obj) {
//     if (JSON.stringify(obj).length <= 2) return true
//     else return false
// };
// // =========== Approach 2: Using Object.keys ===========
// var isEmpty = function(obj) {
//     return Object.keys(obj).length == 0
// }
// =========== Approach 3: Using loop ===========
var isEmpty = function(obj) {
    for (const _ in obj) return false;
    return true;
}