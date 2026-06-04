# DENETİM RAPORU: basbogaruveyda-afk / su-sim-lasyonu- (Rüveyda Başboğa)

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon verilerini TÜİK tabanlı resmi çevre ve nüfus göstergelerini içeren yerel CSV dosyalarından PapaParse kütüphanesi yardımıyla dinamik olarak çekmektedir. Tarayıcı tabanlı CORS veya ağ erişim kısıtlamaları ihtimaline karşı gömülü yerel veri setleri (fallback) başarılı bir şekilde entegre edilmiştir. Alınan ham veriler, kütle dengesi (mass balance) formülasyonu altında runScenario fonksiyonuyla işlenerek anlık olarak Chart.js grafiklerine, şeffaflık paneline ve detay analiz tablosuna aktarılmaktadır.

Kontrol Kaldıraçları: Kullanıcı; projeksiyon yılı, yıllık nüfus artış oranı, doğal kaynak verimlilik çarpanı, şebeke kayıp-kaçak oranı, kullanıcı tasarruf oranı ve başlangıç rezerv katsayısını arayüzdeki slider elemanları ile değiştirebilmektedir. Ayrıca şebeke rehabilitasyonu, akıllı tarımsal sulama, akıllı sayaç tarifesi ve kamu bilinçlendirme gibi aktif politikalar checkbox kontrolleri ile sisteme dahil edilmiştir. Bu girdiler modeldeki katsayıları doğrudan manipüle ederek çıktı sonuçlarını, risk seviyelerini ve tükenme yılı tahminlerini gerçekçi bir şekilde değiştirmektedir; kurgu tamamen dinamiktir ve kozmetik değildir.

Localhost Kontrolü: GEÇTİ - Proje kod tabanında canlı yayını olumsuz etkileyecek localhost, 127.0.0.1 veya kullanıcı bilgisayarına ait mutlak yerel dosya yolu referansları bulunmamaktadır. Tüm veri kaynakları bağıl (relative) yollarla yönetilmiştir.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Simülasyon, TÜİK resmi raporlarındaki baseline değerleri referans alan fiziksel diferansiyel kütle dengesi denklemleriyle kurgulanmıştır. Math.random() gibi kontrolsüz rastgele gürültü üreteçleri kullanılmamış, girdiler ile çıktılar arasında net matematiksel bağ kurulmuştur.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan kontrol elemanları ve politika senaryoları bir karar verici için eyleme geçirilebilir anlamlı kaldıraçları temsil etmektedir ve simülasyonun amacına doğrudan hizmet ederek sonuçları mantıksal bir doğrultuda etkilemektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Üretilen simülasyon verileri, Excel ve diğer analiz araçlarıyla tam uyumlu çalışacak şekilde Türkçe karakter senkronizasyonuna (BOM) sahip, noktalı virgül (;) ayırıcılı yapılandırılmış bir CSV formatında dışa aktarılabilmektedir (btnDownloadCSV tetikleyicisi aktiftir).

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Üstlenilen Rol ve Konu Uygunluğu: Rapor, "Su Kaynakları Planlama ve Analiz Uzmanı" rolünü kurumsal bir ciddiyetle benimsemiş ve doğrudan Belediye Başkanı'na hitap ederek bir karar alıcının ihtiyaç duyacağı stratejik bakış açısını başarıyla yansıtmıştır. Şehrimizin su rezervlerinin tükenme riskine karşı sunulan altyapı ve politika önerileri, sıradan bir akademik ödev olmanın ötesinde, tamamen eyleme geçirilebilir somut birer teklif niteliğindedir. Anlatım ve Basitlik Düzeyi: Simülasyonun arkasındaki karmaşık matematiksel kütle dengesi mantığı, "su bardağı, pipetle su içen çocuklar ve bardağın altındaki delik" analojisiyle 5 yaşındaki birinin bile anlayabileceği bir sadeliğe indirgenmiştir. Kendi simülasyonundan elde edilen kümülatif veriler ile yıllara sari spesifik nüfus ve m³ bazındaki rezerv çıktıları (Tablo 1 ve Tablo 2) rapora doğrudan entegre edilerek veri temelli kanıt sunma başarısı gösterilmiştir. Yapay Zeka İzleri ve Özensizlik: Yapay zekanın üretebileceği jenerik başlıklar veya basmakalıp dolgu paragrafları titizlikle temizlenmiştir. Metin, simülasyon senaryosunun özgün verileri ve hedefleri doğrultusunda tamamen kişiselleştirilmiş ve özgünleştirilmiştir. rapor Dil ve Profesyonelliği: Rapor resmi, kurumsal ve oldukça saygın bir üslupla kaleme alınmıştır. İçerisinde kuralları ihlal edecek hiçbir emojiye yer verilmemiştir. Uygun bir hitapla başlamış, kurumsal bir birim unvanı ve saygı ifadesiyle sonlandırılmıştır. Ancak, rol yapma derinliği korunurken teslimi yapan öğrencinin kendi ad ve soyad bilgisi imza alanında açıkça belirtilmemiştir.

PUAN KIRILMA GEREKÇELERİ

[Raporda resmi unvan ve birim kullanılarak profesyonel kapanış yapılmış olsa da, imza bölümünde öğrencinin kendi ad ve soyad bilgisini yazmamış olması nedeniyle tavan puandan -5 puan kırılmıştır.]

NİHAİ FİNAL NOTU: 75 XP