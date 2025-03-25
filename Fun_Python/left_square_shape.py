def main():
    n = int(input("Enter an integer greater than 1: "))
    
    if n <= 1:
        print("The number must be greater than 1.")
        return
    
    # P: Build the left square shape
    # 1st horizontal line of n stars
    print('* ' * n)
    
    vertical_line_length = 2 * n - 1
    # Print the vertical line of 2n-1 stars
    for _ in range(vertical_line_length):
        print('*')
    
    # 2nd horizontal line of n stars
    print('* ' * n)

# Call the main function to run the program
if __name__ == "__main__":
    main()