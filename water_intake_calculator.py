print("veejoomise kalkulaator")

goal = 8
drank = int(input("Mitu klaasi vett oled juba joonud? "))

percent = (drank/goal) * 100


if percent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif percent <75:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")