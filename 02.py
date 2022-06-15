try:
    string = input()
    if not string.strip():
        print('ERROR')
        exit()

    string = string.split()
    result = [elem[-1].upper() for elem in string]
    print(*result)
except Exception:
    print('ERROR')