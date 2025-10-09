#problem 1: String processing

full_name = "john michael smith"
email = "john.smith@university.edu"
phone = "555-123-4567"

first_name = full_name.split()[0]
print(f"First Name: {first_name}")

last_name = full_name.split()[-1]
print(f"Last Name: {last_name}")

name_parts = full_name.split()
initials = ".".join ([name_part[0]for name_part in name_parts]) + "."
print(f"initials: {initials}")

contains_university = "university" in email.lower()
print(f"Contains 'university': {contains_university}")

new_phone = phone.replace("-", " ")
print(f"New Phone Format: {new_phone}")

#problem 3: Movie Review Number Management
numbers = [3, 5, 4, 3, 2, 1, 3]
print(f"Start list: {numbers}")
numbers.append(4)
print(f"\nAfter task 3.2 (append 4): {numbers}")
numbers[2] = 3 
print(f"After task 3.3 (change index 2 to 3): {numbers}")
numbers.remove(1)
print(f"After task 3.4 (remove value 1): {numbers}")
numbers.insert(2, 3)
print(f"After task 3.5 (insert 3 at index 2): {numbers}")
sublist_first_three = numbers[:3]
print(f"\nSublist of the first 3 numbers: {sublist_first_three}")
print("\n--- task 3.7 print outs ---")
print(f"Total review numbers: {len(numbers)}")
print(f"The first review number: {numbers[0]}")
print(f"The last review number: {numbers[-1]}")