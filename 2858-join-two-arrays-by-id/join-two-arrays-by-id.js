/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const merged = {}
    const concatArr = arr1.concat(arr2);
    concatArr.forEach((obj)=>{
        const id = obj.id;
        if (!merged[id]){
            merged[id] = {... obj};
        } else {
            merged[id] = {... merged[id], ... obj}; // overRide with Arr2;
        }
    })
    const returnArr = Object.values(merged);
    returnArr.sort((a,b)=> (a.id > b.id) ? 1 : -1)
    return returnArr
};