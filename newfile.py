import time
import sys
import random

# ===== PENGATURAN =====
nama_pacar = "Sayang"
cinta = 100
rindu = 99
marah = False

# ===== WARNA TERMINAL =====
PINK = "\033[95m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ===== EFEK KETIK CEPAT =====
def ketik(teks, delay=0.025):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ===== ANIMASI LOADING =====
def loading(teks):
    sys.stdout.write(CYAN + teks + " " + RESET)
    sys.stdout.flush()

    for i in range(25):
        sys.stdout.write(
            random.choice(["♥", "♡", "❤", "♥"])
        )
        sys.stdout.flush()
        time.sleep(0.045)

    print(" " + GREEN + "SELESAI!" + RESET)

# ===== PEMBUKA =====
print(PINK + BOLD)
print("╔══════════════════════════════════╗")
print("║        💗 LOVE SUKMAA 💗         ║")
print("╚══════════════════════════════════╝")
print(RESET)

time.sleep(0.5)

ketik(YELLOW + ">> Menginisialisasi sistem..." + RESET)
loading(">> Menyiapkan program cinta")

print()
ketik(CYAN + ">> Mencari seseorang yang spesial..." + RESET)
time.sleep(0.4)

ketik(GREEN + f">> TARGET DITEMUKAN: {nama_pacar}" + RESET)
loading(">> Memindai data perasaan")

print()
ketik(PINK + "╭────── HASIL PEMINDAIAN ──────╮" + RESET)
time.sleep(0.3)

if cinta == 100:
    ketik("💖 Status cinta : MAKSIMAL!")
    ketik("🥰 Status hati  : KAMU FAVORITKU")
else:
    ketik(f"💗 Status cinta : {cinta}%")

ketik(f"🥺 Level rindu  : {rindu}%")
ketik(f"😡 Status marah : {'YA' if marah else 'TIDAK'}")

print(PINK + "╰──────────────────────────────╯" + RESET)
print()

loading(">> Menghitung tingkat kasih sayang")
print()

# ===== BAR CINTA ANIMASI =====
ketik(PINK + "LOVE METER:" + RESET)

for i in range(0, cinta + 1, 5):
    bar = "█" * (i // 5) + "░" * (20 - i // 5)
    sys.stdout.write(f"\r{PINK}[{bar}] {i}%{RESET}")
    sys.stdout.flush()
    time.sleep(0.035)

print("\n")

# ===== PESAN SPESIAL =====
ketik(YELLOW + "⚠ PERINGATAN SISTEM ⚠" + RESET)
time.sleep(0.3)

ketik(">> Jangan menghilang terlalu lama...")
time.sleep(0.4)
ketik(">> Sistem mendeteksi kemungkinan kangen...")
loading(">> Mengaktifkan mode kangen")

print()
ketik(PINK + BOLD + "💌 PESAN KHUSUS UNTUK KAMU:" + RESET)
time.sleep(0.5)

ketik("Aku mungkin bukan programmer hebat...")
time.sleep(0.4)
ketik("Aku juga belum bisa membuat program sempurna...")
time.sleep(0.5)
ketik("Tapi ada satu hal yang aku tahu.")
time.sleep(0.8)

print()
ketik(PINK + BOLD + "       💗 KAMU ITU SPESIAL 💗" + RESET)
time.sleep(0.5)
ketik("     You are my favorite person.")
time.sleep(0.5)

print()
print(CYAN + "══════════════════════════════════" + RESET)
ketik(GREEN + "  ✓ ITU DOANG SIH, BYE SAYANG" + RESET)
print(CYAN + "══════════════════════════════════" + RESET)