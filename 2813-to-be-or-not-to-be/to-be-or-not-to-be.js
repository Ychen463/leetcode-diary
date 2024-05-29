/**
 * @param {string} val
 * @return {Object}
 */
// var expect = function(val) {
//     return {
//         toBe: (anotherVal) => {
//             if (val !== anotherVal) throw new Error ("Not Equal")  
//             return true;
             
//         },
//         notToBe: (anotherVal)=> {
//             if (val === anotherVal) throw new Error ("Equal")  
//             return true; 
//         }

//     }
// };

class Expect{
    constructor(val){
        this.val = val;
    };
    toBe(anotherVal){
        if (this.val === anotherVal){
            return true
        } throw new Error("Not Equal")            
    };
    notToBe(anotherVal){
        if (this.val !== anotherVal){
            return true
        } throw new Error("Equal")        
    }
}
const expect = (val) => new Expect(val);

// function expect(val) {
//     return new Expect(val);
// }

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */