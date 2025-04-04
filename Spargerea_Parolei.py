import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


real_hash = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
specials = "!@#$"
lowercase = "abcdefghijklmnopqrstuvwxyz"

recursive_count = 0


def generate_passwords(current, upper, digit, special, lower):
    global recursive_count
    recursive_count += 1

    if len(current) == 6:
        if upper == 1 and digit == 1 and special == 1 and lower == 3:
            if hash_password(current) == real_hash:
                print(f"Parola găsită: {current}")
                print(f"Număr apeluri recursive: {recursive_count}")
                return True
        return False

    for char in uppercase:
        if upper < 1 and generate_passwords(current + char, 1, digit, special, lower):
            return True
    for char in digits:
        if digit < 1 and generate_passwords(current + char, upper, 1, special, lower):
            return True
    for char in specials:
        if special < 1 and generate_passwords(current + char, upper, digit, 1, lower):
            return True
    for char in lowercase:
        if lower < 3 and generate_passwords(current + char, upper, digit, special, lower + 1):
            return True

    return False


generate_passwords("", 0, 0, 0, 0)
