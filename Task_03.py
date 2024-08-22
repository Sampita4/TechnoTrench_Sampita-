import random
import string

# Function to generate a password
def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    character_pool = ""
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation
    
    if not character_pool:
        return "Error: No character types selected!"
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# Main function to run the password generator
def password_generator():
    print("Password Generator")
    
    try:
        # Prompt the user for password length
        length = int(input("Enter the desired password length: "))
        
        # Prompt the user for password complexity options
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        
        # Generate and display the password
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Error: Please enter a valid number for the password length.")

if __name__ == "__main__":
    password_generator()
