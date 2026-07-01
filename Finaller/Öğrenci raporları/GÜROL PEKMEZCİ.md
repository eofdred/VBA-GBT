---
gorev_13: 0
final_notu: 0
ogrenci_no: 2511317005
butunleme_notu: 0
---
# BÜTÜNLEME

## DENETİM RAPORU: GurolPekmezci/Havayolu-Sim

### AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

- **Hile/Manipülasyon Riski:** YOK
    
- **Sahte Veri/Manipülasyon Tespiti:** HAYIR
    
- **Hile Kanıtı:** Kod dürüstlüğü doğrulanmıştır.
    

### TEKNİK ANALİZ

- **Veri Akışı (Data Lineage):** Simülasyon; kod içinde tanımlı rota ve uçak veri setlerinden, Binance USD/TRY API çağrısından, Open-Meteo hava durumu çağrısından ve tarih tabanlı deterministik yakıt fiyatı simülasyonundan besleniyor. Çekirdek çıktı; rota, sezon, uçak kapasitesi, talep esnekliği, doluluk, kargo, ek gelir, yakıt, iniş ücreti ve operasyon maliyeti formülleriyle üretiliyor. `Math.random()` çekirdek finansal simülasyonda değil, sadece yağmur/kar görsel parçacıklarının ekrandaki konumu ve animasyon süresi için kullanılıyor. ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com"))
    
- **Kontrol Kaldıraçları:** Kullanıcı; uçuş rotası, sezon, uçak tipi ve yapay zeka fiyatlandırma/yield management seçimini kontrol edebiliyor. Bu kontroller kozmetik değil: rota mesafe, baz talep, baz fiyat, esneklik ve iniş ücretini; sezon talep ve fiyat çarpanını; uçak tipi kapasite, yakıt tüketimi, sabit maliyet ve kargo kapasitesini; yapay zeka fiyatlandırması ise fiyat aralığı taramasıyla yolcu talebi ve gelir optimizasyonunu değiştiriyor. ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/index.html "AeroSim Pro | Canlı Havacılık Yönetimi")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com"))
    
- **Localhost ve Dağıtım Uygunluğu:** GEÇTİ - Repo statik `index.html`, `script.js`, `style.css` dosyalarından oluşuyor; Python/Streamlit/Flask gibi GitHub Pages ile uyumsuz backend yapısı görünmüyor. `script.js` içinde `localhost`, `file://`, `Downloads`, `Masaüstü`, `Path.home` eşleşmesi bulunmadı. ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim "GitHub - GurolPekmezci/Havayolu-Sim · GitHub")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com"))
    

### EŞİK DEĞERLENDİRMELERİ

- **Eşik 1 (Gerçekçilik ve Mantık):** GEÇTİ - _Gerekçe:_ Kullanıcı girdileri ile çıktılar arasında açık matematiksel bağ var: talep esnekliği, sezon çarpanı, kapasite sınırı, yakıt/operasyon maliyeti, kargo ve ek gelir hesapları çıktı değerlerini belirliyor. Çekirdek sonuçlar kontrolsüz rastgele gürültüyle üretilmiyor.
    
- **Eşik 2 (Kontrol Edilebilirlik):** GEÇTİ - _Gerekçe:_ Rota, sezon, uçak tipi ve yield management anahtarı karar verici açısından anlamlı kaldıraçlar. Değişiklikler doluluk, gelir, maliyet, kargo ve kâr/zarar hesaplarına doğrudan etki ediyor.
    
- **Eşik 3 (Veri Dışa Aktarımı):** KALDI - _Gerekçe:_ Uygulamada “Veriyi PDF İndir” işlevi var ve `downloadPDF()`jsPDF ile rapor üretiyor; ancak CSV, JSON veya analiz için yeniden kullanılabilir yapılandırılmış veri dışa aktarımı bulunmuyor. Kodda `CSV`, `.csv`, `Blob`, `URL.createObjectURL` veya `application/json` tabanlı dışa aktarım eşleşmesi yok. PDF raporu, bu eşikte istenen analiz edilebilir veri formatı yerine raporlama dokümanıdır. ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/index.html "AeroSim Pro | Canlı Havacılık Yönetimi")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com")) ([GitHub](https://github.com/GurolPekmezci/Havayolu-Sim/raw/refs/heads/main/script.js "raw.githubusercontent.com"))
    

---

**NİHAİ DURUM:** REDDEDİLDİ (NOT: 0)  
