/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const returnObject = {};

    for (const each of this){
        const key = fn(each);
        if (key in returnObject){
            returnObject[key].push(each);
        }else{
            returnObject[key] = [each]
        }
    }
    return returnObject
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */