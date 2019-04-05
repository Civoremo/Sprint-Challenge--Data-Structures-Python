import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# --- part of BST
# bst1 = BinarySearchTree(names_1[len(names_1)-1])
# bst2 = BinarySearchTree(names_2[len(names_2)-1])
# for name in names_1:
#     bst1.insert(name)
# for name in names_2:
#     bst2.insert(name)

# duplicates = []
# --- using BST --- results in under 1 sec
# for name_1 in names_1:
#     if bst1.contains(name_1) == bst2.contains(name_1):
#         duplicates.append(name_1)

# --- original ---
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# --- results in under 1 hundreth of sec
names = set(names_1) & set(names_2)
duplicates = [None]*len(names)
for index, name in enumerate(names):
    duplicates[index] = name

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

