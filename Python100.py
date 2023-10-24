# B1
# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200)
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

def baitap1(range1,range2,step=1):
    result = [x for x in range(range1,range2+1,step) if x%7==0 and x%5!=0]
    return result

# Lời giải
# j=[]
# for i in range(2000, 3201):
#   if (i%7==0) and (i%5!=0):
#   j.append(str(i))
# print (','.join(j))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B2
# Viết một chương trình có thể tính giai thừa của một số cho trước
# Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

def baitap2(n,result=1):
    # n=int(input("Chọn số tính giai thừa : "))
    if (n-1)!=0:
        baitap2(n-1,result*n)
    elif (n-1)<0:
        print("Số không hợp lệ")
    else:
        return result

# Lời giải
# x=int(input("Nhập số cần tính giai thừa:"))
# def fact(x):
#     if x == 0:
#     return 1
#     return x * fact(x - 1)
# print (fact(x))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B3
# Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này
# Ví dụ:Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.

def baitap3(soNguyenNBaiTap3):
    return {z:z*z for z in range(soNguyenNBaiTap3+1)}

# Lời giải
# n=int(input("Nhập vào một số:"))
# d=dict()
# for i in range(1,n+1):
#   d[i]=i*i
# print (d)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B4
# Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
# Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

def baitap4(baiTap4Nhap):
    # baiTap4Nhap = input("Nhập 1 chuối phân tách bằng dấy , : "))
    print(baiTap4Nhap.split(","))
    print(tuple(baiTap4Nhap.split(",")))

# Lời giải
# values=input("Nhập vào các giá trị:")
# l=values.split(",")
# t=tuple(l)
# print (l)
# print (t)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B5
# Định nghĩa một class có ít nhất 2 method:
# getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển
# printString: in chuỗi vừa nhập sang chữ hoa.
# Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.
# Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM

class baitap5:
    def __init__(self) -> None:
        self.chuoi = ''
    def getString(self):
        self.chuoi = str(input("Nhập chuỗi : "))
    def printString(self):
        print(self.chuoi.upper())
    
# Lời giải
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#     def getString(self):
#         self.s = input("Nhập chuỗi:")
# # Code by Quantrimang.com
#     def printString(self):
#         print (self.s.upper())
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B6
# Viết một method tính giá trị bình phương của một số.

def baitap6(baiTap6):
    return baiTap6**2

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B7
# Python có nhiều hàm được tích hợp sẵn, nếu không biết cách sử dụng nó, bạn có thể đọc tài liệu trực tuyến hoặc tìm vài cuốn sách
# Nhưng Python cũng có sẵn tài liệu
# về hàm cho mọi hàm tích hợp trong Python. Yêu cầu của bài tập này là viết một chương trình để in tài liệu về một số hàm Python được tích hợp sẵn như abs(), int(),
# input() và thêm tài liệu cho hàm bạn tự định nghĩa.

def baitap7():
    '''
    Đây sẽ là doc của chương trình <------ __doc__
    '''
    return


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B8
# Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
# Gợi ý:
#   Khi định nghĩa tham số instance, cần thêm nó vào __init__
#   Bạn có thể khởi tạo một đối tượng với tham số bắt đầu hoặc thiết lập giá trị sau đó

class baitap8:
    lopBaiTap8 = "test"
    # đây là lớp của class > baitap8.lopBaiTap8 = test
    def __init__(self,baiTap8):
        self.baiTap8 = baiTap8
        # đây là instance và 

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B9
# Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]. Với giá trị cố định của C là
# 50, H là 30. D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.
# Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.

import math as m
def baitap9(D,C=50,H=30):
    # D = str(input("Nhập D : "))
    return ",".join([str(round(m.sqrt((2*C*float(d))/H))) for d in D.split(",")])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B10
# Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. 
# Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j. 
# Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1. 
# Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

def baitap10(X,Y):
    return [[y*x for y in range(Y)] for x in range(X)]

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B11
# Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy. 
# Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.

def baitap11(baiTap11Value):
    # baiTap11Value=str(input("Nhập chuỗi : "))
    result = baiTap11Value.split(",")
    result.sort()
    return ",".join(result)


# Lời giải
# items=[x for x in input("Nhập một chuỗi: ").split(',')] 
# items.sort() 
# print(','.join(items))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B12
# Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này thành chữ in hoa và in ra màn hình. 
# Giả sử đầu vào là: 
# Hello world 
# Practice makes perfect 
# Thì đầu ra sẽ là: 
# HELLO WORLD 
# PRACTICE MAKES PERFECT

def baitap12():
    lines = [] 
    while True: 
        s = input() 
        # s luôn true khi có input được nhập vào > nhập được nhiều dòng , mỗi dòng đó sẽ ăn vào lines
        # Khi bấm tiếp enter , không có chuỗi được nhập > False , thoát khỏi while loop
        if s: 
            lines.append(s.upper()) 
        else: 
            break
    [print(line.upper()) for line in lines]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B13
# Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng, loại bỏ các từ trùng lặp, sắp xếp theo thứ tự bảng chữ cái, rồi in chúng. 
# Giả sử đầu vào là: hello world and practice makes perfect and hello world again 
# Thì đầu ra là: again and hello makes perfect practice world

def baitap13():
    line = str(input("Nhập chuỗi trắng :")).split(" ")
    return " ".join(sorted(set(line)))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B14
# Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. 
# Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy. 
# Ví dụ đầu vào là: 0100,0011,1010,1001 Đầu ra sẽ là: 1010

def baitap14(baiTap14):
    return  ",".join([x for x in baiTap14.split(",") if int(x,2)%5==0])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B15
# Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho tất cả các chữ số trong số đó là số chẵn. 
# In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.

def baitap15(min,max):
    return ",".join([str(x) for x in range(min,max+1) if len([y for y in str(x) if int(y) in [0,2,4,6,8]])==4])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B16
# Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. 
# Giả sử đầu vào sau được cấp cho chương trình: hello world! 123 
# Thì đầu ra sẽ là: Số chữ cái là: 10 Số chữ số là: 3

def baitap16(input):
    return f'''
Số chữ cái là : {len([x for x in [*input] if x.isalpha()])}
Số chữ số là : {len([x for x in [*input] if x.isnumeric()])}'''


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B17
# Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.
# Giả sử đầu vào là: Quản Trị Mạng
# Thì đầu ra là:
# Chữ hoa: 3
# Chữ thường: 8

def baitap17(input):
    return f'''
Số chữ Hoa là : {len([x for x in [*input] if x.isalpha() and x.isupper()])}
Số chữ Thường là : {len([x for x in [*input] if x.isalpha() and x.islower()])}'''


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B18
# Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi 
# người dùng.
# Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234

def baitap18(input):
    return "".join([str(int(input)*x) for x in range(1,5)])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B19
# Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.
# Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9

def baitap19(input):
    return ",".join([str(x) for x in input.split(",") if int(x)%2])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B20
# Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký
# giao dịch được nhập vào từ giao diện điều khiển.
# Định dạng nhật ký được hiển thị như sau:
# D 100
# W 200
# (D là tiền gửi, W là tiền rút ra).
# Giả sử đầu vào được cung cấp là:
# D 300
# D 300
# W 200
# D 100
# Thì đầu ra sẽ là:
# 500

def baitap20():
    history = []
    while True:
        duLieu =  input() 
        if duLieu:
            history.append(duLieu)
        else:
            break
    return sum([int(x.split(" ")[1]) if x.split(" ")[0] == "D" else 0-int(x.split(" ")[1]) for x in history])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B21
# Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký. 
# Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào. 
# Các tiêu chí kiểm tra mật khẩu bao gồm:

