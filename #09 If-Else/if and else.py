avtomabillar = ['toyotta' , 'mazda' , 'hyunda' , 'gm' , 'kia']
for avtomabil in avtomabillar:
    if avtomabil =='gm' :
        print(avtomabil.upper())
    else:
        print(avtomabil.title())

login = input("Ismingizni kiriting: aa")
if login == 'admin':
    print("Xushkelibsiz admin , foydalanuvchilar ruyxatini ko'rasizmi: ")
else:
    print(f"Xush kelibsiz {login.title()}")


son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
if son1 == son2:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")

son = int(input("Istalgan son kiriting: "))
if son >0:
    print(f"{son} son Musbat")
else:
    print(f"{son} son Manfiy")
    
son = int(input("Istalgan son kiriting: "))
if son >0:
    print(f"{son} ning ildizi {son**0.5}")
else:
    print("-100Manfiy sondan ildiz chiqmaydi")
    
    






