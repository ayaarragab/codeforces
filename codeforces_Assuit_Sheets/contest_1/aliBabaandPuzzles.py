def main():
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    c = int(data[2])
    d = int(data[3])
    if a + b - c == d or a - b + c == d or a * b + c == d or a + b * c == d or a * b - c == d or a - b * c == d:
        print("YES")
    else:
        print("NO")
main()