from random import randint
class NumberInCoupon(Exception):
    "This number is on the coupon"
    pass

def numbers():
    """
    This function allows the user to input 6 numbers for a lottery bet.

    Returns:
    list of int: A list of 6 unique integers entered by the user.

    The function prompts the user to enter 6 numbers in the range from 1 to 49 for a lottery bet.
    It ensures that the entered numbers are unique and within the valid range. If a number is not an integer
    or has already been entered, the user is informed of the error and prompted to enter the number again.
    Once the user enters 6 valid and unique numbers, the function returns them as a list.
    """

    print("Enter 6 numbers you want to bet on.")
    numbers = []
    for x in range(1,7):
        while True:
            i = input(f"{x}: ")
            try:
                if int(i) < 50 and int(i) > 0:
                    if i in numbers:
                        raise NumberInCoupon
                    numbers.append(int(i))
                    break
                else:
                    print(f"{i} is not a number from 1 to 49")
            except ValueError:
                print(f"'{i}' is not a number")
            except NumberInCoupon:
                print(f"{i} is on the coupon")
    return numbers

def lottery(a):
    """
    Generate a list of unique random numbers in the range from 1 to 49.

    Args:
    a (int): The number of random numbers to generate.

    Returns:
    list of int: A list of 'a' unique random integers in the range from 1 to 49.

    This function generates a list of 'a' unique random integers in the range from 1 to 49 for a lottery draw.
    It ensures that the generated numbers are unique.
    If a duplicate is generated, the function skips it and continues generating until 'a' unique numbers are obtained.
    The resulting list of numbers is returned.
    """

    table = []
    for x in range(0,a):
        while len(table) != 6:
            try:
                i = randint(1,49)
                if i in table:
                    raise NumberInCoupon
                table.append(i)
            except NumberInCoupon:
                break
    return table


print("Oh! You want to play a Lottery game!\nGreat! Enter Your 6 numbers.")

bet = sorted(numbers())
winning_numbers = sorted(lottery(6))

if bet == winning_numbers:
    print("WOW! YOU WON!")
else:
    counter = 0
    for number in bet:
        print(number)
        if number in winning_numbers:
            counter += 1
    print(f"Sorry! You get only {counter} wright numbers")
    print(f"The winning numbers are {winning_numbers}")

