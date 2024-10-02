number_largest = 24
number_smallest = 16
while number_smallest:
    number_store = number_smallest
    number_smallest = number_largest % number_smallest
    number_largest = number_store
print("HCF is: ", number_largest)