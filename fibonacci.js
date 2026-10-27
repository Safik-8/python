let fibonacci = (n, arr) => {

    console.log(arr, n)
    if (n < 2) {
        return arr[n] = n
    }

    if (arr[n] === -1) {
        arr[n] = fibonacci(n - 1, arr) + fibonacci(n - 2, arr)
        return arr[n]
    }
    else {
        return arr[n]
    }

}

// Tabular method
let fibonacci2 = (n) => {

    let arr = new Array(n + 1).fill(-1)

    arr[0] = 0
    arr[1] = 1
    for (let i = 2; i <= n; i++) {
        arr[i] = arr[i - 1] + arr[i - 2]
    }

    return arr[n - 1]

}
// optimized Space complexity method
let fibonacci3 = (n) => {

    let prev2 = 0
    let prev1 = 1
    for (let i = 2; i < n; i++) {
        let curr = prev1 + prev2
        console.log(curr)

        // Here a problem appears i swapped below 2 row
        prev2 = prev1
        prev1 = curr

    }

    return prev1

}

let n = 6

let arr = new Array(n + 1).fill(-1)
console.log(arr)

// console.log(fibonacci(n, arr))
// console.log(fibonacci2(n))
console.log(fibonacci3(4))




