roman_lat = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

arabic_lat = [
    (1000, "M"),
    (900,  "CM"),
    (500,  "D"),
    (400,  "CD"),
    (100,  "C"),
    (90,   "XC"),
    (50,   "L"),
    (40,   "XL"),
    (10,   "X"),
    (9,    "IX"),
    (5,    "V"),
    (4,    "IV"),
    (1,    "I")
]

while True:
    question = input("Enter 'a' to convert from Roman to Arabic, 'b' for Arabic to Roman or 'q' to quit: ").lower()
    question = question.replace(" ", "") # remove spaces


    if question == 'q':
        print("goodbye lil g")
        break


    if question == "a":
        roman_to_arabic = input("enter a number(use eng letters): ")

        # check if the input is empty
        if roman_to_arabic == "":
            print("Empty input. Try again.")
            continue

        roman_to_arabic = roman_to_arabic.upper()
        roman_to_arabic = roman_to_arabic.replace(" ", "") # remove spaces
    
        flag = True

        # check if the input is valid
        for ch in roman_to_arabic:
            if ch not in roman_lat:
                flag = False
                print("Wrong input. Try again.")
                break

        #max 3 same symbols in a row
        # if the same symbol is found more than 3 times in a row, it's invalid
        count = 1
        for i in range(1, len(roman_to_arabic)):
            if roman_to_arabic[i] == roman_to_arabic[i - 1]:
                count += 1
                if count > 3:
                    flag = False
                    print("Wrong input. Try again.")
                    break
            else:
                count = 1
        
        
        if flag:
            total = 0
            for i in range(len(roman_to_arabic)):
                value = roman_lat[roman_to_arabic[i]]

                # если справа есть символ и он больше надо минусовать(if sim2 <= sim1 - "+")(VI = 5 + 1)
                # иначе плюс(if sim2 > sim1 - "-")(IV = 5 - 1)
                if i + 1 < len(roman_to_arabic) and roman_lat[roman_to_arabic[i]] < roman_lat[roman_to_arabic[i + 1]]:
                    total -= value
                else:
                    total += value
            print(f"Arabic number is: {total}")

        
    elif question == "b":
        arabic_to_roman = input("enter a number (1-3999): ")

        # check if the input is empty
        if arabic_to_roman == "":
            print("Empty input. Try again.")
            continue

        arabic_to_roman = arabic_to_roman.replace(" ", "")
        arabic_to_roman = int(arabic_to_roman)

        if arabic_to_roman > 0 and arabic_to_roman <= 3999:
            roman = ""

            for value, symbol in arabic_lat:
                while arabic_to_roman >= value:
                    roman += symbol
                    arabic_to_roman -= value
            print(f"Roman numeral is: {roman}")

        else:
            print("Wrong input. Try again.")

    else:
        print("Wrong input. Try again.")