for i in range(101):
    def divisible(numero, divisor):
        if numero % divisor == 0: 
            return True
        else:
            return False
    if divisible(i, 3):
        print('Fizz')
    if divisible(i, 5):
        print('Buzz')
    if not(divisible(i, 3)) and not(divisible(i, 5)):
        print(i)

    