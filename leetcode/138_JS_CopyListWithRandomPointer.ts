/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     next: Node | null
 *     random: Node | null
 *     constructor(val?: number, next?: Node, random?: Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *         this.random = (random===undefined ? null : random)
 *     }
 * }
 */

function copyRandomList(head: Node | null): Node | null {
    let visitedHash = new Map<Node, Node>();
    console.log("see visitedHAsh", visitedHash);

    const cloneNode = (node: Node) => {
        if (node == null) {
            return null
        }
        if (visitedHash.has(node)) {
            return visitedHash.get(node)
        }
        let newNode = new Node(node.val, null, null)
        visitedHash.set(node, newNode)
        newNode.next = cloneNode(node.next)
        newNode.random = cloneNode(node.random)
        return newNode
    }
    return cloneNode(head)
};