# 1. Ít nhất 1 chữ cái nằm trong [a-z] 
# 2. Ít nhất 1 số nằm trong [0-9] 
# 3. Ít nhất 1 kí tự nằm trong [A-Z] 
# 4. Ít nhất 1 ký tự nằm trong [$ # @] 
# 5. Độ dài mật khẩu tối thiểu: 6 
# 6. Độ dài mật khẩu tối đa: 12 

# Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy và kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không. 
# Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy. 
# Ví dụ mật khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345 Thì đầu ra sẽ là: ABd1234@1
import re
def baitap21(passwords):
    return ",".join([password for password in passwords.split(",") 
                     if 
                        re.findall(pattern=r"[a-z]",string=password) and 
                        re.findall(pattern=r"[A-Z]",string=password) and 
                        re.findall(pattern=r"[0-9]",string=password) and 
                        re.findall(pattern=r"[$#@]",string=password) and
                        not re.findall(pattern=r"[\s]",string=password) and
                        6<= len(password) <=12
                        ])

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B22
# Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name là string, age và height là number. 
# Tuple được nhập vào bởi người dùng. 
# Tiêu chí sắp xếp là:
# Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. Ưu tiên là
# tên > tuổi > điểm.
# Nếu đầu vào là:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Thì đầu ra sẽ là:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19',
# '80')]

def baitap22():
    result = []
    while True:
        profile = input("")
        if profile:
            result.append(tuple(profile.split(",")))
        else:
            break
    return sorted(result,key=lambda x: x[0] and x[1] and x[2]) 


# Lời giải
# from operator import itemgetter, attrgetter
# Bài tập Python 22 Code by Quantrimang.com
# l = []
# while True:
# s = input()
# if not s:
#   break
# l.append(tuple(s.split(",")))
# print (sorted(l, key=itemgetter(0,1,2)))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B23
# Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7.

def baitap23(n):
    for x in range(n+1):
        if not x%7:
            yield x


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B24
# Một Robot di chuyển trong mặt phẳng bắt đầu từ điểm đầu tiên (0,0). 
# Robot có thể di chuyển theo hướng UP, DOWN, LEFT và RIGHT với những bước nhất định. Dấu di chuyển của robot được đánh hiển thị như sau:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 3
# Các con số sau phía sau hướng di chuyển chính là số bước đi. 
# Hãy viết chương trình để tính toán khoảng cách từ vị trí hiện tại đến vị trí đầu tiên, sau khi robot đã di chuyển một quãng đường. 
# Nếu khoảng cách là một số thập phân chỉ cần in só nguyên gần nhất.
# Ví dụ: Nếu tuple sau đây là input của chương trình:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# thì đầu ra sẽ là 2

def baitap24():
    vault = []
    while True:
        step = input()
        if not step:
            break
        vault.append(step.split(" "))
    x = sum([int(data[1]) if data[0] == "UP" else -int(data[1]) for data in vault if data[0] in ["UP","DOWN"]])
    y = sum([int(data[1]) if data[0] == "RIGHT" else -int(data[1]) for data in vault if data[0] in ["LEFT","RIGHT"]])
    return int(round(m.sqrt(x**2+y**2)))
    # Pytago

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B25
# Viết chương trình tính tần suất các từ từ input. 
# Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái.
# Giả sử input là: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Thì output phải là:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

def baitap25(inputVal):
    return "\n".join(sorted([f"{x}:{inputVal.split(' ').count(x)}" for x in set(inputVal.split(" "))]))

# Lời giải
# freq = {} # frequency of words in text
# line = input()
# for word in line.split():
#   freq[word] = freq.get(word,0)+1
# # Bài tập Python 25 Code by Quantrimang.com
# words = sorted(freq.keys())
# for w in words:
#   print ("%s:%d" % (w,freq[w]))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B26
# Định nghĩa 1 hàm có thể tính tổng hai số.

def baitap26(num1,num2):
    return num1+num2


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B27
# Định nghĩa một hàm có thể chuyển số nguyên thành chuỗi và in nó ra giao diện điều khiển

