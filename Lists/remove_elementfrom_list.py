
list1= [4, 2, 6, 8, 9, 3, 10, 12, 16, 18, 3]

# Removing elements from List
# using iterator method
for i in range(6, 12):
      if i in list1:
          list1.remove(i)
print("\nList after Removing a range of elements: ")
print(list1)