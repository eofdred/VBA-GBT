# DENETİM RAPORU: tarim-su-simulasyonu / Ayşe Aydın

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon verileri, bölgedeki 100 adet tarımsal arazi için indeks tabanlı deterministik formüllerle (alan hesaplaması için mod fonksiyonu, toprak verimlilik çarpanı için sinüs dalgası dalgalanması) üretilmektedir. Toplanan girdiler FAO 33 ve 66 bitki stres algoritmaları ile Loucks hidrolik rezervuar yönetim denklemleri katmanlarından geçirilerek işlenmekte; toplam bölgesel rekolte, baraj su tasarrufu ve baraj ömrü uzama süresi çıktıları anlık olarak KPI göstergelerine, Chart.js tabanlı interaktif grafiklere ve dinamik tarla durum tablosuna aktarılmaktadır. Çıktı verileri kullanıcı tarafından CSV formatında dışa aktarılabilmektedir.

Kontrol Kaldıraçları: Kullanıcı; Verilen Su Kotası (verilen_su_kotasi), Günlük Baraj Çekimi (gunluk_baraj_cekimi), Doğal Mevsimsel Yağış (dogal_yagis) ve Bitki İdeal Su İhtiyacı (ideal_su_ihtiyaci) parametrelerini sürgüler aracılığıyla dinamik olarak kontrol edebilmektedir. Bu kaldıraçlar simülasyonun gıda arzı ve su rezervi dengesini bulma amacına doğrudan hizmet etmekte, arka plandaki matematiksel motoru eşzamanlı tetikleyerek rekolte ve baraj ömrü çıktılarının mantıksal davranışını gerçekçi bir şekilde değiştirmektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Canlıda çalışan web arayüzü katmanı (index.html, style.css, app.js) GitHub Pages üzerinde tamamen statik ve istemci taraflı (client-side) olarak sorunsuz çalışmaktadır. Sistem localhost, sunucu veya canlı uygulamayı kilitleyen herhangi bir yerel dosya yolu bağımlılığı barındırmamaktadır; yerel dosya sistemi üzerinden de bağımsız çalışabilmektedir. Python analitik motorundaki biyolojik ve hidrolik modeller web katmanına JavaScript dili ile başarıyla kopyalanmıştır. (Not: Yardımcı bir rapor derleme aracı olan generate_docx.py betiği içerisinde yerel bir mutlak klasör yolu tanımlanmış olsa da, bu durum dağıtımı hedeflenen canlı web simülasyon panelinin çalışmasını etkilememekte veya kilitlememektedir.)

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Rastgele sayı üreten algoritmaların kullanımı engellenmiş, veri doğruluğu deterministik formüllerle korunmuştur. Girdiler ile çıktılar arasında FAO standartlarına ve Loucks hidrolik modeline dayalı net bir nedensellik bağı kurulmuştur.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Sunulan dört adet kontrol sürgüsü, bir karar verici için eyleme geçirilebilir anlamlı kaldıraçları temsil etmekte ve simülasyon çıktılarını anlık olarak güncellemektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Simüle edilen 100 tarlaya ait detaylı dönüştürülmüş veriler, arayüzdeki buton aracılığıyla analiz edilmeye uygun yapılandırılmış CSV formatında dışa aktarılabilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): GEÇTİ - Raporda, hitap edilen makam olan İl Tarım ve Orman Müdürü'nün yasal yetki sınırları ve idari kabiliyetleri dahilinde uygulanabilecek, ampirik temelli somut bir bürokratik eylem planı sunulmuştur. Sabit kotalar yerine mevsimsel yağış tahminlerine dayalı dinamik iklim-adaptif kota yönetimi, biyolojik stres eşiğini gözeten kritik kuruma alarmı entegrasyonu ve damla sulama altyapısına yönelik hibe teşvikleri gibi stratejik kaldıraçlar gerçekçidir. Raporda herhangi bir kısır döngü (tautoloji), etik dışı/absürt öneri veya sığ varsayımlardan ibaret jenerik tablo yapısı bulunmamaktadır. Çözümü Satabilme ve İkna Kabiliyeti: Öğrenci, üstlendiği kurumsal rolün ciddiyetini ve hitap dilini ("Sayın İl Müdürü") rapor boyunca kusursuz bir şekilde sürdürmüştür. Karar vericinin ve saha personelinin teknik grafikleri ve KPI göstergelerini kolayca yorumlayabilmesi amacıyla kurgulanan "5 Yaş Kuralı" altındaki günlük hayat analojileri (Mahsul Yolu, Rezervuar Kumbarası), projenin ikna kabiliyetini ve yönetim makamına sunum kalitesini en üst seviyeye taşımaktadır. Veri Temelli Kanıtlar ve Simülasyon Atıfları: Rapor, geliştirilen simülasyon motorunun ampirik çıktılarıyla tam bir veri senkronizasyonu içerisindedir. Çok değişkenli kriz senaryoları bölümünde; Senaryo A, Senaryo B ve Senaryo C başlıkları altında simülasyondan elde edilen spesifik rekolte tonajları (703.87 Ton, 96.00 Ton, 863.84 Ton), baraj su tasarrufu hacimleri ve net rezervuar ömrü uzama süreleri (+480.0 Gün, +960.0 Gün, +256.0 Gün) tablolara ve grafiklere doğrudan atıf yapılarak somut kanıtlarla sunulmuştur. Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Yapay zekanın üretebileceği basmakalıp dolgu paragrafları, robotik geçiş ifadeleri veya düzenlenmemiş jenerik başlıklar rapordan tamamen arındırılmıştır; içerik özgünleştirilmiş ve kurumsal dile uyarlanmıştır. Raporun konusu net, akademik referansları APA formatında eksiksizdir. Uygun bir hitap yapısıyla başlayıp resmi bir kapanışla tamamlanan raporda öğrencinin tam adı, soyadı ve öğrenci numarası doğrulanabilir şekilde yer almaktadır. Raporun genelinde kurumsal ciddiyete yakışmayan hiçbir emoji kullanımına yer verilmemiştir.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

Kusursuz teslimat, puan kırılmamıştır.

NİHAİ FİNAL NOTU: 80 XP