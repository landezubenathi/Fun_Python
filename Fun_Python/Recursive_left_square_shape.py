def print_vertical_line(n, count=0):
    """Recursively print a vertical line of 2n-1 stars."""
    if count < 2 * n - 1:
        print('*')
        print_vertical_line(n, count + 1)

def print_horizontal_lines(n):
    """Print two horizontal lines of n stars, separated by a blank line."""
    print('* ' * n)

def main():
    n = int(input("Enter an integer greater than 1: "))
    
    if n <= 1:
        print("The number must be greater than 1.")
        return
    
    # P & O: Build and display the left square shape
    print_horizontal_lines(n)
    print_vertical_line(n)
    print_horizontal_lines(n)

if __name__ == "__main__":
    main()