/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
//  // =========== Approach 1: Brute Force =========== 
// var join = function(arr1, arr2) {
//     const merged = {}
//     const concatArr = arr1.concat(arr2);
//     concatArr.forEach((obj)=>{
//         const id = obj.id;
//         if (!merged[id]){
//             merged[id] = {... obj};
//         } else {
//             merged[id] = {... merged[id], ... obj}; // overRide with Arr2;
//         }
//     })
//     const returnArr = Object.values(merged);
//     returnArr.sort((a,b)=> (a.id > b.id) ? 1 : -1)
//     return returnArr
// };

 // =========== Approach 2: Using Map =========== 
var join = function(arr1, arr2) {
    const map = new Map();
    for (const obj of arr1) map.set(obj.id, obj);
    for (const obj of arr2) {
        if (!map.has(obj.id)) map.set(obj.id, obj)
        else {
            const prevObj = map.get(obj.id);
            for (const key of Object.keys(obj)){
                prevObj[key] = obj[key]
            }
        }
    }
    const res = new Array();
    for (let key of map.keys()) res.push(map.get(key));
    return res.sort((a,b)=>a.id - b.id);
}