"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node:
            orig_node_map = {} ## val, node reference
            created_node_map = {}
            self.createNodeMaps(node, orig_node_map, created_node_map)
            self.addConnections(orig_node_map, created_node_map)
            return created_node_map[node.val]
        
    def createNodeMaps(self, node, orig_node_map, created_node_map):
        if node:
            if node.val not in orig_node_map:
                orig_node_map[node.val] = node
                created_node_map[node.val] = Node(node.val, [])
                for n in node.neighbors:
                    self.createNodeMaps(n, orig_node_map, created_node_map)
    
    def addConnections(self, orig_node_map, created_node_map):
        for val, createdNode in created_node_map.items():
            for n in orig_node_map[val].neighbors:
                createdNode.neighbors.append(created_node_map[n.val])
            
                
                
