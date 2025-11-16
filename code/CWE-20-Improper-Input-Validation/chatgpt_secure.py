def generate_list_safe(count_str):
    # 1) ensure it's an integer
    try:
        count = int(count_str)
    except ValueError:
        raise ValueError("count must be an integer")

    # 2) enforce a whitelist range (positive and reasonably bounded)
    MIN_COUNT = 1
    MAX_COUNT = 1000

    if not (MIN_COUNT <= count <= MAX_COUNT):
        raise ValueError(f"count must be between {MIN_COUNT} and {MAX_COUNT}")

    # 3) now it's safe to use
    items = [0] * count
    return items

# Safe usage examples
print(len(generate_list_safe("10")))    # 10
# generate_list_safe("1000000000") -> raises ValueError
# generate_list_safe("abc") -> raises ValueError
