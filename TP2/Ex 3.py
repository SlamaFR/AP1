U_input = input("Saisir une unité d'entrée : ").upper()
T_input = float(input("Saisir une température : "))
T_kelvin = None

if U_input == "C":
    T_kelvin = T_input + 273.15
elif U_input == "F":
    T_kelvin = T_input + 454.67 / 1.8
elif U_input == "K":
    T_kelvin = T_input
else:
    print("Unité de sortie incorrecte !")

if T_kelvin is not None:
    if T_kelvin < 0:
        print("Cette température est impossible")
    else:
        U_output = input("Saisir une unité de sortie : ").upper()

        if U_output != "F" and U_output != "C" and U_output != "K":
            print("Unité de sortie incorrecte !")
        else:
            if U_output == "F":
                T_output = 1.8 * T_kelvin - 459.67
            elif U_output == "C":
                T_output = T_kelvin - 273.15
            else:
                T_output = T_kelvin

            print(T_input, "°" + U_input, "correspond à",
                  round(T_output, 2), "°" + U_output)
