print("***Illion Finder & WhichIllion***")
translate = {
    "A": 10000,
    "B": 20000,
    "C": 30000,
    "D": 40000,
    "E": 50000,
    "F": 60000,
    "G": 70000,
    "H": 80000,
    "I": 90000,
    "J": 2000,
    "K": 3000,
    "L": 4000,
    "M": 5000,
    "N": 6000,
    "O": 7000,
    "P": 8000,
    "Q": 9000,
    "R": 1000,
    "S": 200,
    "T": 300,
    "U": 400,
    "V": 500,
    "W": 600,
    "X": 700,
    "Y": 800,
    "Z": 900,
    "1": 100,
    "2": 10,
    "3": 20,
    "4": 30,
    "5": 40,
    "6": 50,
    "7": 60,
    "8": 70,
    "9": 80,
    "!": 90,
    "@": 1,
    "#": 2,
    "$": 3,
    "%": 4,
    "^": 5,
    "&": 6,
    "*": 7,
    "(": 8,
    ")": 9,


}

def florida():
    s = "[@_!#$%^&*()<>?/\|}{~:]'"
    zedre = '[@_!#$%^&*()<>?/\|}{~:]"'
    
    number = input("Input a number: ")
    a = 0
    number = number.replace(",", "")
    for i in number:
        if a == 0 and i == "0":
            print("Numbers can't start with a 0 you silly!")
        a += 1
    print(number)
    """if a < 3003:
        try:
            int(number) * 1
        except ValueError:
            print("The string you entered has a non-numerical character in it. please try again.")
            return"""

    for i in number:
        if i.isalpha():
            print("The string you entered has a non-numerical character in it. please try again.")
            return
        elif i in s or i in zedre:
            print("The string you entered has a non-numerical character in it. please try again.")
            return
         
    print("Digits:",a)
    if a < 7:
        print("The Number you entered is not long enough.")
    else:  
        var = (a - 4)//3
        if var == 1:
            print("Your number is the first illion and it's name is a million!")
        elif var == 2:
            print("Your number is the second illion and it's name is a billion!!")
        elif var == 3:
            print("Your number is the third illion and it's name is a trillion!!!")
        elif var == 4:
            print("Your number is the fourth illion and it's name is a quadrillion!!!")
        elif var == 5:
            print("Your number is the fifth illion and it's name is a quintillion!!!")
        elif var == 6:
            print("Your number is the sixth illion and it's name is a sextillion!!!")
        elif var == 7:
            print("Your number is the seventh illion and it's name is a septillion!!!")
        elif var == 8:
            print("Your number is the eighth illion and it's name is a octollion!!!")
        elif var == 9:
            print("Your number is the ninth illion and it's name is a nonillion!!!")
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

            print("Your illion's name is:", y)
            f = open("illionlogs.txt", 'a+')
            f.write(str(number) + ", " + str(y) + ", " + str(var)  + ", " + str(a) +"\n")
def california(): 
        var12 = input("Enter Illion Name: ")
        var12 = var12.lower()
        var12 = var12.replace(" ", "")
        number = 0
        var12 = var12.replace("llion", ""
                        ).replace("nonimyri", "I"
                                ).replace("dumyri", "B"
                                        ).replace("trimyri", "C"
                                                        ).replace("quadrimyri", "D"
                                                                ).replace("quinmyri", "E"
                                                                        ).replace("sexmyri", "F"
                                                                                ).replace("septimyri", "G"
                                                                                                ).replace("octomyri", "H"
                                                                                                        ).replace("myri", "A"
                                                                                                                ).replace("dumillini", "J"
                                                                                                                        ).replace("trimillini", "K"
                                                                                                                                ).replace("quadrimillini", "L"
                                                                                                                                                ).replace("quinmillini", "M"
                                                                                                                                                        ).replace("sexmillini", "N"
                                                                                                                                                                ).replace("septimillini", "O"
                                                                                                                                                                        ).replace("octomillini", "P"
                                                                                                                                                                                        ).replace("nonimillini", "Q"
                                                                                                                                                                                                ).replace("millini", "R"
                                                                                                                                                                                                        ).replace("ducenti", "S"
                                                                                                                                                                                                                ).replace("trucenti", "T"
                                                                                                                                                                                                                        ).replace("quadringenti", "U"
                                                                                                                                                                                                                                ).replace("quingenti", "V"
                                                                                                                                                                                                                                        ).replace("sexagenti", "W"
                                                                                                                                                                                                                                                        ).replace("septingenti", "X"
                                                                                                                                                                                                                                                                ).replace("octogenti", "Y"
                                                                                                                                                                                                                                                                        ).replace("nongenti", "Z"
                                                                                                                                                                                                                                                                                ).replace("centi", "1"
                                                                                                                                                                                                                                                                                        ).replace("deci", "2"
                                                                                                                                                                                                                                                                                                ).replace("viginti", "3"
                                                                                                                                                                                                                                                                                                        ).replace("triginti", "4"
                                                                                                                                                                                                                                                                                                                        ).replace("quadraginti", "5"
                                                                                                                                                                                                                                                                                                                                ).replace("quinquaginti", "6"
                                                                                                                                                                                                                                                                                                                                        ).replace("sexaginti", "7"
                                                                                                                                                                                                                                                                                                                                                ).replace("septuaginti", "8"
                                                                                                                                                                                                                                                                                                                                                                ).replace("octoginti", "9"
                                                                                                                                                                                                                                                                                                                                                                        ).replace("nonaginti", "!"
                                                                                                                                                                                                                                                                                                                                                                                ).replace("un", "@"
                                                                                                                                                                                                                                                                                                                                                                                        ).replace("duo", "#"
                                                                                                                                                                                                                                                                                                                                                                                                ).replace("tre", "$"
                                                                                                                                                                                                                                                                                                                                                                                                        ).replace("quattour", "%"
                                                                                                                                                                                                                                                                                                                                                                                                                ).replace("quin", "^"
                                                                                                                                                                                                                                                                                                                                                                                                                                ).replace("sex", "&"
                                                                                                                                                                                                                                                                                                                                                                                                                                        ).replace("septen", "*"
                                                                                                                                                                                                                                                                                                                                                                                                                                                ).replace("octo", "("
                                                                                                                                                                                                                                                                                                                                                                                                                                                        ).replace("novem", ")"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                )

        randomlist = []
        for i in var12:
                try:
                    number += translate[i]
                except KeyError:
                     print("The string you entered has a non-numerical character in it. please try again.")
                     return
                randomlist.append(i)
        print(*randomlist)
        if randomlist[0] == "@" and randomlist[1] != "2":
                print("This is the",str(number)+ "st illion and it has", (number * 3) + 4, "digits!")
        elif randomlist[0] == "#" and randomlist[1] != "2":
                print("This is the",str(number)+ "nd illion and it has", (number * 3) + 4, "digits!")
        elif randomlist[0] == "$" and randomlist[1] != "2":
                print("This is the",str(number)+ "rd illion and it has", (number * 3) + 4, "digits!")
        else:
                print("This is the",str(number)+ "th illion and it has", (number * 3) + 4, "digits!")
        f = open("whichillionlogs.txt", "a+")
        f.write(str(number) + ", "+ str((number * 3) + 4) + "\n")
def choosing(x):
    if x < 100:
        option = input("Choose App: IllionFinder(i) or WhichIllion(w): ")
        if option.lower() == "i":
            florida()
        elif option.lower() == "w":
            california()
        novar1 = input("Again? (y / n): ")
        if novar1.lower() == "y":
            choosing(99)
        else:
            choosing(101)
choosing(99)