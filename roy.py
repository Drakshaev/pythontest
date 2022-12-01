def get(value):
    if value > 0:
        return "positive"
    if value < 0:
        return("negative")


if __name__ == '__main__':
    value = int(input())
    print(get(value).upper())

def plus(a,b):
    return(a + b)
if __name__ == '__main__':
    print(2,2)