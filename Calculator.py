n = int(input("Enter the number of values:"))
values = []
for i in range(n):
    values.append(int(input("Enter the value:")))

sum_values = 0
product_values = 1
difference_values = values[0]
def divide_values(values):
    result=values[0]
    for value in values[1:]:
        if value==0:
            print("Divide by zero error.")
            return None
        result /=value
    return result


for value in values:
    sum_values += value
    product_values *= value

for value in values[1:]:
    difference_values -= value

division_result=divide_values(values)

print("Sum:", sum_values)
print("Product:", product_values)
print("Difference:", difference_values)
if division_result is not None:
    print("Division:", division_result)

