print("***Illion Finder (1 - 5459)***")


def florida():
    number = input("Input a number: ")
    a = 0
    
    for i in number:
        if a == 0 and i == "0":
            print("Numbers can't start with a 0 you silly!")
        a += 1
    print(a)
    if a < 3003:
        try:
            int(number) * 1
        except ValueError:
            print("Please try a number next time.")
            return
    if a < 7:
        print("The Number you entered is not long enough.")
    else:  
        var = (a - 4)//3
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
            print("Your number is the eighth illion and it is pronunced as octollion!!!")
        elif var == 9:
            print("Your number is the ninth illion and it is pronunced as nonillion!!!")
        elif var >= 10:
            print("Illion:",var)
            illion = str(var)
            x = 0
            y = ""
            for i in illion[::-1]:
                if i == "0":
                    y += ""
                else:
                    y += str(int(i) * (10**x))
                x += 1
            print(x)
            print(y)
            y = y.replace("10000", "myrilli"
                          ).replace("20000", "dumyrilli"
                                ).replace("30000", "trimyrilli"
                                    ).replace("40000", "quadrimyri"
                                        ).replace("50000", "quinmyri"
                                            ).replace("60000", "sexmyri"
                                                ).replace("70000", "septimyri"
                                                    ).replace("80000", "octomyri"
                                                        ).replace("90000","nonimyri"
                                                            ).replace("1000", "millini"
                                                                ).replace("2000", "dumillini"
                                                                    ).replace("3000", "trimillini"
                                                                        ).replace("4000", "quadrimillini"
                                                                            ).replace("5000", "quinmillini"
                                                                                ).replace("6000", "sexmillini"
                                                                                    ).replace("7000", "septimillini"
                                                                                        ).replace("8000", "octomillini"
                                                                                            ).replace("9000","nonimillini"
                                                                                                ).replace("100","centi"
                                                                                                    ).replace("200", "ducenti"
                                                                                                        ).replace("300", "trucenti"
                                                                                                            ).replace("400", "quadringenti"
                                                                                                                ).replace("500", "quingenti"
                                                                                                                    ).replace("600", "sexagenti"
                                                                                                                        ).replace("700", "septingenti"
                                                                                                                            ).replace("800", "octogenti"
                                                                                                                                ).replace("900","nongenti"
                                                                                                                                    ).replace("10", "deci"
                                                                                                                                        ).replace("20", "viginti"
                                                                                                                                            ).replace("30", "triginti"
                                                                                                                                                ).replace("40", "quadraginti"
                                                                                                                                                    ).replace("50", "quinquaginti"
                                                                                                                                                        ).replace("60", "sexaginti"
                                                                                                                                                            ).replace("70", "septuaginti"
                                                                                                                                                                ).replace("80", "octoginti"
                                                                                                                                                                    ).replace("90","nonaginti"
                                                                                                                                                                        ).replace("1", "Un"
                                                                                                                                                                            ).replace("2", "Duo"
                                                                                                                                                                                ).replace("3", "Tre"
                                                                                                                                                                                    ).replace("4", "Quattour"
                                                                                                                                                                                        ).replace("5", "Quin"
                                                                                                                                                                                            ).replace("6", "Sex"
                                                                                                                                                                                                ).replace("7", "Septen"
                                                                                                                                                                                                    ).replace("8", "Octo"
                                                                                                                                                                                                        ).replace("9","Novem"
                                                                                                                                                                                                            ).replace("0", "" 
                                                                                                                                                                                                                ) + "llion"

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
