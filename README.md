# Yüz Tanıma ve Fotoğraf Çekme Uygulaması 📸

OpenCV ve Python kullanılarak geliştirilmiş gerçek zamanlı yüz tanıma ve otomatik fotoğraf çekme uygulaması. Bu uygulama web kameranız aracılığıyla yüzleri otomatik olarak algılar ve özelleştirilebilir ayarlarla fotoğraf çeker.

## 🚀 Özellikler

- **Gerçek Zamanlı Yüz Tanıma**: OpenCV'nin Haar Cascade sınıflandırıcısı ile doğru yüz algılama
- **Otomatik Fotoğraf Çekme**: Yüz algılandığında otomatik olarak fotoğraf çeker
- **Özelleştirilebilir Arayüz**: UI elemanları ve yüz algılama kutularının görünüm ayarları
- **Akıllı Bekleme Sistemi**: Yapılandırılabilir bekleme süreleri ile spam fotoğraf çekimini önler
- **İstatistik Gösterimi**: Gerçek zamanlı FPS, yüz sayısı ve fotoğraf sayısı istatistikleri
- **Esnek Kaydetme Seçenekleri**: Kaydedilen fotoğraflara hangi elemanların dahil edileceğini seçin
- **Kolay Yapılandırma**: Tüm uygulama ayarları için etkileşimli kurulum

## 🛠️ Kurulum

### Gereksinimler

- Python 3.7 veya üzeri
- Çalışan bir web kamera

### Kurulum Adımları

1. **Depoyu klonlayın**
   ```bash
   git clone https://github.com/yusufozbilek/FaceDetector.git
   cd FaceDetector
   ```

2. **Gerekli bağımlılıkları yükleyin**
   ```bash
   pip install -r requirements.txt
   ```

3. **Uygulamayı çalıştırın**
   ```bash
   python main.py
   ```

## 📋 Bağımlılıklar

- `opencv-python>=4.5.4.60` - Yüz tanıma ve görüntü işleme için bilgisayar görüşü kütüphanesi
- `numpy>=1.21.0` - Sayısal hesaplama kütüphanesi (OpenCV bağımlılığı)

## 🎯 Kullanım

### Temel Kullanım

Yüz tanıma uygulamasını başlatmak için ana scripti çalıştırın:

```bash
python main.py
```

### Yapılandırma Seçenekleri

Uygulamayı başlattığınızda, çeşitli ayarları yapılandırmanız istenecek:

1. **UI Gösterimi**: Canlı kamera görüntüsünde UI elemanlarının gösterilip gösterilmeyeceği
2. **UI Kaydetme**: UI elemanlarının kaydedilen fotoğraflara dahil edilip edilmeyeceği
3. **Yüz Kutularını Gösterme**: Canlı görüntüde mavi yüz algılama kutularını açma/kapatma
4. **Yüz Kutularını Kaydetme**: Algılama kutularının fotoğraflara dahil edilip edilmeyeceği
5. **Bekleme Süresi**: Ardışık fotoğraflar arasındaki bekleme süresi (saniye cinsinden)

### Kontroller

- **`q`**: Uygulamayı kapatır
- Uygulama yapılandırıldıktan sonra otomatik olarak çalışır

## 🏗️ Proje Yapısı

```
FaceDetector/
├── face_detector.py    # Ana FaceDetector sınıfı ve tüm işlevsellik
├── main.py            # Giriş noktası ve uygulama çalıştırıcısı
├── requirements.txt   # Python bağımlılıkları
├── photos/            # Kaydedilen fotoğraflar için dizin (otomatik oluşturulur)
└── README.md         # Bu dosya
```

## 🔧 Yapılandırma Detayları

### FaceDetector Sınıfı Parametreleri

- **`camera_index`** (int, varsayılan: 0): Kamera cihaz indeksi
- **`photo_delay`** (int, varsayılan: 5): Yüz algılandıktan sonra fotoğraf çekmeden önce beklenecek saniye
- **`output_dir`** (str, varsayılan: 'photos'): Çekilen fotoğrafların kaydedileceği dizin

### Çalışma Zamanı Ayarları

#### UI Ayarları
- **UI Açık/Kapalı**: Tüm UI elemanlarının (geri sayım, istatistikler, bekleme) görünümünü kontrol eder
- **UI Kaydetme**: UI elemanlarının kaydedilen fotoğraflara dahil edilip edilmeyeceğini belirler
- **Kutuları Gösterme**: Canlı görüntüde yüz algılama dikdörtgenlerini açar/kapatır
- **Kutuları Kaydetme**: Algılama dikdörtgenlerini kaydedilen fotoğraflara dahil eder

#### Zamanlama Ayarları
- **Fotoğraf Gecikmesi**: Yüz algılama ile fotoğraf çekimi arasındaki süre (varsayılan: 5 saniye)
- **Bekleme Süresi**: Ardışık fotoğraflar arasındaki minimum süre (yapılandırılabilir, varsayılan: 10 saniye)

## 📊 Özellik Detayları

### Yüz Tanıma
- OpenCV'nin önceden eğitilmiş Haar Cascade sınıflandırıcısını kullanır
- Aynı anda birden fazla yüzü algılar
- Algılanan yüzlerin etrafına mavi dikdörtgenler çizer
- Oturum sırasında algılanan toplam yüz sayısını sayar

### Otomatik Fotoğraf Çekimi
- Yüzler algılandığında tetiklenir
- Fotoğraf çekmeden önce görsel geri sayım
- Bekleme sistemi ile yinelenen fotoğrafları önler
- Fotoğrafları zaman damgası dosya adlarıyla kaydeder

### İstatistik Gösterimi
- **FPS**: Saniye başına fotoğraf oranı
- **Yüz Sayısı**: Oturumda algılanan toplam yüz sayısı
- **Fotoğraf Sayısı**: Çekilen toplam fotoğraf sayısı
- **Bekleme Zamanlayıcısı**: Kalan bekleme süresini gösterir

### Akıllı UI Sistemi
- Görüntüleme ve kaydetme için ayrı kontroller
- UI elemanlarının esnek kombinasyonu
- Yeniden başlatma gerektirmeyen gerçek zamanlı yapılandırma

## 🎨 Özelleştirme

### Algılama Parametrelerini Değiştirme

`detect_faces` metodundaki parametreleri değiştirerek yüz algılama hassasiyetini ayarlayabilirsiniz:

```python
faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
```

- İlk parametre (1.3): Ölçek faktörü - her ölçekte görüntü boyutunun ne kadar azaltılacağı
- İkinci parametre (5): Minimum komşu - her aday dikdörtgenin korunması için kaç komşuya sahip olması gerektiği

### Fotoğraf Ayarlarını Değiştirme

`main.py` dosyasındaki varsayılan ayarları değiştirin:

```python
detector = FaceDetector(
    camera_index=0,        # Birden fazla kameranız varsa kamerayı değiştirin
    photo_delay=3,         # Daha hızlı fotoğraflar için gecikmeyi azaltın
    output_dir='benim_fotograflarim' # Özel çıktı dizini
)
```

### UI Özelleştirme

`process_frame` metodunda renkler ve fontlar değiştirilebilir:

```python
# Geri sayım metni (yeşil)
cv2.putText(frame_with_ui, f"Fotograf: {countdown}s", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Yüz algılama kutuları (mavi)
cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
```

## 🔍 Sorun Giderme

### Yaygın Sorunlar

1. **Kamera algılanmıyor**
   - Kameranızın diğer uygulamalarla çalışıp çalışmadığını kontrol edin
   - Farklı `camera_index` değerlerini deneyin (0, 1, 2, vb.)
   - Başka uygulamaların kamerayı kullanmadığından emin olun

2. **Yüz tanıma çalışmıyor**
   - İyi aydınlatma koşulları sağlayın
   - Yüz açıkça görünür ve öne dönük olmalı
   - Hassasiyet için algılama parametrelerini ayarlamayı deneyin

3. **Fotoğraflar kaydedilmiyor**
   - Çıktı dizininde yazma izinlerini kontrol edin
   - Yeterli disk alanı olduğundan emin olun
   - Photos dizininin var olduğunu doğrulayın

4. **Performans sorunları**
   - Kamerayı kullanan diğer uygulamaları kapatın
   - Daha hızlı işleme için fotoğraf gecikmesini azaltın
   - Sistem kaynaklarını (CPU/Bellek) kontrol edin

### Hata Mesajları

- **"Kamera bulunamadı"**: camera_index parametresini değiştirin
- **"Dizine erişilemiyor"**: Dosya izinlerini kontrol edin
- **"Geçersiz giriş"**: Yapılandırma girişleri için doğru formatı kullanın

## 🤝 Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Lütfen bir Pull Request göndermekten çekinmeyin. Büyük değişiklikler için, önce ne değiştirmek istediğinizi tartışmak üzere bir issue açın.

### Geliştirme Kurulumu

1. Depoyu fork edin
2. Bir özellik dalı oluşturun (`git checkout -b feature/HarikaBirOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Harika bir özellik ekle'`)
4. Dala push yapın (`git push origin feature/HarikaBirOzellik`)
5. Bir Pull Request açın


