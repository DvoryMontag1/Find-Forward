
from TST_tree_LinkedListNode import LinkedListNode
from TST_tree_node import Node
import TST_tree_node
import TST_tree_LinkedListNode
import pickle


root=Node('m')
# root = Node('')
# video1=LinkedListNode( "05-05-2024","10-00",15)
# video2=LinkedListNode( "05-05-2024","03-00",45)
# video3=LinkedListNode( "05-05-2022","10-00",15)
# video4=LinkedListNode( "05-05-2020","03-00",45)

# TST_tree_node.insert(root, "cat")
# TST_tree_node.insert(root, "car")
# TST_tree_node.insert(root, "person")
# TST_tree_node.insert(root, "table")

# TST_tree_node.traverseTST(root)

# result=TST_tree_node.searchTST(root, "cat")
# TST_tree_LinkedListNode.add_sorted(result,video1)
# TST_tree_LinkedListNode.add_sorted(result,video2)
# TST_tree_LinkedListNode.add_sorted(result,video3)
# TST_tree_LinkedListNode.add_sorted(result,video4)


# שמירת העץ והרשימה לקובץ באמצעות Pickle
data = {"root": root}
TST_tree_node.insert( root,"bicycle")

with open("data.pickle", "wb") as file:
    pickle.dump(data, file)



# טעינת העץ והרשימה מהקובץ באמצעות Pickle
with open("data.pickle", "rb") as file:
    loaded_data = pickle.load(file)

print("ggg")

# TST_tree_LinkedListNode.print_LinkedListNode(result)
# print("Found" if TST_tree_node.searchTST(root, "bu") else "Not Found")



# # דוגמה לשימוש וחיפוש ברשימה המקושרת
# node1 = LinkedListNode("2023-05-19", "10:30", 5)
# node2 = LinkedListNode("2023-05-20", "12:45", 8)
# node3 = LinkedListNode("2023-05-21", "15:20", 3)

# head=node1
# node1.next=node2

# # חיפוש ברשימה המקושרת
# result = TST_tree_LinkedListNode.search_linked_list(result.next, "05-05-2024","03-00")
# if result is not None:
#     print(f"Found: Date: {result.date}, Time: {result.time}, Value: {result.minute}")
# else:
#     print("Element not found")

# This code is contributed by Shivam Tiwari