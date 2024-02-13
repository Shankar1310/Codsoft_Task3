import random
import string

def generate_password(length, include_letters=True, include_digits=True, include_punctuation=True):
    """Generate a random password based on user specifications."""
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type (letters, digits, punctuation) must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length, include_letters=True, include_digits=True, include_punctuation=True):
    """Generate multiple passwords."""
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, include_letters, include_digits, include_punctuation)
        if password:
            passwords.append(password)
    return passwords

def main():
    print("Password Generator")

    # Prompt the user for password specifications
    try:
        length = int(input("Enter the desired length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
        include_letters = input("Include letters (yes/no): ").lower() == "yes"
        include_digits = input("Include digits (yes/no): ").lower() == "yes"
        include_punctuation = input("Include punctuation (yes/no): ").lower() == "yes"
    except ValueError:
        print("Error: Invalid input.")
        return

    # Generate and display multiple passwords
    passwords = generate_multiple_passwords(num_passwords, length, include_letters, include_digits, include_punctuation)
    
    if passwords:
        print("\nGenerated Passwords:")
        for idx, password in enumerate(passwords, start=1):
            print(f"{idx}. {password}")

if __name__ == "__main__":
    main()
