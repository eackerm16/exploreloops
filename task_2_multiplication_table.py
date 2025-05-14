number = int(input("Enter a number: "))

output_string = ""
for i in range(1, 11):
    result = number * i
    output_string += f"{number} x {i} = {result} "

# Remove the trailing space for cleaner output, though the example includes it.
# For exact match with example, use: print(output_string)
print(output_string.strip()) 