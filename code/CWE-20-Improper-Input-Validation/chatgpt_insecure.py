def generate_list(count_str):
    # takes a user-supplied string and uses it directly
    count = int(count_str)           # no checks
    items = [0] * count              # could allocate extremely large list
    return items

# Example: caller passes "1000000000" or "-5"
print(len(generate_list("1000000000")))
