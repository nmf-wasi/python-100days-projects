def nm(firstName, *lastName):
    """This function takes first and last name(s) and returns names in title case"""
    # Combine the first name with all last names
    full_name = firstName + " " + " ".join(lastName)
    return full_name.title()


# Test the function
print(nm("wasi", "yuna", "lia"))  # Output: Wasi Uddin Khan
