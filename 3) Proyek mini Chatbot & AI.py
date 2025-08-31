def chatbot():
 print("=== 🤖 Mini Chatbot 10 Kata (Keyword) ===")"=== 🤖 Mini Chatbot 10 Kata (Keyword) ===")
 print("Ketik 'keluar' untuk keluar.\n")"Ketik 'keluar' untuk keluar.\n")

 sedangkan True:
 user_input = input("Kamu: ").lower()"Kamu: ").lower()

 if masuk_pengguna di ["keluar", "keluar", "berhenti"]:if masuk_pengguna di ["keluar", "keluar", "berhenti"]:
 print("Chatbot: Sampai jumpa, semoga harimu menyenangkan.")"Chatbot: Sampai jumpa, semoga harimu menyenangkan.")
 breakbreak

 # Respon berdasarkan keyword
 jika "halo" di user_input atau "hai" di user_input:"halo" di user_input atau "hai" di user_input:
 reply = "Halo juga, senang bertemu denganmu.""Halo juga, senang bertemu denganmu."
 elif "nama" di user_input:"nama" di user_input:
 reply = "Saya chatbot mini sepuluh kata saja.""Saya chatbot mini sepuluh kata saja."
 elif "cuaca" di user_input:"cuaca" di user_input:
 reply = "Cuaca hari ini cerah dan cukup menyenangkan.""Cuaca hari ini cerah dan cukup menyenangkan."
 elif "baik" di user_input:"baik" di user_input:
 balasan = "Syukurlah, semoga harimu penuh kebahagiaan.""Syukurlah, semoga harimu penuh kebahagiaan."
 elif "makan" in user_input:"makan" in user_input:
 reply = "Jangan lupa makan supaya tetap sehat selalu.""Jangan lupa makan supaya tetap sehat selalu."
 elif "ai" di user_input:"ai" di user_input:
 reply = "AI adalah kecerdasan buatan yang membantu manusia.""AI adalah kecerdasan buatan yang membantu manusia."
 else:else:
 reply = "Maaf, saya belum mengerti pertanyaanmu sekarang.""Maaf, saya belum mengerti pertanyaanmu sekarang."

 # Batasi 10 kata10 kata
 reply_limited = " ".join(reply.split()[:10])" ".join(reply.split()[:10])
 print(f"Chatbot: {reply_limited}")"Chatbot: {reply_limited}")

jika __nama__ == "__main__":"__main__":
 chatbot()
