import tutorial01 as A1

<<<<<<< HEAD
actual_answers = [9, 12, 80, 5, [2, 6, 18, 54, 162],[1/5,1/4,1/3,1/2,1,0,-1,-1/2,-1/3,-1/4],0]
student_answers = []
=======
actual_answers = [9, 12, 28, 5]
student_answers = [9, 12, 28, 5]
>>>>>>> f806065adaaef99cd03329d4e91dc31f09086b22

test_case_1 = A1.add(4, 5)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(14, 2)
student_answers.append(test_case_2)


test_case_3 = A1.multiply(10, 8)
student_answers.append(test_case_3)

test_case_4 = A1.divide(10, 2)
student_answers.append(test_case_4)

# Driver code 

a = 2 # starting number 
r = 3 # Common ratio 
n = 5 # N th term to be find 

gp = A1.printGP(a, r, n) 
gp = list(gp) 
student_answers.append(gp)

print(gp)
print(actual_answers)
print(student_answers)

a=5
d=-1
n=10
hp= A1.printHP(a,d,n)
hp=list(hp)
student_answers.append(hp)

print(hp)
print(actual_answers)
print(student_answers)

num1='a'
num2=0
power=A1.power(num1,num2)
student_answers.append(power)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print(f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")

