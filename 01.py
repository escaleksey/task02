try:
    n = int(input())
    if n <= 0:
        print('ERROR')
        exit()
    numbers = []
    for i in range(n):
        numbers.append(float(input()))

    print(abs(max(numbers) - min(numbers)))

except Exception:
    print('ERROR')