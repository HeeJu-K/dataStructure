class RandomizedSet {
    private map: Map<number, number>; // key: val, val: idx to array
    private list: number[];

    constructor() {
        this.map = new Map<number, number>();
        this.list = [];
    }

    insert(val: number): boolean {
        if (this.map.has(val)) return false
        
        this.map.set(val, this.list.length);
        this.list.push(val);
        return true
    }

    remove(val: number): boolean {
        if (!this.map.has(val)) return false

        let removeIdx: number = this.map.get(val);
        let lastVal: number = this.list[this.list.length-1];
        this.list[removeIdx] = lastVal;
        this.map.set(lastVal, removeIdx);
        this.list.pop();
        this.map.delete(val);
        return true
    }

    getRandom(): number {
        const randIdx: number = Math.floor(Math.random() * this.list.length);
        return this.list[randIdx];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */