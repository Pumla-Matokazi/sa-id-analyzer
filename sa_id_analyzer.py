from datetime import date, datetime


def get_id_number():
    try:
        id_number = input("Enter South African ID number: ").strip()

        if not id_number.isdigit():
            raise ValueError("ID number must contain digits only.")

        if len(id_number) != 13:
            raise ValueError("ID number must be exactly 13 digits long.")

        return id_number

    except ValueError as error:
        print(f"Invalid input: {error}")
        return None


def validate_birthdate(id_number):
    try:
        birth_date = id_number[:6]
        datetime.strptime(birth_date, "%y%m%d")
        return True
    except ValueError:
        return False


def extract_birthdate(id_number):
    birth_date = id_number[:6]
    dob = datetime.strptime(birth_date, "%y%m%d").date()
    return dob


def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return age


def extract_gender(id_number):
    sequence = int(id_number[6:10])
    return "Male" if sequence >= 5000 else "Female"


def extract_citizenship(id_number):
    return "South African" if id_number[10] == "0" else "Non-South African"


def analyze_id(id_number):
    if not validate_birthdate(id_number):
        print("Invalid ID number: birth date is not valid.")
        return

    dob = extract_birthdate(id_number)
    age = calculate_age(dob)
    gender = extract_gender(id_number)
    citizenship = extract_citizenship(id_number)

    print("\n--- ID ANALYSIS RESULT ---")
    print(f"ID Number     : {id_number}")
    print(f"Date of Birth : {dob.strftime('%d %b %Y')}")
    print(f"Age           : {age}")
    print(f"Gender        : {gender}")
    print(f"Citizenship   : {citizenship}")


def main():
    id_number = get_id_number()

    if id_number:
        analyze_id(id_number)


if __name__ == "__main__":
    main()

        