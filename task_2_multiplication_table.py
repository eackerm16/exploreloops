number = int(input("Enter a number: "))

output_string = ""
for i in range(1, 11):
    result = number * i
    output_string += f"{number} x {i} = {result} "

print(output_string.strip()) 
