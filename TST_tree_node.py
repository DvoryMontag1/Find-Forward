
# מימוש של עץ מילון
import pickle




class Node:
	def __init__(self, data):
		self.data = data
		self.isEndOfString = False
		self.left = None
		self.eq = None
		self.right = None
		self.next = None  # מצביע לרשימה הבאה


# הוספת מילה חדשה
def insert(root, word):
	if not root:
		root = Node(word[0])
	if word[0] < root.data:
		root.left = insert(root.left, word)
	elif word[0] > root.data:
		root.right = insert(root.right, word)
	else:
		if len(word) > 1:
			root.eq = insert(root.eq, word[1:])
		else:
			root.isEndOfString = True
	return root


# dfs מעבר על כל המילים בצורה ממוינת - סריקת 
def traverseTSTUtil(root, buffer, depth):
	if root:
		traverseTSTUtil(root.left, buffer, depth)
		buffer[depth] = root.data
		if root.isEndOfString:
			print("".join(buffer[:depth+1]))
		traverseTSTUtil(root.eq, buffer, depth+1)
		traverseTSTUtil(root.right, buffer, depth)


def traverseTST(root):
	buffer = [''] * 50
	traverseTSTUtil(root, buffer, 0)


# חיפוש מילה בעץ ובמקרה ונמצא מוחזר ראש הרשימה המקושרת  
def searchTST(root, word):
	if not root:
		return False
	if word[0] < root.data:
		return searchTST(root.left, word)
	elif word[0] > root.data:
		return searchTST(root.right, word)
	else:
		if len(word) > 1:
			return searchTST(root.eq, word[1:])
		else:
			# return root.isEndOfString
			if root.isEndOfString:
				return root
			else:
				return None
			

# # שמירת העץ והרשימה לקובץ באמצעות Pickle
# root=Node(" ")
# data = {"root": root}
# with open("data.pickle", "wb") as file:
#     pickle.dump(data, file)



# # טעינת העץ והרשימה מהקובץ באמצעות Pickle
# with open("data.pickle", "rb") as file:
#     loaded_data = pickle.load(file)


