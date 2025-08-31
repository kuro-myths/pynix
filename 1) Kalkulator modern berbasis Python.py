import math

def hitung(expr: str):
    """Evaluasi ekspresi matematika"""
    try:
        # Ganti simbol supaya bisa dipahami Python
 expr = expr.replace("×", "*").replace("÷", "/")
 expr = expr.replace("^", "**")       # pangkat
 expr = expr.replace("√", "matematika.sqrt")

        # Fungsi trigonometri (pakai derajat, bukan radian)
 expr = expr.replace("dosa", "math.sin(math.radians")
 expr = expr.replace("cos", "math.cos(math.radians")
 expr = expr.replace("tan", "math.tan(math.radians")

        # Tambahkan konstanta
 expr = expr.replace("π", "matematika.pi")
 expr = expr.replace("e", "matematika.e")

        # Evaluasi
 hasil = eval(expr)

        # Rapikan hasil float
        if isinstance(hasilnya, float) and hasil.adalah_integer():
 hasil = int(hasil)

        return hasil
 kecuali Pengecualian sebagai e:
        return kesalahan F"❌: {e}"


def utama():
    print("=== 🧮 Kalkulator CLI Modern ===")
    print("Fitur: + - × ÷ ^ √ sin cos tan π e")
    print("Contoh input:")
    print(" 5+10")
    print(" √(25)")
    print(" dosa(90)")
    print(" 2^3 + cos(60)")
    print("Ketik 'keluar' untuk keluar.\n")

    sementara True:
 expr = input(">>> ")

        if expr.lower() == "keluar":
            print("Keluar dari kalkulator...")
            break

 hasil = hitung(expr)
        print("= ", hasil, "\n")


if __nama__ == "__utama__":
    utama()
