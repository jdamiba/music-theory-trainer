from questions import questions

# different categories of questions can each be their own array, let
# user choose which category????

# maybe questions should be organized by key?, that way user can choose
# to select only particular keys, or major/minor, sharps, flats?

total_questions = int(input("How many questions do you want to answer this session? "))

num_questions = total_questions

if num_questions > len(questions):
    num_questions = len(questions)

correct = 0
incorrect = 0


for question in questions:
    inp = input(question[0] + " ")

    if inp.lower() == question[1]:
        print("Correct." + "\n")
        correct += 1
    else:
        print("Incorrect." + " The correct answer is " + str(question[1]) + ".\n")

        incorrect += 1

    num_questions -= 1

    if num_questions == 0:
        break

print("###Results###")
print("You got " + str(correct) + " questions correct.")
print("You got " + str(incorrect) + " questions incorrect.")
print("You scored " + str((correct / int(total_questions) * 100)) + "%.")
