def main():
    x = int(input("Input a value: "))

    if is_even(x):
        print("Pair")
    
    else:
        print("Odd")


def is_even(n):
    if n % 2 ==0:
        return True

    else:
        return False

main()