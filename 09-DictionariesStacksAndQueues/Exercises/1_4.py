###
# Operations on a dictionary
# Types of values: name - str, surname - str, age - int,
# hobby - list, married - bool, phone - dict
#
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
}

print(person["name"])
print(person["hobby"])
print(person)

person["surname"] = "Nowak"
person["married"] = not person["married"]
person["gender"] = "male"
person["hobby"].append("bicycle")
person["phone"]["work"] = "313131444"

for key, value in person.items():
    print(key, ':', value)
