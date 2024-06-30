def main():
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    k = int(data[2])
    if a % k == 0 and b % k == 0:
        print("Both")
    elif a % k == 0 and b % k != 0:
        print("Memo")
    elif a % k != 0 and b % k == 0:
        print("Momo")
    else:
        print("No One")
main()