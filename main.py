import random

for i in range(15):
    print("Hello", i)

tema = int(input('give any number 0-9 to ask our AI, is it the number: '))
n_sensor = 15

weights = [[0 for i in range(15)],
           [0 for i in range(15)],
           [0 for i in range(15)],
           [0 for i in range(15)],
           [0 for i in range(15)],
           [0 for i in range(15)],
           [0 for i in range(15)],
           [0 for i in range(15)],
           [0 for i in range(15)],
           [0 for i in range(15)]]

num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')

nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

numbers_of_lessons = 100000
a = 0
nums_max = []

for j in range(10):
    for i in range(15):
        a += int(nums[j][i])
    if a != 0:
        nums_max.append(a-2)
    else:
        nums_max.append(a-2)
    a = 0
    print(nums_max[j])



def perceptron(Sensor, max, target):
    s = 0
    for i in range (n_sensor):
        s += int(Sensor[i]) * weights[target][i]

    if s >= max:
        return True
    else:
        return False

learning_rate = 0.5
def decrease(number, target):
    for i in range(n_sensor):
        if int(number[i]) == 1:
            weights[target][i] -= learning_rate

def increase(number, target):
    for i in range(n_sensor):
        if int(number[i]) == 1:
            weights[target][i] += learning_rate



for i in range(numbers_of_lessons):
    for q in range(10):
        j = random.randint(0, 9)
        recognized = perceptron(nums[j], nums_max[q], q)
        if j != q:
            if recognized:
                decrease(nums[j], q)
        else:
            if not recognized:
                increase(nums[q], q)

correct = []
for i in range(10):
    a = 0
    for j in range(15):
        if float(nums[i][j]) > 0 and weights[i][j] > 0:
            a += 1
        elif float(nums[i][j]) <= 0 and weights[i][j] <= 0:
            a += 1
    if a == 15:
        correct.append('correct for number ' + str(i))
    else:
        correct.append('wrong for number ' + str(i))

for i in range(10):
    print(weights[i], 'weights for number', i)
    print(nums[i], 'pixels for the number', i)
    print('')

print(correct)

'''print(num1)
if True == perceptron(num1): print('true')
else: print('false')

print(num2)
if True == perceptron(num2): print('true')
else: print('false')'''