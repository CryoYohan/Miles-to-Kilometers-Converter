def add(*args):
    numbers = [number for number in args]
    total = sum(numbers)
    return total

if __name__ =="__main__":
    print(add(1,2,3,4,5,6,7,8,9,10))