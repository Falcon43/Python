
class node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.value = val



def insert(root,node):
    if(root == None):
        root = node
    else:
        if root.value < node.value:
            if(root.right == None):
                root.right = node
            else:
                insert(root.right, node)
        else:
            if(root.left == None):
                root.left = node
            else:
                insert(root.left, node)




def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)



def height_tree(root,height):
    if root:
        height +=1
        hleft = height_tree(root.left,height)
        hright = height_tree(root.right,height)
        if hleft == hright:
            return hleft
        elif hleft > hright:
            return hleft
        elif hleft < hright:
            return hright
    else:
        return height



def print_tree(root,tabs):
    if root:
        print(tabs+str(root.value))
        print_tree(root.left,tabs[5:])
        print_tree(root.right,tabs+("\t"*5))





r = node(50)
insert(None,r)
insert(r,node(30))
insert(r,node(20))
insert(r,node(40))
insert(r,node(70))
insert(r,node(60))
insert(r,node(80))
insert(r,node(65))

print(" In order: ")
inorder(r)
height = 0
height = height_tree(r,height)
print("\n\n Height of tree:  "+str(height))

print("\n\n Tree:")
print_tree(r, "\t"*20)

""""
Output:

 In order: 
20
30
40
50
60
65
70
80


 Height of tree:  4


 Tree:
																				50
															30
										20
																				40
																									70
																				60
																									65
																														80




"""
