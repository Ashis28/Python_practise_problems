codes = {"I":1, "V":5,"X":10,"L":50, "C":100,"D":500,"N":1000,"M":1000 }

def roman_to_int(roman):
    numeral,i=0,0

    while i< len(roman):
        present_num=codes[roman[i]]

        try:
            after_num = codes[roman[i+1]]
        except IndexError:
            return numeral + present_num

        if present_num < after_num: 
            numeral +=after_num- present_num
            i+=2

        else:
            numeral += present_num
            i += 1

    return numeral

roman_num = input("Enter the toman numeral: ")
print(f"{roman_num}--> {roman_to_int(roman_num)}")
