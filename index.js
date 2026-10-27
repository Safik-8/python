// let arr = [2, 3, 1, 2, 4, 3]
// let pre = [arr[0]]
// let k = 7
// for (let i = 1; i < arr.length; i++) {
//     pre[i] = pre[i - 1] + arr[i]
// }

// let minans = Infinity

// console.log(pre)

// for (let j = 1; j < pre.length; j++) {
//     let sum = pre[j]
//     let i = 0
//     if (sum >= k) {
//         // minans = Math.min(minans, j - i)
//         // while (sum >= k) {
//         //     minans = Math.min(minans, j - i)
//         //     sum -= pre[i]
//         //     i++
//         // }

//         while (i !== j) {
//             if ((pre[j] - pre[i]) >= k) {
//                 minans = Math.min(minans, j - i)
//             }
//             i++
//         }
//     }
// }

// console.log(minans)





// // Transpose

// let arr = [
//     [1, 2, 3],
//     [4, 5, 6],
//     [7, 8, 9],
// ]

// let ans = []

// for (let col = 0; col < arr[0].length; col++) {
//     let cols = []
//     for (let row = 0; row < arr.length; row++) {
//         cols.push(arr[row][col])
//     }
//     // ans.unshift(cols)
//     ans.push(cols.reverse())
// }

// console.log(ans)





