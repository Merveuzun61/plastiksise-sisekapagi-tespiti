from ultralytics import YOLO

# Modeli yükle
model = YOLO('yolov8s.pt') 

# Eğitimi başlat
results = model.train(
    data='/content/merve_Uzun/data.yaml', 
    epochs=100,            
    imgsz=640,             
    batch=16,              
    patience=20,           
    name='merve_uzun_proje'
)