def baitap27(num):
    print(str(num))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B28
# Định nghĩa hàm có thể nhận hai số nguyên trong dạng chuỗi và tính tổng của chúng, sau đó in tổng ra giao diện điều khiển.

def baitap28(num1,num2):
    print(int(num1)+int(num2))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B29
# Định nghĩa hàm có thể nhận 2 chuỗi từ input và nối chúng sau đó in ra giao diện điều khiển

def baitap29(string1,string2):
    print(string1+string2)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B30
# Định nghĩa một hàm có input là 2 chuỗi và in chuỗi có độ dài lớn hơn trong giao diện điều khiển. Nếu 2 chuỗi có chiều dài như nhau thì in tất cả các chuỗi theo dòng.

def baitap30(str1,str2):
    print(str1 if len(str1)>len(str2) else str2 if len(str2)>len(str1) else f'{str1}\n{str2}')


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B31
# Định nghĩa hàm có thể chấp nhận input là số nguyên và in "Đây là một số chẵn" nếu nó chẵn và in "Đây là một số lẻ" nếu là số lẻ

def baitap31(inputs):
    print("Đây là một số chẵn" if not inputs%2 else "Đây là một số lẻ")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B32
# Định nghĩa một hàm có thể in dictionary chứa key là các số từ 1 đến 3 (bao gồm cả hai số) và các giá trị bình phương của chúng.

def baitap32():
    print({f'{x}':x**2 for x in range(1,4)})


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B33
# Định nghĩa một hàm có thể in dictionary chứa các key là số từ 1 đến 20 (bao gồm cả 1 và 20) và các giá trị bình phương của chúng.

def baitap33():
    print({f'{x}':x**2 for x in range(1,21)})


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B34
# Định nghĩa một hàm có thể tạo dictionary, chứa các key là số từ 1 đến 20 (bao gồm cả 1 và 20) và các giá trị bình phương của chúng. Hàm chỉ in các giá trị mà thôi.

def baitap34():
    print(*{f'{x}':x**2 for x in range(1,21)}.values())


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B35
# Định nghĩa một hàm có thể tạo ra một dictionary chứa key là những số từ 1 đến 20 (bao gồm cả 1 và 20) và các giá trị bình phương của key. Hàm chỉ cần in các key.


def baitap35():
    print(*{f'{x}':x**2 for x in range(1,21)}.keys())


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B36
# Định nghĩa một hàm có thể tạo và in list chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20).

def baitap36():
    print([x**2 for x in range(1,21)])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B37
# Định nghĩa một hàm có thể tạo list chứa các giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20) và in 5 mục đầu tiên trong list.

def baitap37():
    print([x**2 for x in range(1,21)][:5])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B38
# Định nghĩa một hàm có thể tạo ra list chứa các giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20), rồi in 5 mục cuối cùng trong list.

def baitap38():
    print([x**2 for x in range(1,21)][-5:])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B39
# Định nghĩa một hàm có thể tạo list chứa giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20). Sau đó in tất cả các giá trị của list, trừ 5 mục đầu tiên.

def baitap39():
    print([x**2 for x in range(1,21)][5:])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B40
# Định nghĩa 1 hàm có thể tạo và in một tuple chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20).

def baitap40():
    print(tuple(x**2 for x in range(1,21)))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B41
# Với tuple (1,2,3,4,5,6,7,8,9,10) cho trước, viết một chương trình in một nửa số giá trị đầu tiên trong 1 dòng và 1 nửa số giá trị cuối trong 1 dòng.

def baitap41(tup=(1,2,3,4,5,6,7,8,9,10)):
    print(tup[:int(round(len(tup)/2))],end="\n")
    print(tup[int(round(len(tup)/2)):])

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B42
# Viết một chương trình để tạo tuple khác, chứa các giá trị là số chẵn trong tuple (1,2,3,4,5,6,7,8,9,10) cho trước

def baitap42(input):
    return (x for x in input if not x%2)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B43
# Viết một chương trình để tạo ra và in tuple chứa các số chẵn được lấy từ tuple (1,2,3,4,5,6,7,8,9,10).

def baitap42(input):
    return tuple(x for x in input if not x%2)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B44
# Viết một chương trình Python nhận chuỗi nhập vào bởi người dùng, in "Yes" nếu chuỗi là "yes" hoặc "YES" hoặc "Yes", nếu không in "No".

def baitap44():
    while True:
        a = input("")
        if a in ["YES",'yes','Yes']:
            print("Yes")
        else:
            print("No")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B45
# Viết chương trình Python có thể lọc các số chẵn trong danh sách sử dụng hàm filter.
# Danh sách là [1,2,3,4,5,6,7,8,9,10].

def baitap45(input):
    return list(filter(lambda x: not x%2,input))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B46
# Viết chương trình Python dùng map() để tạo list chứa các giá trị bình phương của các số trong [1,2,3,4,5,6,7,8,9,10].

def baitap46(input):
    return list(map(lambda x: x**2,input))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B47
# Viết chương trình Python dùng map() và filter() để tạo list chứa giá trị bình phương của các số chẵn trong [1,2,3,4,5,6,7,8,9,10].

def baitap47(input):
    return list(filter(lambda y: not y%2,map(lambda x: x**2,input))) or list(map(lambda y: y**2,map(lambda x: not x&2,input)))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B48
# Viết chương trình Python dùng filter() để tạo danh sách chứa các số chẵn trong đoạn [1,20].

def baitap48(input):
    return list(filter(lambda y: not y%2,range(1,21)))



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B49
# Viết chương trình Python sử dụng map() để tạo list chứa giá trị bình phương của các số trong đoạn [1,20].

def baitap49():
    return list(map(lambda y: y**2,range(1,21)))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B50
# Định nghĩa một class có tên là Vietnam, với static method là printNationality. ( Static method là method gọi trực tiếp từ class mà không cần instance)

# class Vietnam:
#     # Static attribute
#     bro = 345
#     def __init__(self) -> None:
#         self.bro = 123
#     @staticmethod 
#     def printNationality(): # không cần Self trong agrs
#         print(Vietnam.bro)
#     # Vietnam.printNationality() > 345
#     # a = Vietnam().bro
#     # print(a) > 123


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B51
# Định nghĩa một class tên Vietnam và class con của nó là Hanoi.

# class Vietnam:
#     # Static attribute
#     bro = 345
#     def __init__(self) -> None:
#         self.bro = 123
#     @staticmethod 
#     def printNationality(): # không cần Self trong agrs
#         print(Vietnam.bro)
#     # Vietnam.printNationality() > 345

# class Hanoi(Vietnam):
#     def __init__(self) -> None:
#         super().__init__()
#         # Nạp đạn từ class mẹ 
#     @staticmethod
#     def printNationality():
#         print(Hanoi.bro) 
#     # ghi đè lên static method cũ


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B52
# Định nghĩa một class có tên là Circle có thể được xây dựng từ bán kính. Circle có một method có thể tính diện tích.

# class Circle():
#     def __init__(self,banKinh) -> None:
#         self.__r = banKinh
#     def radius(self):
#         return m.pi * self._r**2
    

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B53
# Định nghĩa class có tên là Hinhchunhat được xây dựng bằng chiều dài và chiều rộng. 
# Class Hinhchunhat có method để tính diện tích.

# class Hinhchunhat:
#     def __init__(self,dai,rong) -> None:
#         self.dai=dai
#         self.rong = rong
#     def tinhdientich(self):
#         return self.dai*self.rong 


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B54
# Định nghĩa một class có tên là Shape và class con là Square. 
# Square có hàm init để lấy đối số là chiều dài. 
# Cả 2 class đều có hàm area để in diện tích của hình, diện tích mặc định của Shape là 0.

# class Shape:
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self,chieudaicanh):
#         super().__init__()
#         self.chieudaicanh = chieudaicanh
#     def area(self):
#         return self.chieudaicanh**2


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B55
# Đưa ra một RuntimeError exception.

def baitap55():
    try:
        raise RuntimeError(False,"args1")
    except RuntimeError as e:
        pass
        # print(e.args[0] or e.args[1]) > args1

# Lời giải
# class RuntimeError(Exception):
#     def __init__(self, mismatch):
#         Exception.__init__(self, mismatch)
# try:
#     print ("And now, the Vocational Guidance Counsellor Sketch.")
#     raise RuntimeError("Does not have proper hat")
#     print ("This print statement will not be reached.")
# except RuntimeError as problem:
#     print ("Vocation problem: {0}".format(problem))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B56
# Viết hàm để tính 5/0 và sử dụng try/exception để bắt lỗi.

def baitap56():
    try:
        a = 5/0
    except Exception as e:
        print(e)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B57
# Định nghĩa một class exception tùy chỉnh, nhận một thông báo là thuộc tính.

# class MyError(Exception):
#     def __init__(self, message: str):
#         super().__init__(message)
#     # a =  Exception("123") = MemoryError("123") > print(a) > 123


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B58 + B59
# Giả sử rằng chúng ta có vài địa chỉ email dạng username@companyname.com.
# Hãy viết một chương trình để in username của địa chỉ email cụ thể. 
# Cả username và companyname chỉ bao gồm chữ cái.

# B59
# Tương tự như bài 58, nhưng lần này ta sẽ viết hàm để lấy companyname

def baitap5859(*inputs):
    return [
        print(f'username:{z.split("@")[0]},companyname:{z.split("@")[1].split(".")[0]}') 
        for z in [y for y in inputs] if "@" in z and list(z).count("@") == 1
    ]


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B60
# Viết một chương trình chấp nhận chuỗi từ được phân tách bằng khoảng trống và in các từ chỉ gồm chữ số.
# Ví du: Nếu những từ sau đây là đầu vào của chương trình: 3 quantrimang.com và 2 python. Đầu ra sẽ là ['3', '2']
import re
def baitap60(input):
    # return [z for z in input if re.match(r'\d',z)] cách 1
    return re.findall(r'\d',input) #cách 2


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B61
# In chuỗi Unicode "Hello world"

def baitap61():
    print(u'Hello world')


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B62
# Viết chương trình để đọc chuỗi ASCII và chuyển đổi nó sang một chuỗi Unicode được mã hóa bằng UTF-8.

def baitap62(input):
    print(input.encode(encoding="utf-8"))


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B63
# Viết comment đặc biệt để chỉ định file code nguồn Python ở Unicode.
# ??


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B64
# Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1) với một n là số được nhập
# vào (n> 0).
# Ví dụ, nếu n là số sau đây được nhập vào:
# 5
# Thì đầu ra phải là:
# 3.55

def baitap64(n):
    return round(sum([x/(x+1) for x in range(1,n+1)]),2)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B65
# Viết chương trình tính: f(n)=f(n-1)+100 khi n>0 và f(0)=0, với n là số được nhập vào (n>0).
# Ví dụ: Nếu n được nhập vào là 5 thì đầu ra phải là 500

def baitap65(n: int):
    if int(n) !=0:
        return baitap65(int(n)-1) + 100
    else:
        return 0


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# B66
# Dãy Fibonacci được tính dựa trên công thức sau:
# f(n)=0 nếu n=0
# f(n)=1 nếu n=1
# f(n)=f(n-1)+f(n-2) nếu n>1
# Hãy viết chương trình tính giá trị của f(n) với n là số được người dùng nhập vào. 
# Ví dụ: Nếu n được nhập vào là 7 thì đầu ra của chương trình sẽ là 13.

def baitap66(n:int):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return baitap66(n-1) + baitap66(n-2)

