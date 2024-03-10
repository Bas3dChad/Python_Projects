
#mylist = [1, 2, 3, 4, 5]
#print(mylist)

list1 = ['Hamdan', '2', 'Osama', 3]
print(list1)

cities = ['Atlanta', 'Baltimore', 'Chicago', 'Denver']
cities.append("New York")
cities = cities + ["Barcelona", "London"]
print(cities[10])

print(cities[0])

print("Welcome to " + cities[2])

#Indexing/Adding/Deleting lists

"""
   scores = [11, 23, 45, 67, 60]
scores.append(49)
scores.insert(0, 91)
print(scores)

names = ["Rafay", "Osama", "Hamdan", "Imran"]
names.append('Faizan')
names.insert(2, 'Hamdan')
print(names)

names[3] = "Hamdan_Sheikh"
print(names)
   """
#new_names = names[2:3]
#del names[4:6]

"""
names = ["Rafay", "Osama", "Hamdan", "Imran"]
names.append(2, 'Intaj')
names.remove("Imran")
print(names)
   """

#### In list

#adding (append)
#insert (position will be defined)
#delete (del)
#remove (name will be defined)
  
"""
names = ["Rafay", "Osama", "Hamdan", "Imran"]
new_names = names.pop(1)
print(names)

   """

# .pop index

marks = [60, 90, 75, 48, 55]
#del marks[2]
#marks.pop(1)
#marks.remove(55)
marks.append([34, 98])
del marks[2:4]
print(marks)
