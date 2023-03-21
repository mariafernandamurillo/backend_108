#-----Working with lists-----

#Create a list: list_name = []
ages = []

#Add elements: in js we use push, but here we use append
ages.append(30)
ages.append(29)
ages.append(4)
ages.append(1)

#Remove elements by position
ages.pop(2)

#Print the list
print(ages)

#Remove element by value
#ages.remove("1")

#-----Working with for loop-----
#for x in list: for every element in the list

for age in ages:
    print(age)

#Sum all the ages
def sum_ages():
    total = 0
    for age in ages:
        total = total + age
    print(total)

sum_ages()
