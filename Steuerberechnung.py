# Jahresgehalt eingabe

eingabe = float(input("Jahresgehalt eingeben: "))

if eingabe > 75000:

    print("Sie zahlen 30% Steuern")
    Steuer1 = round((eingabe * 0.30), 2)
    print("Steuern: ", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))

elif 48000 < eingabe < 75000:
    print("Sie zahlen 20% Steuer")
    Steuer1 = round((eingabe * 0.20), 2)
    print("Steuer: ", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))

elif 48000 > eingabe:
    print("Sie Zahlen 10% Steuern")
    Steuer1 = round((eingabe * 0.10), 2)
    print("Steuer; ", Steuer1)
    print("Neues Jahresgehalt: ", round((eingabe - Steuer1), 2))



