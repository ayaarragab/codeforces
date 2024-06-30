def main():
    data = input()
    if data == "z":
        print("a")
    else:
        print(chr(ord(data) + 1))
main()