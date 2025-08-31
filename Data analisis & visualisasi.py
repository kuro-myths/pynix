import statistics

def main():
    print("=== 📊 Analisis Data Manual ===")
    n = int(input("Masukkan jumlah data: "))

    data = []
    for i in range(n):
        print(f"\n--- Data ke-{i+1} ---")
        nama = input("Nama: ")
        usia = int(input("Usia: "))
        gaji = int(input("Gaji: "))
        data.append({"Nama": nama, "Usia": usia, "Gaji": gaji})

    print("\n=== 🔢 DATA YANG DIMASUKKAN ===")
    for row in data:
        print(row)

    # Ambil kolom numerik
    kolom_numerik = {
        "Usia": [d["Usia"] for d in data],
        "Gaji": [d["Gaji"] for d in data]
    }

    print("\n=== 📈 STATISTIK DESKRIPTIF ===")
    for kolom, values in kolom_numerik.items():
        print(f"\nKolom: {kolom}")
        print(f"  Jumlah data: {len(values)}")
        print(f"  Rata-rata : {statistics.mean(values):.2f}")
        print(f"  Median    : {statistics.median(values):.2f}")
        print(f"  Min       : {min(values)}")
        print(f"  Max       : {max(values)}")

if __name__ == "__main__":
    main()
