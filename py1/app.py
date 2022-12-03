
from math import *
"""character_name="mahmut"
is_male= True
print("name:"+character_name)
phrase="elma"
print(phrase.isupper())
print(phrase[0])
print(phrase.index("lm"))
print(phrase.replace("elma","muz"))
print(phrase)
print(3*2+5)
my_num=4
print(str(my_num)+"is my fav num")  #sayıyı stinge cevirdi mynum+"yazı" yaparsak direk hata verir#
print(pow(3,2))
print(round(4.4))
print(floor(4.7))
#isim=input("adını yaz")
#print("hello "+isim+"!")
num1=input("enter a number")
num2=input("enter another number")
result=float(num1)+float(num2)
print(result) """
"""color=input("enter a color")
noun=input("enter a noun ")
celebrity=input("enter a celeb")
print("roses are"+color)
print(noun+"are blue")
print(celebrity+"I LOVE U")"""
"""friends=["rach","joey","mon","chan","ross"]
friends[2]="mike"
print(friends[-1])
print(friends[1:3])#1 den 1 hariç 3 e kadar"""
"""nums=[1,2,4,7,6]
friends=["rach","joey","mon","chan","chan","ross"]
friends.extend(nums)
friends.append("yenikisi")
friends.insert(1,"kevin")#sectigin indexse yerlestirip dierlerini kaydırıyor
friends.remove("rach")
print(friends)
friends.pop()
print(friends)
print(friends.index("kevin"))
print(friends.count("chan"))
nums.reverse()
nums.sort()
print(nums)
friends2=friends.copy()
print(friends2)"""
""""#TUFLES tipi (listeye benziyor) tufles degistirilemezdir immiutable#
coordinates=(4,44)
print(coordinates[1]"""
#fonksiyonlar^#
"""def say_Hi(name,age):
    print("hi"+name+str(age))
#artık fonksiyon içinde değilim#
say_Hi("derya",22)
say_Hi("selena",13)"""
"""def cube(num):
    return num*num*num
print(cube(3))"""
#if statement
"""is_male=True
is_tall=False
if is_male and is_tall:
    print("you are tall male")
elif is_male and not(is_tall):
    print("you are a male but not tall")
elif not(is_male)and is_tall:
    print("you are a tall girl")
else:
    print("you are eighter male or tall")"""
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
result=max_num(3,6,5)
print(result)



