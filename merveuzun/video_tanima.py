import os
import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO

def main():
    # 1. Model Yükleme
    model_yolu = os.path.join(os.getcwd(), "best.pt")
    if not os.path.exists(model_yolu):
        print(f"HATA: {model_yolu} bulunamadı!")
        exit()

    print(f"Model yükleniyor: {model_yolu}...")
    model = YOLO(model_yolu)
    print("Model başarıyla yüklendi.\n")

   
    root = tk.Tk()
    root.withdraw()

    print("Lütfen analiz edilecek video dosyasını seçiniz...")
    girdi_video_yolu = filedialog.askopenfilename(
        title="Analiz Edilecek Videoyu Seçin",
        filetypes=[("Video Dosyaları", "*.mp4;*.avi;*.mov;*.mkv")]
    )

    if not girdi_video_yolu:
        print("İşlem iptal edildi. Video seçilmedi.")
        input("\nKapatmak için Enter tuşuna basın...")
        exit()

    
    orijinal_video_adi = os.path.splitext(os.path.basename(girdi_video_yolu))[0]

    # 3. Çıktı Klasörü Ayarı
    hedef_klasor = r"C:\Users\acer\OneDrive\Masaüstü\merve_Uzun"
    if not os.path.exists(hedef_klasor):
        os.makedirs(hedef_klasor, exist_ok=True)

    print(f"\n--- VIDEO ANALIZI BASLADI ---")
    print("YOLO orijinal video motoru çalışıyor. Süre ve hız kaybı yaşanmayacaktır.")
    print("Lütfen terminalde işlemlerin tamamlanmasını bekleyin...\n")

    # 4. YOLO'nun Kendi Güçlü Tahmin ve Kayıt Mekanizması
    # save=True ile videoyu orijinal hızında/süresinde otomatik kaydeder.
    model.predict(
        source=girdi_video_yolu,
        imgsz=640,
        conf=0.25,
        classes=[0, 1],  
        save=True,       # Videoyu doğrudan kaydetme talimatı
        project=hedef_klasor,  # Kaydedilecek ana klasör
        name=f"{orijinal_video_adi}_sonuc", # Oluşacak alt klasörün adı
        exist_ok=True    
    )

    print(f"\nİşlem başarıyla tamamlandı!")
    print(f"Sonuç videosu şu klasörün içine kaydedildi:\n--> {hedef_klasor}\\{orijinal_video_adi}_sonuc\\")
    input("\nKapatmak için Enter tuşuna basın...")

if __name__ == "__main__":
    main()