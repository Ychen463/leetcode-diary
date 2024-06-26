/**
 * @return {null|boolean|number|string|Array|Object}
 */
//  // ========= Approach 1: Extending Array Prototype to Include a .last() Method
// Array.prototype.last = function() {
//     if (this.length === 0){
//         return -1
//     } 
//     return  this[this.length -1] 
// };
//  // ========= Approach 1: Extending Array Prototype to Include a .last() Method
// Array.prototype.last = function() {
    
//     return  this.length === 0? -1 : this[this.length -1] 
// };
//  // ========= Approach 1: Extending Array Prototype to Include a .last() Method
// Array.prototype.last = function() {
//     let val = this.pop()
//     return  val === undefined? -1: val
// };

 // ========= Approach 1: Extending Array Prototype to Include a .last() Method
Array.prototype.last = function() {
    return  this.length ? this.slice(-1)[0] : -1
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */