start_number = int(input("Enter the starting number: "))

current_number = start_number
output_string = ""

while current_number >= 1:
    output_string += str(current_number) + " "
    current_number -= 1

print(output_string + "Blast off! 🚀") 