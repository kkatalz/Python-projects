# This program checks the strength of a password based on the following criteria:
# Very strong: 8 characters or more, at least one uppercase letter, one lowercase letter, one special character, and digits
# Strong: 8 characters or more, at least one uppercase letter, one lowercase letter, and digits
# Medium: 8 characters or more, at least one uppercase letter or lowercase letter, and digits
# Weak: 8 characters or more: digits
# Very weak: 7 characters or fewer: digits

import re


def check_password_strength(user_password):
    
    strength = 0
    very_strong_regex = r"(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-+])(?=.*\d).{8,}"
    strong_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    medium_regex = r"^(?=.*[A-Z])(?=.*\d)|(?=.*[a-z])(?=.*\d).{8,}$"
    weak_regex = r"^\d{8,}$"
    very_weak_regex = r"^\d{1,7}&"
 
    if re.match(very_strong_regex, user_password):
        strength = "Very strong"
    elif re.match(strong_regex, user_password):
        strength = "Strong"
    elif re.match(medium_regex, user_password):
        strength = "Medium"
    elif re.match(weak_regex, user_password):
        strength = "Weak"
    elif re.match(very_weak_regex, user_password):
        strength = "Very weak"
    else:
        strength = "Password is not valid"
    
    return strength

def main():
    user_password = input("Enter a password: ").strip()
    password_strength = check_password_strength(user_password)
    print(f"Password strength: {password_strength}")

if __name__ == '__main__':
    main()