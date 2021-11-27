n = int(input("Check this number for prime: "))


# def prime_checker(number=n):
#     p_list = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             p_list.append(i)
#     if len(p_list) == 2:
#         print(f"The number {n} is a prime number")
#     else:
#         print(f"The number {n} is not a prime number")


# prime_checker(n)

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


prime_checker(n)
