/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    // // Method 1: Promise.all()
    // try {
    //     const [res1, res2] = await Promise.all([promise1, promise2]);
    //     return res1 + res2
    // } catch (error) {
    //     throw new Error(error)
    // }
    
    // return Sum(arrayNum)
    // --------------------------------
    // Method 2: Using only Await
    try{
        return await promise1 + await promise2
    }catch (error) {
        console.error(error);
        throw new Error(error);
    }
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */