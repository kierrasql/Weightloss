#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#getting needed information

print("Please Enter Weight Lose Information:")

Firstname=input("Enter the name of the first member?")
Secondname=input("Enter the name of the second member?")

#entering in peoples lost weight

firstnameJanlose=print("How many pounds did", Firstname, "lose in January?")
answer_1j=int(input("answer"))
secondnamejanlose=print("How much many pounds did",Secondname, "lose in January?")
answer_2j=int(input("answer"))
firstnameFeblose=print("How much many pounds did", Firstname,"lose in February?")
answer_1f=int(input("answer"))
secondnameFeblose=print("How much many pounds did",Secondname,"lose in February?")
answer_2f=int(input("answer"))
firstnameMarlose=print( "How much many pounds did", Firstname, "lose in March?")
answer_1m=int(input("answer"))
secondnameMarlose=print("How much many pounds did", Secondname,"lose in March?")
answer_2m=int(input("answer"))
firstnameAprillose=print("How much many pounds did", Firstname, "lose in April?")
answer_1a=int(input("answer"))
secondnameAprillose=print("How much many pounds did", Secondname,"lose in April?")
answer_2a=int(input("answer"))
firstnameMaylose= print("How much many pounds did", Firstname, "lose in May?")
answer_1ma=int(input("answer"))
secondnameMaylose=print("How much many pounds did", Secondname, "lose in May?")
answer_2ma=int(input("answer"))


Firstnametotal= (answer_1j+ answer_1f+ answer_1m+ answer_1a+answer_1ma) 
Secondnametotal= (answer_2j+ answer_2f+ answer_2m+ answer_2a+ answer_2ma)


firstsum= (Firstnametotal)
secondsum=(Secondnametotal)

print()
print("Total Weight Loss Chart")
print("Jan","Feb","March","April","May")
print(Firstname,answer_1j, answer_1f, answer_1m, answer_1a,answer_1ma) 
print(Secondname,answer_2j,answer_2f,answer_2m, answer_2a, answer_2ma)


print(Firstname,"lost a Total Weight of:", firstsum)
print(Secondname,"lost a Total Weight of:", secondsum)


# ##### 
