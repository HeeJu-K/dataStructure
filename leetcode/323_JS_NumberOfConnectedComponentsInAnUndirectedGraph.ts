function countComponents(n: number, edges: number[][]): number {
    const map = new Map<number, number[]>();

    edges.forEach(([a, b])=>{
        map.set(a, [...(map.get(a) || []), b]);
        map.set(b, [...(map.get(b) || []), a]);
    })

    const visited = new Set<number>([]);
    let numConnected: number = 0

    const dfs = ( nodeIdx: number ) => {
        if (visited.has(nodeIdx)) return
        visited.add(nodeIdx)

        const neighbors = map.get(nodeIdx) // returns an array of neighbors
        if (!neighbors) return
        neighbors.forEach(neighbor => dfs(neighbor))

        map.delete(nodeIdx)
    }
    let res: number = 0
    for(let i = 0; i<n; i++) {
        if (!visited.has(i)){
            dfs(i);
            res ++;
        }
    }
    return res
};