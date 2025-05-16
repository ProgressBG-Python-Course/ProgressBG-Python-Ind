# user_name = "Byron"
# print(user_name)

# user_name = 5
# print(user_name)

# --------------------------- Numbers are immuteble -------------------------- #
# x = 5
# print(id(x))
# print(x)
# x = 10
# print(x)
# print(id(x))

# # RAM:
# # 0x123: 5
# # 0x145=>x: 10


# price=float(input("Enter price: "))# 4.5621
# price_rounded = round(price, 2)

# print(price, price_rounded)


# ------------------------------ Math functions ------------------------------ #
# import math
# print(math.factorial(5))


# >>> +42
# print(+42)
# print(.44)

# --------------------------------- Examples --------------------------------- #
# print(1+2)
# print("1"+"2")
# print(5*20)
# print("*"*20)


# ------------------------------ Strings methods ----------------------------- #
# user_first_name = input("Enter first name: ")
# user_last_name = input("Enter last name: ")

# user_first_name = user_first_name.capitalize()
# user_last_name = user_last_name.capitalize()


# print(user_first_name, user_last_name) # Iva Popova


# print("iva".capitalize())

# ----------------------- Formatted Strings (f-strings) ---------------------- #
# user_first_name = "iva"
# user_last_name = "popova"

# # user_full_name = user_first_name + " " + user_last_name
# user_full_name = f"{user_first_name} {user_last_name}"

# print(user_full_name)


# user_name = input("Enter name: ")
# print("Hello, " + user_name)
# print(f"Hello, {user_name}")

# x = 5
# y = 10

# print( f"x+y={x+y}" )

# x = 2.123456
# print(f"{x:.4}")

# x = 1.23456
# y = 1.23
# print(f"{x:>30}")
# print(f"{y:>30}")


# How many are the values ot int data type?
# 1, 2,3,4 .... infinity

# print(type(2))
# print(type(True))
# print(type(False))

# print( bool(5) )
# if 5:
#     print("Hello")

# user_name = input("Enter name:")
# print( bool(user_name) )
# if user_name:
#     print(f"Hello, {user_name}!")
# else:
#     print(f"Hello, Anonymous!")

# --------------------------- Comparison Operators --------------------------- #
# print( 5>3 )
# print( 5==3 )
# print( 5!=3 )


# x = 5
# y = 5
# if x!=y:
#     print("Hello!")

# print( 19>3 )      #True
# print( "19">"3" )  #
# print( "1">"3")

# print( "ab">"@!" )  #
# print( "a">"@" )  #

# print( "ab">"a!")
# print( "b">"!")

# print( True )

# user_age = 23
# user_language = "EN"

# if user_age>=18 and user_language=="BG":
#     print("Здравей")


# print( 2+3 )
# print(True and False) #
# print(False and True) #
# print( 2>4 and 345784385<76473264) #F
# print( False and 0) #


# 6>4 and print("Hello")

# print( True or False )
# print( 2>5 or True )

# print( False or False)

# print( not True) # False
# print( not 2>5)  # ?


# user_age = 18
# if not user_age>18:
#     print("Hello")

# print( 0 and 5 )
# print( 4-4 and True)#0

# print( 1 or 0) # 1
# print( True or False)


# ----------------------------- Modulus Operators ---------------------------- #
# print( 5%2 )
# print( 6%2 )
# print( 7%2 )
# print( 8%3 )

# print( 8%2 == 0)
# print( 7%2 == 0)


# ------------------------------- Control Flow ------------------------------- #
# number = 42

# print( number%2==0 ) #?
# print( number%2 ) #?


# If a number is even then print Even

# number = int(input("Enter a number:"))
# if number%2==0:
#     print("Even")


# user_age = 23
# user_language = "EN"

# if user_age>=18 and user_language=="BG":
#     print("Здравей")
#     print("!!!")
#     print("!!!")
#     print("!!!")
#     print("!!!")
#     print("!!!")

# x = 0
# if x == 0:
#     print("Zero")
# else:
#     if x%2==0:
#         print("Even")
#     else:
#         print("Odd")

x = 6
if x == 0:
    print("Zero")
elif x%2==0:
    print("Even")
else:
    print("Odd")


print("END")

