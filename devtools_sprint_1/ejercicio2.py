def create_phone_number(numbers):
    # Check if the array has exactly 10 numbers
    if len(numbers) != 10:
        return "The list must contain exactly 10 numbers"
    
    for num in numbers:
        if not isinstance(num, int) or num < 0 or num > 9:
            return "The array must contain only positive integers between 0 and 9."
    
    # Convert the first 3 numbers to the format "(###)"
    indicative = ''.join(map(str, numbers[:3]))

    # Convert the next 3 numbers to the format "###-"
    first_part = ''.join(map(str, numbers[3:6]))

    # Convert the last 4 numbers to the format "####"
    second_part = ''.join(map(str, numbers[6:]))

    phone_number = "({}) {}-{}".format(indicative, first_part, second_part)
    # phone_number = f"({indicative}) {first_part}-{second_part}"

    return phone_number


telephone = [3, 1, 0, 4, 5, 1, 6, 6, 0, 0]
print(create_phone_number(telephone))
