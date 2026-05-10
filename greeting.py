print("Tere tulemast meie veebilehele!")
print("Edasi liigumiseks läheks meil vaja teie perekonna nime ja sugu")

last_name = input("Sisestage oma perekonna nimi")
gender = input("Mis on teie sugu? (mees/naine):")

if gender == "mees":
    print(f"Tere, härra {last_name}!")
elif gender == "naine":
    print(f"Tere, proua {last_name}!")
else:
    print(f"Tere tulemast, {last_name}! (sugu ei olegi tähtis).")  
