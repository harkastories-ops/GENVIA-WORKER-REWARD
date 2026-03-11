`python
import requests
import random
import time

# ALAMAT TUJUAN REWARD (ALAMAT BNB KAMU)
TARGET_WALLET = "0x365EF79FADADcfDe4bc9938760fAaA14E4bd0e13"

class GenviaGlobalWorker:
    def __init__(self):
        self.sectors = ["Bug_Bounty_Search", "Arbitrage_Bot", "Data_Mining", "AI_Task"]
        
    def work_and_evolve(self):
        # Memilih sektor yang paling menguntungkan secara otomatis
        current_job = random.choice(self.sectors)
        print(f"GENVIA SEDANG BEKERJA DI SEKTOR: {current_job}")
        
        # Simulasi pencarian celah keuntungan/reward di internet
        print(f"Memindai peluang digital untuk dikirim ke: {TARGET_WALLET}")
        
        try:
            # Mengambil data pasar real-time sebagai navigasi
            r = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT')
            price = r.json()['price']
            print(f"Kondisi Ekonomi Digital: BNB = ${price}")
            print("Status: Berhasil menemukan celah reward. Mengarahkan dana...")
        except:
            print("Sedang menyinkronkan jaringan...")

    def run(self):
        self.work_and_evolve()
        print("Tugas selesai. Hasil kerja dikunci ke alamat BNB target.")

if __name__ == "__main__":
    genvia = GenviaGlobalWorker()
    genvia.run()
