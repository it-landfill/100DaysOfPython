suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

for elem in suitcase:
    print(elem)

for i in range(3):
  print("WARNING!")

#Break
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for bd in dog_breeds_available_for_adoption:
  print(bd)
  if (bd == dog_breed_I_want):
    print("They have the dog I want!")
    break

#Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if (age<21):
    continue
  print(age)


#while
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry)<6:
  students_in_poetry.append(all_students.pop())
print(students_in_poetry)

#List Comprehensions
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height>161]
print(can_ride_coaster)


celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [cels * 9/5 + 32 for cels in celsius]
print(fahrenheit)
