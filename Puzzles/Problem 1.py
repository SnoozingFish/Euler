working_sum = 0
test_num = 3
end = 1000

while test_num < 1000:
    if test_num % 3 == 0 or test_num % 5 == 0:
        working_sum += test_num
    test_num += 1

print(str(working_sum))
