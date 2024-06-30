def main():
    data = input().split()
    dis = int(data[0])
    price = int(data[1])
    result = (price * 100) / (100 - dis)
    print(f"{result:.2f}")

main()