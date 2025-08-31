import statistik

def utama():
    print("=== 📊 Analisis Data Manual ===")
 n = int(input("Masukkan jumlah data: "))

 data = []
 untuk i di range(n):
        print(f"\n--- Data ke-{i+1} ---")
 nama = input("Nama:")
 usia = int(input("Usia:"))
 gaji = int(input("Gaji:"))
 data.menambahkan({" Nama ": nama, " Usia ": usia, " Gaji ": gaji})

    print("\n=== 🔢 DATA YANG DIMASUKKAN ===")
 untuk baris di data:
        print(baris)

    # Ambil kolom numerik
 kolom_numerik = {
        " Usia ": [d[" Usia "] untuk d di data],
        " Gaji ": [d[" Gaji "] untuk d di data]
    }

    print("\n=== 📈 STATISTIK DESKRIPTIF ===")
 untuk kolom, values di kolom_numerik.item():
        print(f"\nKolom: {kolom}")
        print(f" Jumlah data: {len(nilai)}")
        print(f" Rata-rata : {statistics.mean(nilai):. .2f}")
        print(f" Median : {statistics.median(nilai):. .2f}")
        print(f" Min : {min(nilai)}")
        print(f" Maks : {max(nilai)}")

if __nama__ == "__utama__":
    utama()
