---
gorev_13: 0
final_notu: 20
ogrenci_no: 2511317016
butunleme_notu: 80
---
# BÜTÜNLEME

## DENETİM RAPORU: yasar07488/-arj-Altyap-s-

### AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

- **Hile/Manipülasyon Riski:** DÜŞÜK
    
- **Sahte Veri/Manipülasyon Tespiti:** HAYIR
    
- **Hile Kanıtı:** Kod dürüstlüğü doğrulanmıştır.
    

### TEKNİK ANALİZ

- **Veri Akışı (Data Lineage):** Simülasyon verisi `nrel_dataset.js` içindeki saatlik geliş dağılımı, batarya kapasitesi olasılıkları ve başlangıç SoC aralıklarından beslenmektedir. `app.js` içinde kullanıcı tarafından belirlenen trafik oranı, fiyat katsayısı, port sayıları, trafo kapasitesi ve sıcaklık değerleriyle araç gelişleri, kuyruk, şarj süresi, enerji tüketimi, bekleme süresi, kayıp müşteri oranı ve maliyet/gelir çıktıları hesaplanmaktadır. Sonuçlar arayüzde grafik/metrik olarak gösterilmekte ve tamamlanan araç kayıtları CSV olarak dışa aktarılabilmektedir.
    
- **Kontrol Kaldıraçları:** Kullanıcı; maksimum trafik yoğunluğu, AC port sayısı, DC 50 kW port sayısı, DC 150 kW port sayısı, fiyatlandırma katsayısı, yoğunluk bazlı otomatik fiyatlandırma, trafo kapasitesi, aylık sıcaklıklar ve manuel/otomatik ay seçimini kontrol edebilmektedir. Bu kontroller kozmetik değildir: geliş oranını, kuyruk oluşumunu, sunucu kapasitesini, şarj gücünü, şebeke kısıtını, sıcaklığa bağlı verimliliği, gelir hesabını ve balking/kayıp müşteri davranışını doğrudan etkilemektedir. Ancak “NREL EVI-Pro entegrasyonu” ifadesi güçlü bir iddiadır; kodda gerçek bir dış NREL veri dosyası/API bağlantısı değil, temsili ve sabit dağılımlar kullanılmıştır.
    
- **Localhost ve Dağıtım Uygunluğu:** GEÇTİ - Kod tabanı statik HTML/CSS/JavaScript yapısındadır. `localhost`, `127.0.0.1`, yerel mutlak dosya yolu veya Python/Streamlit-Flask gibi GitHub Pages ile uyumsuz dinamik backend bağımlılığı tespit edilmemiştir.
    

### EŞİK DEĞERLENDİRMELERİ

- **Eşik 1 (Gerçekçilik ve Mantık):** GEÇTİ - _Gerekçe:_ Araç gelişleri stokastik fakat parametreli bir kuyruk/simülasyon mantığına bağlıdır. Geliş oranı, saatlik dağılım, fiyat katsayısı, port sayısı, trafo kapasitesi, sıcaklık ve batarya/SoC dağılımları çıktı üzerinde matematiksel etki yaratmaktadır. Rastgelelik yalnızca araç gelişi, batarya profili, SoC ve balking gibi simülasyon bağlamında makul stokastik olaylarda kullanılmaktadır; sırf grafik üretmek için kontrolsüz sahte gürültü üretimi tespit edilmemiştir.
    
- **Eşik 2 (Kontrol Edilebilirlik):** GEÇTİ - _Gerekçe:_ Kullanıcı kontrolleri şarj altyapısı planlaması açısından anlamlı kaldıraçlardır. Port sayıları kapasiteyi, trafik parametresi talebi, fiyat talep/kayıp müşteri davranışını, trafo kapasitesi güç kısıtını, sıcaklık ise şarj verimliliğini değiştirmektedir.
    
- **Eşik 3 (Veri Dışa Aktarımı):** GEÇTİ - _Gerekçe:_ `CSV İndir` işlevi, tamamlanan araçlar için `arrival_time`, `service_time`, `battery_capacity_kWh`, `soc_start`, `soc_end`, `waiting_time` alanlarını içeren yapılandırılmış CSV çıktısı üretmektedir.
    

---

**NİHAİ DURUM:** NOTLANDIRMAYA UYGUN  

## FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

### GENEL ANALİZ

- **Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik):** GEÇTİ. Rapor; 4 AC, 3 DC50, 2 DC150, 1.4x dinamik fiyat çarpanı ve 500 kW trafo sınırı gibi karar alıcının doğrudan uygulayabileceği somut kaldıraçlar sunmaktadır. Öneriler tautolojik değildir; metropol krizi gibi dışsal/etik dışı bir girdiyi politika önerisi gibi sunmamaktadır. Üç adımlı bürokratik eylem planı açık, gerçekçi ve yetki sınırları içindedir.
    
- **Çözümü Satabilme ve İkna Kabiliyeti:** Rapor karar alıcıya doğrudan hitap etmektedir. “Altyapı yatırımı, şebeke güvenliği ve finansal optimizasyon” çerçevesi iyi kurulmuş; pahalı trafo yatırımı yerine akıllı yönetim senaryosu önerilerek problem yönetsel ve mali açıdan satılabilir hale getirilmiştir.
    
- **Veri Temelli Kanıtlar ve Simülasyon Atıfları:** Raporda kendi simülasyon çıktısına açık atıf vardır. Senaryo A, B ve C karşılaştırılarak toplam araç, tamamlanan araç, kayıp müşteri oranı, ortalama bekleme, pik güç, toplam kWh ve ROI değerleri verilmiştir. Özellikle Senaryo C’nin %3.2 kayıp, 4.9 dakika bekleme, 440 kW pik güç ve 4.1 yıl ROI ile gerekçelendirilmesi güçlüdür.
    
- **Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği:** Yapay zeka dolgusu hissi düşük düzeydedir; metin karar alıcıya yönelik kurumsal bir teklif diliyle yazılmıştır. Öğrencinin adı-soyadı nettir, hitap ve kapanış yapısı uygundur, emoji veya laubali ifade tespit edilmemiştir.
    

### PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Kusursuz teslimat, puan kırılmamıştır.
    

---

**NİHAİ FİNAL NOTU:** 80 XP
