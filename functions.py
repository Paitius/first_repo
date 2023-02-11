# def multiply(x,y):
#     return round(x*y,5)


# def no_of_letter(text):
#     return len(text)


def fizz_buzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i
