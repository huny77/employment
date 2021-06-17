n = int(input())
answer = 1
def factorial(n: int) -> None:
    global answer
    if n == 0:
        return
    else:
        answer *= n
        if n == 1:
            print('{}! = {}'.format(n, n))
        else:
            print('{}! = {} * {}!'.format(n, n, n - 1))
        return factorial(n - 1)

factorial(n)
print(answer)

