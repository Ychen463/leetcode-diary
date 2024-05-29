/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const newArray = new Int32Array(arr.length)
    for (let i =0; i < arr.length; i++){
        newArray[i] = fn(arr[i],i)
    }
    return newArray
};