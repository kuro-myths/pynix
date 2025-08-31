import math

def main():
    print("=== Kalkulator CLI Modern ===")
    print("Ketik 'exit' untuk keluar\n")

    while True:
        expr = input("Masukkan ekspresi matematika: ")

        if expr.lower() == "exit":
            print("Keluar dari kalkulator...")
            break

        try:
            # Ganti simbol × ÷ agar sesuai Python
            expr = expr.replace("×", "*").replace("÷", "/")

            # Tambahkan fungsi matematika
            expr = expr.replace("sin", "math.sin(math.radians")
            expr = expr.replace("cos", "math.cos(math.radians")
            expr = expr.replace("tan", "math.tan(math.radians")
            expr = expr.replace("√", "math.sqrt")

            result = eval(expr)

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            print("Hasil =", result, "\n")

        except Exception as e:
            print("❌ Error:", e, "\n")

if __name__ == "__main__":
    main()
