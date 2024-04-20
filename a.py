#bài 1 
# a = int(input("nhập số: "))
# if a % 2 == 0:
#     print("số chẵn")
# else:
#     print("số lẻ")

#bài 2
# a = float(input("nhập số: "))
# b = int(a)
# if a == b:
#    print("số nguyên")
# else:
#    print("ko phải số nguyên")
#bài 3



#bài 4
# a = int(input("nhập: "))
# if a % 3 == 0 and a % 5 == 0:
#     print(a,"chia hết cho 3 và 5")
# elif a % 3 == 0 and not a % 5 == 0:
#     print(a,"chia hết cho 3 nhưng ko chia hết cho 5")
# elif a % 5 == 0 and not a % 3 == 0:
#     print(a,"chia hết cho 5 nhưng ko chia hết cho 3")
# elif not a % 3 == 0 and not a % 5 == 0:
#     print(a,"ko chia hết cho 3 và 5")

#bài 5
# Username = "admin"
# Password = 12345
# a = input("nhập Username: ")
# b = int(input("nhập Password: "))
# if a == Username and b == Password:
#     print("đăng nhập thành công")
# else:
#     print("đăng nhập thất bại")

#bài 6
# a = input("cạnh 1: ")
# b = input("cạnh 2: ")
# c = input("cạnh 3: ")
# if a + b > c and a + c > b and b + c > a :
#     print("hình tam giác")
# else:
#     print("ko phải hình tam giác")

#bài 7
# a = int(input("cạnh 1: "))
# b = int(input("cạnh 2: "))
# c = int(input("cạnh 3: "))
# if a + b > c and a + c > b and b + c > a :
#     print("hình tam giác")
#     if c == (a**1/2)**2 + b**2 or b == (a**1/2)**2 + c**2 or a == (c**1/2)**2 + b**2  :
#         print("tam giác vuông")
#     elif a == b == c:
#         print("tam giác đều")
#         from turtle import*
#         forward(a)
#         left(120)
#         forward(a)
#         left(120)
#         forward(a)
#         left(120)
#         mainloop()
#     else:
#         print("tam giác bình thường")
# else:
#     print("ko phải hình tam giác")
#bài 8 
# for i in range(0,21):
#    if i % 3 ==0:
#     print(i)

#bài 9
# a = str(input("nhap: " ))
# print(len(a))