function removeElement(nums: number[], val: number): number {
    if (nums.length == 0) return 0;
    let left: number = nums.length-1;
    let right: number = nums.length-1;
    let cnt: number = 0;
    while (left >= 0) {
        if (nums[left] == val) {
            cnt ++;
        }
        if (nums[right] == val){
            while (left<right && nums[right] == val) {
                right --;
            }
        }
        else if (nums[left] == val) {
            nums[left] = nums[right]
            right --;
        } else {
            
        }
        left --;
    }
    const k: number = nums.length - cnt;
    return k;
};