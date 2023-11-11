import secrets
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars, special_chars, special_chars_input=None):
    characters = ''

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_digits:
        characters += string.digits

    if use_special_chars:
        if special_chars_input:
            characters += special_chars_input  # Append special_chars_input if provided
        else:
            characters += special_chars  # Use the default special_chars if special_chars_input is not provided

    if not characters:
        print("Please select at least one character type.")
        return

    password_characters = [secrets.choice(characters) for _ in range(length)]
    password = ''.join(password_characters)

    # Concatenate special_chars_input to the generated password
    if special_chars_input:
        password += special_chars_input

    return password, password_characters, special_chars_input

def main():
    print("Random Password Generator")
    print("------------------------")
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    length = int(input("Enter the password length: "))
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?"

    if use_special_chars:
        special_chars_input = input("Enter special characters to include: ")
    else:
        special_chars_input = ""

    password, password_characters, special_chars_input = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars, special_chars, special_chars_input)

    if password:
        print("Generated Password: ", password)
    else:
        print("Password not generated.")

if __name__ == "__main__":
    main()
