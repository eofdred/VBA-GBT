---
gorev_13: 0
final_notu: 10
---
# DENETİM RAPORU: senacifci5-prog / Sena Çiftçi

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Projede göz boyama amaçlı rastgele sayı üretimi (Math.random) yerine, kullanıcı girdilerini temel alan deterministik ve doğrusal bir matematiksel simülasyon modeli kurgulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, 2016-2026 yılları arasındaki Türkiye kaynaklı tarihsel kriminoloji ve ekonomi verilerini sabit bir dizi üzerinden yerel kurguya dahil etmektedir. Küresel veriler ise UNODC kaynaklarından harici bir Python betiği yardımıyla Dünya Bankası API'si üzerinden çekilmiş ve statik bir veri nesnesine dönüştürülerek grafik istemcisine aktarılmıştır. Üretilen simülasyon çıktıları Chart.js kütüphanesiyle görsel panellere beslenmektedir ancak dış dünyaya veri akışı kesilmiştir.

Kontrol Kaldıraçları: Arayüz üzerinde işsizlik oranı, enflasyon, Gini katsayısı, yakalanma olasılığı, ortalama fiili ceza süresi ve eğitim bütçesi için slider bileşenleri sunulmuştur. Bu kaldıraçlar kozmetik olmayıp, arka plandaki `calculateProjection` fonksiyonu vasıtasıyla toplam suç sayısı, tekerrür oranı ve cezaevi mevcudu gibi bağımlı değişkenleri doğrudan değiştiren dinamik etkilere sahiptir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Uygulamanın ana çalışma mekanizması (index.html, simulation.html) tamamen istemci taraflı statik HTML, CSS ve JavaScript mimarisindedir. GitHub Pages gibi statik sunucularda teknoloji uyuşmazlığı yaşamadan bağımsız olarak çalışabilmektedir. Veri çekme aşamasında kullanılan yardımcı Python dosyasında mutlak bir yerel yol (`c:\Users\SENA ÇİFÇİ\...`) tanımlanmış olsa da bu durum ön işleme aracı seviyesindedir ve canlı sistemin kilitlenmesine neden olmamaktadır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Girdiler ile çıktılar arasında, tarihsel temel verilerden beslenen ve sosyo-ekonomik korelasyonları yansıtan net matematiksel formüller tasarlanmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Kullanıcıya sunulan tüm arayüz kontrolleri kriminolojik amaca hizmet eden mantıklı eylemsel kaldıraçlardır ve simülasyon senaryolarını doğrudan manipüle edebilmektedir.

Eşik 3 (Veri Dışa Aktarımı): KALDI - Gerekçe: İlerletilen simülasyon geçmişinin veya üretilen projeksiyon verilerinin raporlama amacıyla CSV ya da JSON gibi yapılandırılmış bir formatta dışa aktarılmasını sağlayan herhangi bir buton, fonksiyon ya da kaydetme mekanizması kod yapısında yer almamaktadır.

NİHAİ DURUM: REDDEDİLDİ (NOT: 0)
,
# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): KALDI - Raporda, karar alıcının stratejik karar mekanizmasında doğrudan kullanabileceği somut, ölçülebilir, kurumsal ve bürokratik bir eylem planı sunulmamıştır. Önerilen çözümler, bütçe yönetimi ve kurumsal işleyişten uzak, "eğitime yatırılması, okullar açılması" gibi genel geçer ve sığ varsayımlardan ibarettir. Simülasyonun kod kurgusundaki doğrusal bağımsız değişken etkileri (işsizlik artınca suçun artması gibi) stratejik bir politika eylemi gibi yansıtılmış ancak ampirik bir öngörü kurgulanamamıştır.

Çözümü Satabilme ve İkna Kabiliyeti: Raporda kullanılan analojiler (çatı tamiri, bataklık-sivrisinek örnekleri) ve hitap tarzı, karar alıcıya yönelik bir satış üslubu taşımaktadır. Konuya yaklaşım problem çözme odaklı görünse de, bu ikna dili somut kurumsal eylemlerle desteklenmediği için soyut bir ödev anlatımı seviyesini aşamamıştır.

Veri Temelli Kanıtlar ve Simülasyon Atıfları: Öğrenci, geliştirdiği simülasyondan elde edilen ampirik verilere, spesifik sayılara, yüzdelere veya grafik çıktılarına raporda hiçbir şekilde yer vermemiştir. "Suçlar patlıyor", "hızla artıyor" veya "hapishaneler dolup taşıyor" gibi genel ifadeler kullanılmış, simülasyon sonuçlarına dair somut bir kanıt sunulmamıştır.

Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Yapay zeka entegrasyonu esnasında üretilen jenerik dolgu paragrafları ve basmakalıp anlatımlar süzgeçten geçirilmeden metinde bırakılmıştır. Bununla birlikte, raporda emoji kullanılmamış, kurumsal üsluba uygun bir hitapla başlanmış, saygı ifadesiyle bitirilerek ad-soyad bilgisi net bir şekilde sunulmuştur.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporda eyleme geçirilebilir bir stratejik kaldıraç ve somut bürokratik eylem planı bulunmadığı, politika önerileri sığ ve genel geçer varsayımlardan ibaret olduğu için rapor "Stratejik Eyleme Geçirilebilirlik (1. Kritik Eşik)" kriterinden kalmış ve REDDEDİLMİŞTİR (0 XP).
    
- Geliştirilen simülasyon sistemindeki sayısal verilere, oranlara ve metriklere raporda hiçbir spesifik atıf yapılmamış, metin simülasyon çıktılarından kopuk ve tamamen teorik düzeyde bırakılmıştır.
    

NİHAİ FİNAL NOTU: 0 XP