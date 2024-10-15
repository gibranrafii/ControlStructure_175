percentage = float(input ("Enter the student's percentage : "))

def penilaian(percentage):
    if percentage >= 90:
        return "Excelent Performance"
    elif percentage >= 80:
        return "Very Good Performance"
    elif percentage >= 70:
        return "Good Performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Need Improve"

print(penilaian(percentage))

#fungsi buat mencari 3 terttinggi
def largest(a, b, c):
    if a >= b and a >=c:
        return a
    elif b >=a and b >= c:
        return b
    else:
        return c
    
a = float(input("Masukkan nomor ke-1 : "))
b = float(input("Masukkan nomor ke-2 : "))
c = float(input("Masukkan nomor ke-3 : "))
print("Nomor terbesar adalah : ", largest(a,b,c))

#fungsi fibonacci
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series [-2])
    return fib_series[:n]

fibo = int(input("Masukkan Batas limit untuk fibonacci : "))
print("Fibonacci series : ", fibonacci(fibo))



def cetak_angka_ganjil(n):
    for i in range(1, n + 1):
        if i % 2 != 0:  # Memeriksa apakah angka ganjil
            print(i, end=' ')
    print()

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))    
cetak_angka_ganjil(n)

# Function to print pattern based on n
def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=' ')
        print()

# Example usage

n = int(input("Enter the value of n: "))
print_pattern(n)
 