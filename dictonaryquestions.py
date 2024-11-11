# list1={1,2,3,4,5,6}
# list2={"emmanual","kevin","saran","aswajith","anjo"}
# dictionary={}
# for i in range(len(list1)):
#   dictionary[list1[i]]=list2[i]
# print(dictionary)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ["emmanual", "ikku", "anu", "ann", "wawa", "don", "me", "you", "vava"]
dictionary = {}
for i in range(len(list1)):
    dictionary[list1[i]] = list2[i]
print(dictionary)


s = "hteruerhbdyiggd45764₹73##+8)-))"

kevin = {
    'alphabets': 0,
    'numericals': 0,
    'special_characters': 0
}

for i in s:
    if i.isalpha():
        kevin['alphabets'] += 1
    elif i.isdigit():
        kevin['numericals'] += 1
    else:
        kevin['special_characters'] += 1

print(kevin)