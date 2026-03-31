# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# # DFS preorder + null markers ("N") + comma-join/split, 
# # serialize tc: O(n), deserialize tc: O(n), sc: O(n) output/tokens + O(d) recursion
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        preorder = []

        def getPreorderString(root):
            if not root:
                preorder.append("N")
                return

            preorder.append(str(root.val))
            
            getPreorderString(root.left)
            getPreorderString(root.right)

        getPreorderString(root)
        return ",".join(preorder)
    
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        n = len(data)
        indx = 0
        preorder = data.split(",")

        def buildTree():
            nonlocal indx
            if indx>n or preorder[indx]=="N":
                indx+=1
                return None

            root= TreeNode(int(preorder[indx]))
            indx+=1
            root.left = buildTree()
            root.right = buildTree()

            return root

        return buildTree()

# # DFS parenthesized preorder "(val left right)" with "()" nulls,
# # serialize tc: O(n^2) due to recursive string concatenation, deserialize tc: O(n), sc: O(n) output + O(d) recursion
# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """

#         def getPreorderString(root) -> str:
#             if not root:
#                 return "()"

#             return "(" + str(root.val) + getPreorderString(root.left) + getPreorderString(root.right) + ")"

#         return getPreorderString(root)
    
        
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """

#         n = len(data)
#         indx = 0

#         def buildTree():
#             nonlocal indx,n
#             if indx>=n or data.startswith("()", indx):
#                 indx+=2
#                 return None

#             indx+=1
#             nextIndx = data.index("(", indx)
#             node = TreeNode(int(data[indx:nextIndx]))

#             indx = nextIndx
#             node.left = buildTree()
#             node.right = buildTree()
#             indx+=1

#             return node

#         return buildTree()



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))