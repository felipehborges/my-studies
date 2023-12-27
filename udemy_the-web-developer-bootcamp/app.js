//// ==================================================>
//// 283. Creating Our Own Promises

//// Defining the Promise in the variable "fakeRequest"
// const fakeRequest = (url) => {
//     return new Promise((resolve, reject) => {
//         const rand = Math.random();
//         setTimeout(() => {
//             if (rand < 0.7) {
//                 resolve('***FAKE DATA***');
//             } else {
//                 reject('Request ERROR!');
//             }
//         }, 1000)
//     })
// }

//// Promise in practice
// fakeRequest('/dogs/1')
//     .then((data) => {
//         console.log("DONE WITH REQUEST!")
//         console.log(`Here is your data: ${data}`)
//     })
//     .catch((err) => {
//         console.log("OH NO!", err)
//     })

//// Doesn't matter the name we call the parameters, the first one will be the RESOLVED request, and the second one will be the REJECTED one.

//// ==================================================>
//// 284. The Async Keyword



//// ==================================================>
//// 285. The Await Keyword



//// ==================================================>
//// ==================================================>
//// ==================================================>
//// ==================================================>
//// ==================================================>
//// ==================================================>