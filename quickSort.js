function quickSort(arr) {
    if (arr.length < 2) return arr;
    let pivot = arr[0];
    let less = arr.slice(1).filter((el) => el <= pivot );
    let greater = arr.slice(1).filter((el) => el > pivot);
    return quickSort(less).concat([pivot], quickSort(greater));
}

test = [1, 4, 6, 9, 3, 5, 6, 7, 1, 3, 82748, 13761, 1873, 8173,991, 8, 3]
console.log(quickSort(test))