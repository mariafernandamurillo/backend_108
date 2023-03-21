colors = ['teal', 'PINK', 'PURPLE', 'ORANGE', 'green', 'BLUE', 'YELLOW', 'red', 'pink', 'TEaL', 'PurPLE', 'greEn', 'YELLOW', 'ORAnGE', 'blue', 'RED', 'teal', 'PINk', 'purPle', 'orange', 'GREEN', 'BluE', 'YelLow', 'ReD']

#1. Print how many color there are in the list
print(len(colors))

#2. Get the list of unique color (in lowercase), case insensitive
unique_color = []

for every_color in colors:
    a_color = every_color.lower()
    if a_color not in unique_color:
        unique_color.append(a_color)

print(unique_color)

#3. Given a color, count how many tmes it exist on the list
count = 0
color = "red"

for a_color in colors:
    if color == a_color.lower():
        count = count + 1
print(f"{color}: {count}")

