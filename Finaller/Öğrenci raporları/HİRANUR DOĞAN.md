# DENETİM RAPORU: dgnhira/mts_acilservissimilasyon

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, hastaların acil servise giriş anlarını Poisson dağılımına dayalı eksponansiyel rastgele zaman aralıklarıyla (getExponentialRandom fonksiyonu üzerinden) üretmektedir. Sisteme giren hastalar sırasıyla triaj kuyruğu, triaj aktif alanı, Manchester Triaj Sistemi (MTS) renk kodlaması, muayene bekleme odası, aktif hekim muayenesi ve olasılıksal olarak (%30 oranında) müşahade yatağı aşamalarından geçmektedir. Her hastanın geçiş zamanları, bekleme süreleri ve ihlal durumları dinamik olarak state.logs dizisinde doğrusal bir veri hattı oluşturacak şekilde biriktirilmekte ve sonuçlar anlık grafiklere (Chart.js) aktarılarak CSV çıktısına dönüştürülmektedir.

Kontrol Kaldıraçları: Kullanıcı; Saatlik Geliş Hızı (lambda), Triaj Hemşiresi sayısı, Aktif Hekim sayısı ve Müşahade Yatağı kapasitesini arayüzdeki slider bileşenleri üzerinden kontrol edebilmektedir. Bu kaldıraçlar sadece kozmetik birer gösterge olmayıp, kod içerisindeki kuyruk işleme döngülerini (processQueuesImmediately ve tick fonksiyonları) doğrudan etkilemektedir. Örneğin hekim sayısı azaltıldığında muayene kuyruğundaki yığılma matematiksel olarak artmakta, belirli süre sınırları aşıldığında ise hastaların sırayı terk etme (LWBS) mekanizması tetiklenmektedir.

Localhost Kontrolü: GEÇTİ - Canlı dağıtıma esas teşkil eden kaynak kodda hiçbir localhost, 127.0.0.1 veya yerel bilgisayara ait mutlak dosya yolu (C:/Users/... vb.) tespit edilmemiştir. Tüm kütüphaneler güvenli harici CDN ağları üzerinden yüklenmektedir.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Kesikli olay simülasyonu ilkelerine uygun olarak Kuyruk Teorisi, Poisson gelişleri ve eksponansiyel servis süreleri başarıyla modellenmiştir. Manchester Triaj Sistemi renk kodlarının (Kırmızı, Turuncu, Sarı, Yeşil, Mavi) tıbbi aciliyet ağırlıkları ve maksimum bekleme süreleri sisteme entegre edilmiştir. Özellikle Kırmızı alan hastalarının medikal önceliği nedeniyle düşük öncelikli hastaların muayenesini yarıda kesip (preemption) öne geçmesi gibi ileri düzey mekanik gerçekçilik unsurları eksiksiz uygulanmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüz kontrolleri simülasyonun çalışması esnasında dinamik girdi sağlamaktadır. Kullanıcının yaptığı kaynak planlaması değişiklikleri, sistemin anlık MTS uyumluluk oranını ve doluluk kapasitesini doğrusal/mantıksal bir algoritmayla değiştirmekte, gün sonu raporunda başlangıç kadrosu ile güncel kadro arasında anlamlı bir A/B senaryo analizi sunmaktadır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: exportCSV fonksiyonu, simülasyon sürecinde üretilen gerçek verileri yapılandırılmış bir CSV şemasına (Hasta_ID, Giriş_Sanal_Dakika, Manchester_Triaj_Rengi, Triaj_Bekleme_Süresi_DK, Muayene_Bekleme_Süresi_DK, Toplam_Acilde_Kalış_Süresi_DK, MTS_Hedef_Süre_Aşıldı_Mı) dönüştürmekte ve kullanıcı bilgisayarına indirilebilir formatta aktarmaktadır.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Üstlenilen Rol ve Konu Uygunluğu: Öğrenci, raporda "Kıdemli Sistem Analisti ve Yöneylem Uzmanı" rolünü başarılı ve derinlikli bir şekilde üstlenmiştir. Karar alıcı pozisyonundaki Hastane Yönetim Kurulu'na doğrudan hitap eden , sıradan bir akademik ödev veya makale havasından uzak, tamamen kurumsal bir iş teklifi ve "Stratejik Çözüm Ortaklığı" vizyonu sunulmuştur. Ele alınan acil servis yoğunluğu ve kapasite problemleri, hastanenin finansal sağlığı ve marka itibarı üzerinden kritik bir problem çözücü olarak işlenmiştir.

Anlatım ve Basitlik Düzeyi: Raporda "5 yaşındaki birine anlatır gibi" ilkesine büyük ölçüde sadık kalınmıştır. Ayrık Olay Simülasyonu (DES), ED Boarding ve LWBS gibi teknik ve ağır jargona sahip kavramlar; sektörü derinlemesine bilmeyen bir yöneticinin bile ilk okumada rahatça kavrayabileceği şekilde "atıl kapasite tuzağı", "gelir koruması" ve "maaş tasarrufu" gibi net ifadelerle basitleştirilmiştir. Durum A ve Durum B karşılaştırmasını sunan performans metriği tablosu, simülasyonun geleceğe yönelik operasyonel tahminlerini ve stratejik kazanımlarını somut sayılarla son derece anlaşılır kılmaktadır.

Yapay Zeka İzleri ve Özensizlik: Metnin genelinde yapay zekaya has basmakalıp dolgu paragrafları ve içi boş jenerik robotik geçiş ifadeleri başarıyla temizlenmiştir. Öğrenci yapay zeka çıktısının üzerinden kendi diliyle geçmiş; hastane bilançosu, personel tükenmişliği ve yatırım getirisi (ROI) çözümlemelerini ikna edici ve özgün bir kurumsal dille rapora entegre etmiştir.

E-Posta Dil ve Profesyonelliği: Değerlendirmeye esas teşkil eden dosya içeriğinde veya başvuru kapsamında; konu satırı, profesyonel hitap, emojisiz kurumsal gövde metni ve ad-soyad içeren resmi kapanış kurallarına sahip bağımsız bir e-posta iletişim taslağı sunulmamıştır. Profesyonel iletişim boyutu bu teslimatta eksik bırakılmıştır.

PUAN KIRILMA GEREKÇELERİ

- Rapor kalitesi, rol canlandırma derinliği ve anlatım sadeliği kusursuz seviyede olsa da, değerlendirme kriterlerinin önemli bir parçası olan profesyonel e-posta metni/öğrenci iletişimi taslağı sunulmadığı ve bu alan boş bırakıldığı için 5 puan kırılmıştır.
    

NİHAİ FİNAL NOTU: 75 XP