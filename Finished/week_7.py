# Assignment #1
num = int(input("Please enter a positive number.\n"))
while num <= 0:
    num = int(input(f"Number 0 {num} is not larger than 0.\n"))
else:
    print("Correct entry.")
count = 0
while num > 1:
    num -= 1
    if(num == 6):
        continue
    print(num)
    count += 1
else:
    print(
        f"All numbers have beeen printed out succesfully.\nA total of {count} numbers have been printed.")
# ################################
# Assignment #2
counter = 5
friends = []
while counter != 0:
    name = input(f"Please enter your friend's name, {counter} entries left.\n")
    friends.append(name)
    counter -= 1
cnt2 = 0
ignored = 0
while cnt2 < 5:
    if friends[cnt2].islower():
        cnt2 += 1
        ignored += 1
        continue
    else:
        print(friends[cnt2])
    cnt2 += 1
print(
    f"Your friends have been successfully printed, and {ignored} have been ignored.\n")
# ################################
# Assignment #3
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
    print(skills.pop())
# ################################
# Assignment #4
friends = []
print("You may only enter 4 friends.")
count = 0
while count < 4:
    name = input(f"Please enter friend #{count+1}.\n").strip()
    if name.isupper():
        print("Wrong entry, please try again.")
        continue
    elif name[0].islower():
        print("First letter is small, captializing..")
        friends.append(name.capitalize())
        print("Friend added.\n")
        count += 1
    else:
        friends.append(name)
        print("Friend added.\n")
        count += 1
else:
    print("4 friends have been added succesfully.")
    print(friends)
# ################################
# Assignment #1 --> Second Sheet
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
count = 1
for num in my_nums:
    if num % 5 == 0:
        print(f"{count} => {num} ")
        count += 1

print("Program finished sucessfully.\n")
# ################################
# Assignment #2 --> Second Sheet
for num in range(1, 21):
    num = str(num)
    if num == "6" or num == "8" or num == "12":
        continue
    else:
        print(num.zfill(2))

print("All numbers printed successfully.\n")
# ################################
# Assignment #3 --> Second Sheet
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}
rank_equiv = {
    'A': 100,
    'B': 80,
    'C': 40
}  # reference for each rank's value
sum = 0
for mainkey, mainvalue in my_ranks.items():
    print(
        f"My rank in {mainkey} is {mainvalue} and this is equal to {rank_equiv[mainvalue]} points.")
    sum += rank_equiv[mainvalue]
print(f"Total points are exactly {sum}.")
# ################################
# Assignment #4 --> Second Sheet
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}
rank_ref = {
    'A': 100,
    'B': 80,
    'C': 40,
    'D': 20
}
# using .items()
for primkey, primvalue in students.items():
    sum = 0
    print("------------------------------")
    print(f"-- Student Name => {primkey}")
    print("------------------------------")
    for secondkey, secondvalue in students[primkey].items():
        print(f"- {secondkey} => {rank_ref[secondvalue]} points.")
        sum += rank_ref[secondvalue]
    print(f"Total points for {primkey} is {sum}")
print("="*80)
# using normal approach
for names in students:
    sum = 0
    print("------------------------------")
    print(f"-- Student Name => {primkey}")
    print("------------------------------")
    for rank in students[names]:
        print(f"- {rank} => {rank_ref[students[names][rank]]} points.")
        sum += rank_ref[students[names][rank]]
    print(f"Total points for {names} is {sum}")
# ################################
