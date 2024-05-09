/**
 Do not return anything, modify nums1 in-place instead.
 */
 function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let tail1: number = m-1
    let tail2: number = n-1
    let tail: number = m+n-1
    
    while (tail1>=0 && tail2>=0) {
        if (nums1[tail1]< nums2[tail2]) {
            nums1[tail] = nums2[tail2];
            tail2 --;
            tail --;
        } else {
            nums1[tail] = nums1[tail1];
            tail1 --;
            tail --;
        }
    }

    while (tail2>=0) {
        nums1[tail] = nums2[tail2];
        tail --;
        tail2 --;
    }
    while (tail1>=0) {
        nums1[tail] = nums1[tail1];
        tail --;
        tail1 --;
    }
};