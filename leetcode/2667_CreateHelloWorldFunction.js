/**
 * @return {Function}
 */
// var createHelloWorld = function() {
    
//     return function(...args) {
        
//     }
// };

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */

const createHelloWorld=()=>{
    return function() {
        return 'Hello World';
    }
}
// const createHelloWorld=()=>{
//     return(...args)=>{
//         return'Hello World'
//     }
// }
// // Test the function
const f = createHelloWorld();
console.log(f({}, null, 42));