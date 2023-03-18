from about import me 

print(me)

print(me["name"])

print(me["name"] + " " + me["last_name"])

#Modify a dictionary
me["age"] = me["age"] + 1
print(me)

#Adding somethin new
me["color"] = "yellow"
print(me)

#print name:age
#eg: Sergio: 37

print(me["name"] + ": " + str(me["age"]))

#Optional HW
# 1 print the same ^ - but using python string formatting
name = me["name"]
age = me["age"]

print(f"{name} : {age}")

# 2 delete the age key from the dictionary and print the dictionary to confirm 
#del me["age"]
