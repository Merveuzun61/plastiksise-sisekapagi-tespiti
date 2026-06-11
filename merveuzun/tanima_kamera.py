import cv2
from ultralytics import YOLO
import os
from datetime import datetime

def main():
    # 1. Modelin tam yolu
    model_yolu = os.path.join(os.getcwd(), "best.pt")
    
    if not os.path.exists(model_yolu):
        print(f"HATA: {model_yolu} dosyası bulunamadı!")
        exit()

    print(f"Model yükleniyor: {model_yolu}...")
    model = YOLO(model_yolu)
    print("Model başarıyla yüklendi.\n")

    # Hedef klasör (Kayıtlar buraya gidecek)
    hedef_klasor = r"C:\Users\acer\OneDrive\Masaüstü\merve_Uzun"
    if not os.path.exists(hedef_klasor):
        os.makedirs(hedef_klasor, exist_ok=True)

    # 2. Kamera Başlatma
    cap = cv2.VideoCapture(0)
    
    print("--- SADECE SISE VE KAPAK MODU AKTIF ---")
    print("Seni veya baska nesneleri tanimayacaktir.")
    print("'s' -> Kaydet | 'q' -> Cikis")

    while True:
        success, frame = cap.read()
        if not success:
            break

        # 3. Tahmin ve Filtreleme
        # classes=[0, 1] diyerek sadece plastik_sise ve sise_kapagi'ni aliyoruz.
        results = model.predict(
            source=frame, 
            imgsz=640, 
            conf=0.50,     
            iou=0.45, 
            verbose=False, 
            classes=[0, 1]  
        )
        
        # 4. Çizim
        resim_sonuc = results[0].plot(line_width=2, labels=True)

        # 5. Ekran Gösterimi
        cv2.imshow("YOLOv8 Filtrelenmis Tespit", resim_sonuc)

        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('s'):
            zaman = datetime.now().strftime("%H%M%S")
            yol = os.path.join(hedef_klasor, f"tespit_{zaman}.jpg")
            cv2.imwrite(yol, resim_sonuc)
            print(f"Kaydedildi: {yol}")

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()