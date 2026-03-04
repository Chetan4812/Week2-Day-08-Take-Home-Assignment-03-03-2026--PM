import random
import string


def analyze_password(password):
    score = 0
    missing = []

    length = len(password)

    # ---- Length Scoring ----
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        missing.append("too short")

    # ---- Character Type Flags ----
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # ---- Repeated Character Check ----
    no_repeated = True
    repeat_count = 1

    # ---- For Loop to Analyze Each Character ----
    for i in range(len(password)):
        char = password[i]

        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in "!@#$%^&*":
            has_special = True

        # Check repeated characters more than 2 in a row
        if i > 0 and password[i] == password[i - 1]:
            repeat_count += 1
            if repeat_count > 2:
                no_repeated = False
        else:
            repeat_count = 1

    # ---- Add Points for Character Types ----
    if has_upper:
        score += 1
    else:
        missing.append("uppercase")

    if has_lower:
        score += 1
    else:
        missing.append("lowercase")

    if has_digit:
        score += 1
    else:
        missing.append("digit")

    if has_special:
        score += 1
    else:
        missing.append("special char")

    if no_repeated:
        score += 1
    else:
        missing.append("too many repeated characters")

    return score, missing


def get_strength_rating(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score <= 6:
        return "Strong"
    else:
        return "Very Strong"


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    # ---- For Loop to Generate Password ----
    for _ in range(length):
        password += random.choice(characters)

    return password


# ===============================
# MAIN PROGRAM
# ===============================

while True:   # ---- While Loop Until Strength >= 5 ----
    user_password = input("Enter password: ")

    score, missing = analyze_password(user_password)
    rating = get_strength_rating(score)

    print(f">> Strength: {score}/8 ({rating})")

    if missing:
        print(">> Missing:", ", ".join(missing))

    if score >= 5:
        print(">> Password accepted!")
        break
    else:
        print(">> Try again...\n")


# ===============================
# PASSWORD GENERATOR
# ===============================

print("\n--- Generate Secure Password ---")
length = int(input("Enter desired password length: "))

generated_password = generate_password(length)
print("Generated Password:", generated_password)

score, missing = analyze_password(generated_password)
rating = get_strength_rating(score)

print(f">> Generated Password Strength: {score}/8 ({rating})")
if missing:
    print(">> Missing:", ", ".join(missing))