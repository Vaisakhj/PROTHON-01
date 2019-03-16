if __name__ == '__main__':
    print("Enter the sentence:")
    Text = input()
    print("1.All Caps\n 2.Smallcaps\n 3.Title case\n 4.Start Case\n")
    print("Enter the option:")
    n = int(input())
    if n==1:
        print(Text.upper())
    elif n==2:
        print(Text.lower())
    elif n==3:
        print(Text.title())
    elif n==4:
        print(Text.capitalize())
    else:
        print("Wrong choice")