number_input = input("Enter a number: ")
number = int(number_input)
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")