# DENETİM RAPORU: ece-naz/hava_yolu

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Kullanıcı arayüzündeki kaydırıcılar (slider) ve kitle seçim filtreleri, simülasyon çıktısını matematiksel bir formül üzerinden doğrudan ve anlamlı bir şekilde etkilemektedir. Sırf grafik çizdirmek için üretilmiş kontrolsüz veya ilgisiz bir rastgelelik bulunmamaktadır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, Kaggle'daki havayolu yolcu memnuniyeti veri setinin yapısına uygun olarak 1000 kişilik yapay bir popülasyon üretmektedir. Her yolcu için sınıf, sadakat, seyahat amacı gibi demografik özellikler ve temel hizmet puanları (Wi-Fi, koltuk, yemek, temizlik, rötar vb.) atanır. Bu veriler `calculateScore` fonksiyonunda ağırlıklandırılarak işlenir ve sonuçlar anlık olarak grafiklere, canlı yolcu haritasına (HTML Canvas) ve 50 satırlık ön izleme tablosuna aktarılır.

Kontrol Kaldıraçları: Kullanıcı Wi-Fi, koltuk konforu, ikram kalitesi, uçak içi eğlence, çevrimiçi rezervasyon, kabin temizliği ve rötar süresi gibi operasyonel faktörleri değiştirebilmektedir. Ayrıca yolcu kitlesi profili filtrelerle (uçuş sınıfı, sadakat durumu, seyahat amacı) yeniden üretilebilmektedir. Bu kaldıraçlar, yolcuların anlık durumunu (Memnun, Nötr, Memnuniyetsiz) belirleyen formülü dinamik olarak etkilemekte ve harita üzerindeki parçacıkların hedef konumlarını gerçek zamanlı değiştirmektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Proje tamamen statik web teknolojileri (HTML5, CSS3, istemci taraflı JavaScript) ile geliştirilmiştir. Kod içinde harici veya yerel bir sunucu bağımlılığı (localhost) ya da mutlak dosya yolu bulunmamaktadır. Yapı GitHub Pages üzerinde sorunsuz çalışmaya uygundur.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Yolcuların memnuniyet durumları, demografik puan bonusları ve rötar cezalarını da içeren mantıklı, ağırlıklı bir puanlama formülüne (`calculateScore`) dayanmaktadır. Sistem mekanik olarak tutarlıdır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan tüm kontrol elemanları simülasyonun amacına doğrudan hizmet eden, çıktıları ve grafiksel dağılımları anlık ve dinamik olarak güncelleyen anlamlı eyleme geçirilebilir kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Kod tabanında `downloadCsv` fonksiyonu eksiksiz yapılandırılmıştır. Üretilen 1000 kişilik popülasyonun güncel ve başlangıç verileri CSV formatında yapılandırılmış bir şekilde dışa aktarılabilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Üstlenilen Rol ve Konu Uygunluğu: Öğrenci, "Veri Bilimi ve Havacılık Analitiği Proje Lideri" rolüne eksiksiz bir şekilde bürünmüştür. Havayolu şirketlerinin yönetim kuruluna ve üst düzey yöneticilerine hitap eden, havayolu yolcu memnuniyeti odaklı stratejik bir yatırım raporu sunmuştur. Konu seçimi, müşteri deneyimi yönetimi (CXM) ve kurumsal kaynakların optimizasyonu gibi bir yönetici için tamamen problem çözücü, finansal dönüşü yüksek ve eyleme geçirilebilir somut teklifler içermektedir. Anlatım ve Basitlik Düzeyi: Rapor, karmaşık veri bilimi ve simülasyon süreçlerini kurumsal karar alıcıların saniyeler içinde yorumlayabileceği makro göstergelere indirgeyerek son derece sade ve anlaşılır bir dille aktarmıştır. Raporda yer alan 50 satırlık ham veri seti tablosu, "Nötr" yolcu segmentinin risk analizi ve arayüzdeki grafiklerin (Doughnut, Radar, Bar Chart) kurumsal yönetim kuruluna ne ifade ettiği çok net, basitleştirilmiş ve başarılı bir şekilde açıklanmıştır. Yapay Zeka İzleri ve Özensizlik: Metin genelinde yapay zekanın ürettiği basmakalıp, dolgu ve tekrara düşen jenerik ifadelere veya temizlenmemiş robotik konu başlıklarına rastlanmamıştır. Öğrenci, AI çıktısını kendi süzgecinden geçirmiş, havacılık analitiği terminolojisiyle harmanlayarak özgün ve akıcı bir kurumsal dil inşa etmiştir. Rapor Dil ve Profesyonelliği: Rapor kurumsal profesyonelliğe tamamen uygundur. "Yönetici Özeti ve Stratejik Problem Tanımı" ile net bir amaca odaklanarak başlamış, yönetim kurulu düzeyinde ciddiyete sahip kurumsal bir hitap ve sunum üslubu sürdürmüş, metnin hiçbir yerinde emojiye yer vermemiştir. Rapor, "Saygılarımla" ifadesiyle kurallara uygun, saygın bir kapanış yapmış ve öğrencinin tam adı-soyadı ile unvanı açıkça belirtilmiştir.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

Kusursuz teslimat, puan kırılmamıştır.

- Çözümü satabilme, ikna kabiliyeti ve karar alıcıya yaklaşım mükemmel seviyededir.
    
- "Nötr" yolcu segmenti (PAX-1003, PAX-1008, PAX-1031) ve rötar sürelerinin yıkıcı etkisi (PAX-1016) üzerinden kendi simülasyonundaki verilere, tablolara ve formül mantığına doğrudan spesifik atıflar yapılmıştır.
    
- Rapor format kurallarına (başlık, hitap, emoji yasağı, ad-soyad ve unvan içeren kapanış) tam uyum sağlanmıştır.
    

NİHAİ FİNAL NOTU: 80 XP