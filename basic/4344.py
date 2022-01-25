classes = int(input())

for i in range(classes):
    numbers = []
    numbers = list(map(int, input().split()))
    students = numbers[0]
    count = 0
    sum = 0
    for i in range(students):
        sum += numbers[i + 1]

    avg = sum / students

    for i in range(students):
        if numbers[i + 1] > avg:
            count += 1

    num = count / students * 100

    print(f'{num:.3f}%')
