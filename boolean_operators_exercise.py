student = input("are you a student? (y/n) : ")
pets = input("do you have pets? (y/n) : ")
smokes = input("do you smoke? (y/n) : ")

is_student = student == "y"
has_pets = pets == "y"
does_smokes = smokes == "y"

student_can_rent = is_student and not has_pets and not does_smokes
non_student_can_rent = not is_student and not (does_smokes and has_pets)

can_rent = student_can_rent or non_student_can_rent

print("can rent: " + str(can_rent))