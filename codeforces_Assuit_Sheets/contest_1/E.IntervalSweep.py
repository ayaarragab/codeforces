def main():
    nums = input().split()
    num1, num2 = int(nums[0]), int(nums[1])
    if abs(num1 - num2) == 1 or num1 - num2 == 0:
        print("YES")
    else:
        print("NO") 
main()