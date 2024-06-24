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

// // ============== Approach 2: Using Iterative Queue ================
// var flat = function (arr, n) {
//     let nestedArrayElement = true
//     let queue;
//     let depth = 0;
//     while(nestedArrayElement && depth < n){
//         queue = [];
//         nestedArrayElement = false;
//         for (const num of arr) {
//             if (Array.isArray(num)){
//                 queue.push(...num)
//                 nestedArrayElement = true
//             } else {
//                 queue.push(num)
//             }
//         }
//         arr = [...queue];
//         depth++;
//     }
//     return arr
// }

// ============== Approach 3: Using Iterative Stack ============== 
var flat = function (arr, n) {
    const stack = [...arr.map((item)=>[item,n])];
    const res = [];

    while (stack.length > 0){
        const [item, depth] = stack.pop();
        if (Array.isArray(item) && depth > 0){
            stack.push(...item.map((el) => [el, depth-1]));
        } else {
            res.push(item);
        }
    }
    return res.reverse();
}
