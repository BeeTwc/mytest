def sums(numbers, ans):
    seen_numbers = {}
    for number in numbers:
        complement = ans - number
        if complement in seen_numbers:
            return True, (complement, number)  
        seen_numbers[number] = True
    return False

#Ex
list = [1, 3, 5, 7, 9, 11]
ans = 12

result, pair = sums(list, ans)

if result:
    print("True")
    print(f"เพราะ: {pair[0]} + {pair[1]} = {ans}")
else:
    print("False")