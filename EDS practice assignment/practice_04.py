# Function to reverse a number

def reverse_number(num):
    return int(str(num)[::-1])

# Example usage
if __name__ == '__main__':
    number = 12345
    print(f'The reverse of {number} is {reverse_number(number)}')