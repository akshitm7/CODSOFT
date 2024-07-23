import string
import random
def generate_password(length, use_uppercase, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    password = generate_password(length, use_uppercase, use_digits, use_special)
    print("Generated Password:", password)
if __name__ == "__main__":
    main()
