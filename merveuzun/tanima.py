import cv2
import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
import os

def main():
    # Modelin tam yolu. 'best.pt' python dosyanla aynı klasörde.
    model_yolu = os.path.join(os.getcwd(), "best.pt")
    
    # Tam yol oluşturmayı garanti altına alalım
    if not os.path.exists(model_yolu):
        print(f"HATA: {model_yolu} dosyası bulunamadı!")
        print(f"Mevcut çalışma klasörü: {os.getcwd()}")
        input("\nKapatmak için Enter tuşuna basın...")
        exit()

    print(f"Model yükleniyor: {model_yolu}...")
    model = YOLO(model_yolu)
    print("Model başarıyla yüklendi.\n")
    
    # 2. Dosya Seçimi
    root = tk.Tk()
    root.withdraw()
    
    print("Lütfen analiz edilecek görseli seçiniz...")
    # Sadece resim dosyalarını göstermek için filtre
    foto_yolu = filedialog.askopenfilename(
        title="Görsel Seçiniz",
        filetypes=[("Resim Dosyaları", "*.jpg;*.jpeg;*.png;*.webp")]
    )
    
    if not foto_yolu:
        print("İşlem iptal edildi.")
        input("\nKapatmak için Enter tuşuna basın...")
        exit()
        
    # 3. Tahmin Yapma
    results = model.predict(source=foto_yolu, imgsz=640, conf=0.15, iou=0.45)
    
    # 4. Çizim Ayarları
    resim_sonuc = results[0].plot(line_width=2, labels=True)
    
    # --- YENİ BÖLÜM: Sonucu merve_Uzun Klasörüne Kaydetme ---
    # Orijinal dosyanın adını ve uzantısını alıyoruz
    tam_dosya_adi = os.path.basename(foto_yolu)
    dosya_adi, uzanti = os.path.splitext(tam_dosya_adi)
    
    # Hedef klasör yolunu buraya sabitledik
    hedef_klasor = r"C:\Users\acer\OneDrive\masaüstü/merve_Uzun/"
    
    # Klasör yoksa oluştur (güvenlik için)
    os.makedirs(hedef_klasor, exist_ok=True)
    
    # Kaydedilecek dosya adını oluşturuyoruz (Örn: resim_sonuc.jpg)
    yeni_dosya_adi = f"{dosya_adi}_sonuc{uzanti}"
    kaydedilecek_yol = os.path.join(hedef_klasor, yeni_dosya_adi)
    
    # Resmi doğrudan bu klasöre kaydediyoruz
    print(f"Görsel kaydediliyor: {kaydedilecek_yol}...")
    cv2.imwrite(kaydedilecek_yol, resim_sonuc)
    # --------------------------------------------------------
    
    # 5. Pencere Boyutu ve Konum Ayarı
    pencere_adi = f"YOLOv8 - Sonuc: {tam_dosya_adi}"
    
    cv2.namedWindow(pencere_adi, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(pencere_adi, 550, 550)
    # Pencereyi ekranın ortasına yakın bir yere konumlandıralım
    cv2.moveWindow(pencere_adi, 400, 200)
    
    cv2.imshow(pencere_adi, resim_sonuc)
    
    print(f"\nİşlem tamamlandı. Sonuç görseli başarıyla şuraya kaydedildi:\n--> {kaydedilecek_yol}")
    print("\nResmi kapatmak ve programdan çıkmak için klavyeden herhangi bir tuşa basınız.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()