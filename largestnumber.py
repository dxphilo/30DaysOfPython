
def biggest_number(numbers):
    dig=0
    for num in numbers:
        if num > dig:
            dig=num
            num+=1
    return dig
