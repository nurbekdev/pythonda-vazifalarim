dostlar = ['ali' , 'vali' , 'umar' , 'anvar' , 'sarvar', 'hasan']
for dost in dostlar:
    print(f"Salom {dost.title()} ")

print(f"Dastur {len(dostlar)} marta takrorlandi")

sonlar = list(range(10,101,3))
for son in sonlar:
    print(f"{son} ning kubi {son**3} ga teng")

dostlar = []
print("5 ta eng sevimli kinolaringizni kiriting: ")
for n in range(5):
    dostlar.append(input(f"{n+1} - kinoning nomini kiriting: "))
print(dostlar)

dostlar = []
n = int(input("Nechta odam bilan suhbatlashdingiz: "))
dostlar.extend(input(f"{a+1} - odamning ismini kiriting: ") for a in range(n))
print(f"Sizning do'stlaringiz: {dostlar}")
  
