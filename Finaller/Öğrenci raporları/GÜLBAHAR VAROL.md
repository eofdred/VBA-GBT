---
gorev_13: 0
final_notu: 20
ogrenci_no: 2511317007
butunleme_notu: 75
---
# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): KALDI - Sisteme yüklenen dosyalar çözümlenemeyen ham binary (zip/docx) verisi olarak iletildiğinden, içerikte politika yapıcılar için eyleme geçirilebilir ampirik bir sonuç, öngörü veya bürokratik bir eylem planı tespit edilememiştir.

Çözümü Satabilme ve İkna Kabiliyeti: Yetersiz - Okunabilir ve anlamlı bir metin dokusu bulunmadığından, projenin bir karar alıcıya sunum/satış dili ve ikna kabiliyeti değerlendirilememiştir.

Veri Temelli Kanıtlar ve Simülasyon Atıfları: Yetersiz - Dosya içeriklerinin sıkıştırılmış binary yapıda olması sebebiyle simülasyon çıktılarına veya ampirik verilere yönelik hiçbir atıf okunamamıştır.

Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Yetersiz - Raporun profesyonel standartlara uygunluğu, hitap yapısı ve yapay zeka dolgularından arındırılmış olma durumu kontrol edilememiştir. Ayrıca metin okunamadığı için öğrenci ad-soyad doğrulaması ve kimlik tespiti yapılamamaktadır.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporda öğrencinin tam adı ve soyadı net olarak okunup tespit edilemediği ve kimlik doğrulanabilirliği sağlanamadığı için rapor REDDEDİLMİŞTİR.
    
- Teslim edilen dosyaların içeriği okunabilir metin formatında olmayıp, doğrudan ham binary kod yığını olarak kaldığından Kritik Eşik (Stratejik Eyleme Geçirilebilirlik) geçilememiş ve KALDI olarak işaretlenmiştir.
    
- Herhangi bir eyleme geçirilebilir eylem planı, stratejik kaldıraç ve simülasyon verisi sunulmadığı için değerlendirme kriterleri karşılanamamıştır.
    

NİHAİ FİNAL NOTU: 0 XP

# BÜTÜNLEME

DENETİM RAPORU: [Gülbahar Varol / Global-Mortalite-Sim-lasyonu]

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, Dünya Sağlık Örgütü (WHO) ve BM (UN) verilerini temel alan (bölgelere göre 2026 yılı tahmini nüfusları, başlangıç PM2.5, tütün ve şeker kullanım oranları vb.) bir durumdan beslenmektedir. Yaş ve cinsiyete dayalı kohortlar üzerinden, hastalık risk katsayılarını (Relative Risk ve Population Attributable Fraction metodolojisi ile) yeniden hesaplayarak ileriye dönük ölüm sayılarını hesaplar. Üretilen veriler dinamik olarak demografik piramit, harita, grafikler üzerinde gösterilmekte ve yapılandırılmış tablo (CSV) formatına dönüştürülmektedir.

Kontrol Kaldıraçları: Kullanıcı arayüzünde "Şeker Vergisi, PM2.5 Azaltımı, Tütün Kontrolü, Tuz Azaltımı" gibi politikalar toggle (aç-kapat) butonları ile sunulmuş ve her biri için %0-100 arasında etki şiddeti kaydırıcısı (slider) eklenmiştir. Bu kontroller kozmetik değildir; doğrudan `impact` fonksiyonu aracılığıyla modelin temelindeki risk çarpanlarını (`pm25Multiplier`, `smokingMultiplier` vb.) modifiye ederek gelecek yıllardaki ölüm formüllerini matematiksel olarak yeniden hesaplatmaktadır. Ayrıca bölge, yaş ve yıl gibi veri filtreleme kontrolleri mevcuttur.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Proje tamamen tarayıcı tabanlı (client-side) çalışan, tek bir bağımsız HTML/JS/CSS dosyasından (`index.html`) oluşmaktadır. Kod içinde yerel bir dosya yoluna (`C:/`, `localhost` vs.) veya harici bir backend servisine bağımlılık bulunmamaktadır. Statik sunucu ortamlarında (örn. GitHub Pages) tam uyumlu olarak çalışmaktadır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Simülasyonda "rastgele (random) gürültü" üretilmemiş; kaba ölüm oranları, yaş piramitleri ve risk çarpanları birbirine matematiksel bir epidemiyoloji modeli doğrultusunda bağlanmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Sunulan politika kaydırıcıları ve seçenekler, doğrudan hastalık yayılımlarını ve mortalite oranlarını gerçekçi ölçülerde dinamik olarak etkileyen mantıklı kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Sistem, seçilen parametrelerin etkisini, önlenen ölüm oranlarını ve demografik değişiklikleri kapsayan analiz amaçlı temiz bir yapılandırılmış "mortality_simulation_data.csv" çıktısı verebilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): GEÇTİ - Raporda tautoloji (kısır döngü) veya altı boş jenerik tablolar bulunmamaktadır. Karar alıcı konumundaki Sağlık Bakanlığı'nın kendi yetki alanında uygulayabileceği ampirik verilere dayalı, somut, gerçekçi ve eyleme geçirilebilir bürokratik kaldıraçlar (vergilendirme, tuz azaltım programları, dumansız hava sahası vb.) net bir eylem planı olarak sunulmuştur.

Çözümü Satabilme ve İkna Kabiliyeti: Öğrenci, veri analisti rolünü ikna edici bir şekilde üstlenmiş ve tasarladığı simülasyonu bir "karar destek aracı" olarak başarıyla sunmuştur. Kuruma yönelik yazım dili profesyonel, objektif ve bürokratik karar alma süreçlerine katkı sağlayacak niteliktedir. Satış dili oldukça başarılıdır.

Veri Temelli Kanıtlar ve Simülasyon Atıfları: Rapor, tamamen kendi simülasyon çıktılarına dayanmaktadır. Eklenen grafiklere metin içinde doğrudan atıflar yapılmış (Örn: Grafik 1, Grafik 4) ve simülasyonun ürettiği spesifik sayılar (Örn: Afrika bölgesinde şeker vergisi senaryosu altında önlenen ölüm sayısının sıfır hesaplanması) detaylıca analiz edilerek veri temelli kanıtlar güçlü bir şekilde kullanılmıştır.

Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Rapor dili temiz, akıcı ve yapay zeka dolgu metinlerinden arındırılmıştır. Emoji kullanılmamıştır ve giriş hitabı son derece uygundur. Kimlik tespiti net bir şekilde yapılmıştır. Ancak kurumsal raporlama standartlarında beklenen profesyonel kapanış bölümünde eksiklik tespit edilmiştir.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporun girişinde uygun bir kurumsal hitap ve kimlik beyanı bulunmasına rağmen, raporun en sonunda profesyonel bir kapanış ritüeli (saygı/iyi dilek ifadesi ve ad-soyad ile bitiriş) yapılmadığı ve doğrudan kaynakça ile bitirildiği için -5 puan kırılmıştır.
    

NİHAİ FİNAL NOTU: 75 XP