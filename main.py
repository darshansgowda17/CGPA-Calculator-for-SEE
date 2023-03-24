grading = {
    "S" : 10,
    "A" : 9,
    "B" : 8,
    "C" : 7,
    "D" : 6,
    "E" : 5,
}
numerator = 0
credits = 0
print('''🅲 🅶🅿 🅰   🅲🅰 🅻 🅲 🆄 🅻🅰 🆃🅾 🆁''')
print("")
print("Welcome to CGPA Calculator Brought to you by Darshan S Gowda❤")
print("")
count = int(input("Total number of Subjects appearing Including Labs:- "))
i = 1
while i <= count:
    name = input(f"{i}.Subject Name - ")
    credit = float(input(f"How many Credits does {name} Hold? - "))
    grade = input("What is your expected Grade? ")
    numerator += credit * grading[grade.upper()]
    credits += credit
    print("")
    i += 1
cgpa = (numerator / credits).__round__(2)
print(f"Your CGPA according to your Expected Grades is {cgpa}.Subscribe to Brothers Together YouTube Channel for more such Projects.")
print('Thank you😊❤️')


