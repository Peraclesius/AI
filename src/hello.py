def bruhSqr():
    for i in range(10):
        print('bruh ' * i + '      ' + ('bruh ' * (10 - i)))

def tenBruh():
        return '*' * 10

def incBruh():
    for i in range(10):
        print((('  ' * i + tenBruh()) + ('   ' * (10 - i))) * 20)

incBruh()