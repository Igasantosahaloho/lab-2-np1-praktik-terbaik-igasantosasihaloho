  import math

def luas_segitiga(a, b, c):
    s = (a + b + c) / 2
    luas = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return luas

def main():
    try:
        a = float(input("Masukkan panjang sisi pertama: "))
        b = float(input("Masukkan panjang sisi kedua: "))
        c = float(input("Masukkan panjang sisi ketiga: "))

        if a <= 0 or b <= 0 or c <= 0:
            print("Masukkan bilangan yang valid (bilangan positif) untuk panjang sisi segitiga.")
        elif a + b <= c or a + c <= b or b + c <= a:
            print("Tiga panjang sisi tidak membentuk segitiga yang valid.")
        else:
            luas = luas_segitiga(a, b, c)
            print("Luas segitiga dengan panjang sisi {}, {}, dan {} adalah {:.2f}".format(a, b, c, luas))
    except ValueError:
        print("Masukkan bilangan yang valid.")

if __name__ == "__main__":
    main()