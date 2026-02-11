import cv2
import numpy as np

MAVI = (255, 0, 0)
YESIL = (0, 255, 0)
KIRMIZI = (0, 0, 255)
BEYAZ = (255, 255, 255)
SIYAH = (0, 0, 0)
SARI = (0, 255, 255)
# Çizim Kalınlıkları
KALIN = 5
ORTA = 3
INCE = 1

dosya_adi = "blackswan.jpg"
img_ham = cv2.imread(dosya_adi)

print(f"Görüntü Verisi Yüklendi.")
print(f"Matris Boyutu: {img_ham.shape}")
#orjinal veriyi korumak için kopyayla çalışıyoruz.
img = img_ham.copy()
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Black Swan", (50, 50), font, 1, BEYAZ, 2)

print("\n--- KONTROLLER ---")
print("c: Daire (Circle) - Mavi")
print("r: Dikdörtgen (Rectangle) - Yeşil")
print("l: Çizgi (Line) - Beyaz")
print("x: Temizle (Reset) - Orijinale dön")
print("s: Kaydet (Save)")
print("q: Çıkış (Quit)")

# GÖRÜNTÜ İŞLEME DÖNGÜSÜ
while True:
    cv2.imshow("Veri Manipulasyon Ekrani", img)

    tus = cv2.waitKey(1) & 0xFF

    # Çıkış
    if tus == ord('q'):
        print("Program sonlandırıldı.")
        break

    elif tus == ord('c'):
        cv2.circle(img, (465, 130), 70, MAVI, ORTA)
        print("Veri Güncellendi: Mavi Daire Eklendi.")

    elif tus == ord('r'):
        cv2.rectangle(img, (800, 500), (100, 300), YESIL, ORTA)
        print("Veri Güncellendi: Yeşil Dikdörtgen Eklendi.")

    elif tus == ord('l'):
        cv2.line(img, (850, 200), (80, 180), SARI, KALIN)
        print("Veri Güncellendi: Kırmızı Çizgi Eklendi.")

    # Başlangıca dönme
    elif tus == ord('x'):
        # Orijinal kopyadan tekrar yükle (Reset)
        img = img_ham.copy()
        cv2.putText(img, "Ekran Temizlendi", (50, 50), font, 1, BEYAZ, 2)
        print("Matris Sıfırlandı (Reset).")

    # Görseli kaydetme
    elif tus == ord('s'):
        cv2.imwrite("charlie_islenmis.jpg", img)
        print("Sonuç diske kaydedildi.")

cv2.destroyAllWindows()