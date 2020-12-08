# A programme that prints name and age

all_ages = []
for user in range(0, 3):
    first_name, last_name, age = input("Enter your First Name, Last Name, Age: ").split()
    numbers = int(age)
    # full_friends.extend([first_name, last_name, age])
    print(first_name, last_name, numbers)

    # for age in range(numbers):
    all_ages.append(numbers)

print('Total of age is : {}'.format(sum(all_ages)))
print('Average Age is : {}'.format(sum(all_ages)/len(all_ages)))