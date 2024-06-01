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
    //  Note: Use of await directly on promise1 and promise2 
    // is not as concurrent as using Promise.all(). 
    // As awaiting promises one after the other will 
    // result in a longer total time for resolution 
    // compared to awaiting them concurrently with Promise.all().
    // try{
    //     return await promise1 + await promise2
    // }catch (error) {
    //     console.error(error);
    //     throw new Error(error);
    // }
    // --------------------------------
    // Method 3: Promise.then
    try{
        return promise1.then((val1)=> promise2.then((val2) => val1+val2))
    }catch(error){
        console.error(error);
        throw new Error(error);
    }
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */