/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
//  // ============== Approach 1: Recursive approach ================
// var flat = function (arr, n) {
//     const res = new Array();
//     var flatening(nums, l )=>{
//         for (const num of nums){
//             if (Array.isArray(num) && l > 0){
//                 flatening(num, l-1 );
//             }else{
//                 res.push(num);
//             }
//         }
//     }
//     flatening(arr, n);
//     return res
// };

// ============== Approach 2: Using Iterative Queue ================
var flat = function (arr, n) {
    let nestedArrayElement = true;
    let depth = 0;
    let queue;
    while (nestedArrayElement && depth < n){
        nestedArrayElement = false;
        queue = [];
        for (let num of arr){
            if (Array.isArray(num)){
                queue.push(...num);
                nestedArrayElement = true;
            } else {
                queue.push(num);
            }
        }
        arr = [...queue];
        depth ++;
    }
    return arr;
}