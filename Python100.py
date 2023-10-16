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