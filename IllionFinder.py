print("***Illion Finder (1 - 999)***")


def florida():
    number = input("Input a number: ")
    a = 0
    try:
        int(number) * 1
    except ValueError:
        print("Please try a number next time.")
        return
    for i in number:
        a += 1
    if a < 7:
        print("The Number you entered is not long enough.")
    if a >= 3004:
        print("The Number you entered is somehow not short enough.")
    else:  
        var = ((a - 1)-3)//3
        if var == 1:
            print("Your number is the first illion and it is pronunced as million!")
        elif var == 2:
            print("Your number is the second illion and it is pronunced as billion!!")
        elif var == 3:
            print("Your number is the third illion and it is pronunced as trillion!!!")
        elif var == 4:
            print("Your number is the fourth illion and it is pronunced as quadrillion!!!")
        elif var == 5:
            print("Your number is the fifth illion and it is pronunced as quintillion!!!")
        elif var == 6:
            print("Your number is the sixth illion and it is pronunced as sextillion!!!")
        elif var == 7:
            print("Your number is the seventh illion and it is pronunced as septillion!!!")
        elif var == 8:
            print("Your number is the eighth illion and it is pronunced as octillion!!!")
        elif var == 9:
            print("Your number is the ninth illion and it is pronunced as nonillion!!!")
        elif var >= 10:
            print("Illion:",var)
            illion = str(var)
            x = 0
            y = ""
            for i in illion[::-1]:
                y += str(int(i) * (10**x))
                x += 1
            print(x)
            y = y.replace("100", "centi").replace("200", "ducenti").replace("300", "trucenti").replace("400", "quadringenti").replace("500", "quingenti").replace("600", "sexagenti").replace("700", "septingenti").replace("800", "octogenti").replace("900","nongenti").replace("10", "deci").replace("20", "viginti").replace("30", "triginti").replace("40", "quadraginti").replace("50", "quinquaginti").replace("60", "sexaginti").replace("70", "septuaginti").replace("80", "octoginti").replace("90","nonaginti").replace("1", "Un").replace("2", "Duo").replace("3", "Tre").replace("4", "Quattour").replace("5", "Quin").replace("6", "Sex").replace("7", "Septen").replace("8", "Octo").replace("9","Novem") + "llion"

            print("Your illion's pronunciation is:", y)

            f = open("illionlogs.txt", 'a+')
            f.write(number + ", " + y + "\n")

var1 = 1
while var1 < 999:
    florida()
    novar1 = input("Another number? (Y or N):")
    if novar1.lower() == "y":
        continue
    else:
        var1 = 999999999999999