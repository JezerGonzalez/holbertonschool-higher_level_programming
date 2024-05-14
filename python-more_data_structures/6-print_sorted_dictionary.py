def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary)
    for items in sorted_list:
        print(f"{items}: {a_dictionary[items]}")
