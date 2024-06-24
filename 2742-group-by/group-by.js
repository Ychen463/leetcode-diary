/**
 * @param {Function} fn
 * @return {Object}
 */
//  // ========== Approach 1: For Loop ==================
// Array.prototype.groupBy = function(fn) {
//     const returnObject = {};
//     for (const each of this){
//         const key = fn(each);
//         if (key in returnObject){
//             returnObject[key].push(each);
//         }else{
//             returnObject[key] = [each]
//         }
//     }
//     return returnObject
// };
// ====== Approach 2: Reduce  ==================
Array.prototype.groupBy = function(fn) {
    return this.reduce((accum, item)=>{
        const key = fn(item);
        accum[key] ||= [];
        accum[key].push(item);
        return accum;
    },{})
}


/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */