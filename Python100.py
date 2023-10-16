# B1
# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200)
# Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

def baitap1(range1,range2,step=1):
    result = [x for x in range(range1,range2+1,step) if x%7==0 and x%5!=0]
    return result

# B2
# Viết một chương trình có thể tính giai thừa của một số cho trước
# Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
# Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

def giaithua(n=int(input("Chọn số tính giai thừa : ")),result=1):
    if (n-1)!=0:
        giaithua(n-1,result*n)
    elif (n-1)<0:
        print("Số không hợp lệ")
    else:
        return result

# Test
