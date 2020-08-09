name = 'Avital'


def main():
    print("hello")

def first():
    print(name)

def second():
    print(2)

def third(x, y = 4):
    return x + y

def four(x, y = 4):
    return x * y

if __name__ == '__main__':
    second()
    first()
    x = third(5, 8)
    print(third(5, 7))
    print(four(5, 5))