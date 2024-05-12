#var = "trevigintitrucentidumillinioctomyrillion"
var = input("Enter Illion Pronunciation")
var = var.lower()
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
number = 0
var = var.replace("llion", ""
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
for i in var:
    number += translate[i]
    randomlist.append(i)
print(*randomlist)
if randomlist[0] == "@" and randomlist[1] != "2":
    print("This is the",str(number)+ "st illion")
elif randomlist[0] == "#" and randomlist[1] != "2":
    print("This is the",str(number)+ "nd illion")
elif randomlist[0] == "$" and randomlist[1] != "2":
    print("This is the",str(number)+ "rd illion")
else:
    print("This is the",str(number)+ "th illion")