YOLOv8 Tabanlı Plastik Atık ve Kapak Tespit Sistemi
Tokat Gaziosmanpaşa Üniversitesi | Bilgisayar Programcılığı
Geliştirici: Merve Uzun

Proje Motivasyonu
Bu çalışma, çevresel sürdürülebilirlik ve akıllı geri dönüşüm sistemlerine katkı sağlamak amacıyla tasarlanmıştır. Görüntü işleme teknolojileri kullanılarak, evsel atıklar içerisinde sıklıkla bulunan plastik şişeler ve şişe kapaklarının otonom bir şekilde ayırt edilmesi ve sınıflandırılması hedeflenmiştir.

Veri Mühendisliği ve Roboflow Entegrasyonu
Sınıf Yapısı: Model; "Plastik Şişe" ve "Şişe Kapağı" olmak üzere iki farklı nesne sınıfını tanıyacak şekilde konfigüre edilmiştir.

Roboflow Pipeline: Veri seti yönetimi için Roboflow platformu tercih edilmiştir. Bu platform üzerinden görseller; farklı ışık şiddetleri, döndürme (rotation) ve bulanıklaştırma (blur) gibi Augmentation (Veri Artırma) tekniklerinden geçirilerek modelin zorlu koşullardaki dayanıklılığı artırılmıştır.

Etiketleme Stratejisi: Şişe ve kapak nesneleri, iç içe geçebilen yapılar oldukları için etiketleme aşamasında nesne sınırları (Bounding Boxes) birbirini ezmeyecek şekilde hassasiyetle tanımlanmıştır.

Algoritma ve Eğitim Mimarisi
Projenin temelini, gerçek zamanlı nesne tespiti konusunda endüstri standardı olan YOLOv8 mimarisi oluşturmaktadır.

Model: Hız-performans dengesi gözetilerek optimize edilen mimari üzerine, Roboflow'dan dışa aktarılan özel veri setiyle eğitim gerçekleştirilmiştir.

Transfer Learning: Önceden eğitilmiş ağırlıklar kullanılarak, modelin plastik dokusunu ve kapak formlarını öğrenme süreci hızlandırılmıştır.

Analitik Sonuçlar ve Performans
Doğruluk Oranı: Model, karmaşık arka planlar (çöp yığınları, karışık masalar vb.) üzerinde yapılan testlerde plastik şişe ve kapakları yüksek bir başarı yüzdesiyle tespit etmektedir.

Sınıf Ayrımı: Confusion Matrix sonuçlarına göre, modelin şişe gövdesi ile kapağını birbirine karıştırma oranı minimize edilmiş, her iki sınıf için de dengeli bir mAP (Mean Average Precision) skoru elde edilmiştir.

Fonksiyonel Çıktılar
Gerçek Zamanlı Tespit: Sistem, web kamerası veya video kayıtları üzerinden atıkları saniyeler içinde analiz edebilmektedir.

Ağırlık Yönetimi: Eğitimin en başarılı evresi olan best.pt dosyası, sistemin çıkarım (inference) motoru olarak sisteme entegre edilmiştir.

Proje Bileşenleri
Dataset/: Roboflow üzerinden normalize edilmiş eğitim, test ve doğrulama klasörleri.

data.yaml: Plastik şişe ve kapak sınıflarını tanımlayan konfigürasyon dosyası.

best.pt: Eğitim sonucunda elde edilen en yüksek başarımı temsil eden model dosyası.

Rapor.md: Projenin gelişim sürecini ve teknik detaylarını içeren dokümantasyon.
