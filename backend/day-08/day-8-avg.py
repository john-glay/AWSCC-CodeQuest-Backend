# my_list = [5, 9, 2, 3, 1]

# sum = 0
# avg = 0

# for num in my_list:
#     sum += num

# avg = sum / len(my_list)
# print(avg)

def avg(numlist):
    sum = 0
    avg = 0

    for num in numlist:
        sum += num

    avg = sum / len(numlist)
    return avg      # <-- returning the value of avg 

my_list = [5, 9, 2, 3, 1]
my_avg = avg(my_list)
print(my_avg)