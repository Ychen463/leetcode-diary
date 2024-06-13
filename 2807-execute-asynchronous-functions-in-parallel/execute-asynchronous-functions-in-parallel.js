/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
 // Implementation 1: Using async/await Syntax
// var promiseAll = function(functions) {
//     return new Promise((res,rej) => {
//         if (functions.length == 0){
//             res([]);
//             return;
//         }
//         const newArr = Array(functions.length).fill(null);
//         let resolvedCount = 0;

//         functions.forEach( async (el, idx) =>{
//             try{
//                 const subResult= await el();
//                 newArr[idx] = subResult;
//                 resolvedCount++;
//                 if (resolvedCount == functions.length){
//                     res(newArr);
//                 }
//             } catch(err){
//                 rej(err);
//             }
//         })
//     })
// };

var promiseAll = function(functions) {
    return new Promise((res, rej) => {
        if (functions.length == 0){
            res([]);
            return;
        }
        let resolvedCount =0;
        const newArr = Array(functions.length).fill(null);
        functions.forEach( (el,idx) =>{
            el().then((subResult)=>{
                newArr[idx] = subResult;
                resolvedCount++;
                if (functions.length == resolvedCount){
                    res(newArr);
                }
            }).catch((err)=>{
                rej(err);
            })
        })
    })
}

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */