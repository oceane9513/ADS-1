# This version is for both Python 2.7.x and 3.x.x
# Name 1: Alieu Jallow
# Name 2: Kai Hartung

# Create empty tree
def emptytree ():
    return None

# Insert x into tree t
def insert(t, x):
    if t == None:
        return (x, None , None)
    else:
        key, left, right = t
        if x == key:
            return (key, left, right)
        elif x < key:
            return (key, insert(left, x), right)
        else:
            return (key, left, insert(right, x))

# Create tree by inserting each element in l into an initially empty tree
def treefromlist(l):
    t=emptytree()
    for x in range(0,(len(l))):
        t = insert(t, l[x])
    return t

#implemetnts inorderwalk to output element
def inorderwalk(t):
    if t != None:
        key, left, right = t
        inorderwalk(left)
        print key,
        inorderwalk(right)

#gets the minimum
def tree_minimum(t):
    key, left, right = t
    if left==None:
        return t
    return tree_minimum(left)
#get the maximum
def tree_maximum(t):
    key, left, right = t
    if right==None:
        return t
    return tree_maximum(right)

def transplant(t, node, newnode):
    key, left, right = t
    y = tree_search(t,node)
    z= tree_search(t,newnode)
    p = parent(t,node)
    p_newnode = parent(t,newnode)
    r = root(t)
    plc = leftChild(t,node)
    prc = rightChild(t,node)
    if p == None:
        r = z
    elif y==plc:
        plc = z
    else:
        prc = z
    if z != None:
        p_newnode = p
    return t

#gets the left child of a node x
def leftChild(t,x):
     key, left, right = t
     k,l,r = tree_search(t,x)
     if l == None:
         return None
     else:
         return l
#gets the right child of node x
def rightChild(t,x):
    key, left, right = t
    k,l,r = tree_search(t,x)
    if r ==None:
        return None
    else:
        return r
#get the parent of a node
def  parent(t, x):
    (key, left, right) = t
    y = tree_search(t,x)
    if x==key:
        return None
    else:
        if x<key and y==left:
            return t
        elif x<key and y!=left:
            return parent(left, x)
        else:
            if x>key and y==right:
                return t
            elif x>key and y!=right:
                return parent(right,x)
#implemets search
def tree_search(t,k):
    key,left,right = t
    if t==None or k==key:
        return t
    else:
        if k<key:
            return tree_search(left,k)
        else:
            return tree_search(right, k)

#implemments tree-delete
def tree_delete(t, e):
	if t!=None:
		key, left, right = t
		if key > e:
			t = (key, tree_delete(left,e), right)
		elif key < e:
			t = (key, left, tree_delete(right,e))
		elif key == e:
			if left == None and right == None:
				return emptytree()
			if right != None:
				succ = tree_minimum(right)
				subKey, subLeft, subRight = succ
				t = (subKey, left, tree_delete(right,subKey))
			else:
				pred = tree_maximum(left)
				subKey, subLeft, subRight = pred
				t = (subKey, tree_delete(left,subKey), right)
			return t
	return t


def test():
    t3 = treefromlist ([10,3,5,4,6])
    t4 = treefromlist ([2 ,6 ,7 ,4 ,1])
    t4 = tree_delete(t3,10)
    print tree_delete(t4,6)
    inorderwalk(tree_delete(t4,6))
# python sort.py runs test
if __name__=="__main__":
    test()



