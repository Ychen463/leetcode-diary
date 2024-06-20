/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let i = 0;
    new_arr = []
    while ( i < arr.length) {
        new_arr.push(arr.slice(i, i + size))
        i = i+size 
    }
    return new_arr
};
