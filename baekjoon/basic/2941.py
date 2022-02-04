croatia_word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in croatia:
    count += croatia_word.count(i)

print(len(croatia_word) - count)

