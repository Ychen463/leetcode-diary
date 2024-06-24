/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
//  // ====== Approach 2: Using Slicing ====== 
// var chunk = function(arr, size) {
//     let i = 0;
//     const new_arr = []
//     while ( i < arr.length) {
//         new_arr.push(arr.slice(i, i + size))
//         i = i+size 
//     }
//     return new_arr
// };

// // ======= Approach 4: Using Reduce ======= 
// var chunk = function(arr, size) {
//     return arr.reduce((chuckedArr, element)=>{
//         const lastChuck = chuckedArr[chuckedArr.length - 1];
//         if (!lastChuck || lastChuck.length === size) {
//             chuckedArr.push([element]);
//         } else{
//             lastChuck.push(element);
//         }
//         return chuckedArr
//     },[])
// }

// ======= Approach 5: Using Push ======= 
var chunk = function(arr, size) {
    let currChunck = []
    const result = []
    for (element of arr){
        if (currChunck.length === size){
            result.push(currChunck);
            currChunck = [];
        }
        currChunck.push(element);
    }
    if (currChunck.length) result.push(currChunck);
    return result
}