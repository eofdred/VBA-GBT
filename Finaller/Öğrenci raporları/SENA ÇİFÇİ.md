---
gorev_13: 0
final_notu: 10
ogrenci_no: 2511317018
butunleme_notu: 80
---
# FİNAL
## DENETİM RAPORU: senacifci5-prog / Sena Çiftçi

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
## FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): KALDI - Raporda, karar alıcının stratejik karar mekanizmasında doğrudan kullanabileceği somut, ölçülebilir, kurumsal ve bürokratik bir eylem planı sunulmamıştır. Önerilen çözümler, bütçe yönetimi ve kurumsal işleyişten uzak, "eğitime yatırılması, okullar açılması" gibi genel geçer ve sığ varsayımlardan ibarettir. Simülasyonun kod kurgusundaki doğrusal bağımsız değişken etkileri (işsizlik artınca suçun artması gibi) stratejik bir politika eylemi gibi yansıtılmış ancak ampirik bir öngörü kurgulanamamıştır.

Çözümü Satabilme ve İkna Kabiliyeti: Raporda kullanılan analojiler (çatı tamiri, bataklık-sivrisinek örnekleri) ve hitap tarzı, karar alıcıya yönelik bir satış üslubu taşımaktadır. Konuya yaklaşım problem çözme odaklı görünse de, bu ikna dili somut kurumsal eylemlerle desteklenmediği için soyut bir ödev anlatımı seviyesini aşamamıştır.

Veri Temelli Kanıtlar ve Simülasyon Atıfları: Öğrenci, geliştirdiği simülasyondan elde edilen ampirik verilere, spesifik sayılara, yüzdelere veya grafik çıktılarına raporda hiçbir şekilde yer vermemiştir. "Suçlar patlıyor", "hızla artıyor" veya "hapishaneler dolup taşıyor" gibi genel ifadeler kullanılmış, simülasyon sonuçlarına dair somut bir kanıt sunulmamıştır.

Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Yapay zeka entegrasyonu esnasında üretilen jenerik dolgu paragrafları ve basmakalıp anlatımlar süzgeçten geçirilmeden metinde bırakılmıştır. Bununla birlikte, raporda emoji kullanılmamış, kurumsal üsluba uygun bir hitapla başlanmış, saygı ifadesiyle bitirilerek ad-soyad bilgisi net bir şekilde sunulmuştur.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporda eyleme geçirilebilir bir stratejik kaldıraç ve somut bürokratik eylem planı bulunmadığı, politika önerileri sığ ve genel geçer varsayımlardan ibaret olduğu için rapor "Stratejik Eyleme Geçirilebilirlik (1. Kritik Eşik)" kriterinden kalmış ve REDDEDİLMİŞTİR (0 XP).
    
- Geliştirilen simülasyon sistemindeki sayısal verilere, oranlara ve metriklere raporda hiçbir spesifik atıf yapılmamış, metin simülasyon çıktılarından kopuk ve tamamen teorik düzeyde bırakılmıştır.
    

NİHAİ FİNAL NOTU: 0 XP

# BÜTÜNLEME

DENETİM RAPORU: crime-simulation / Sena Çifçi

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, "Yerel Projeksiyon" sekmesinde Türkiye'nin 2016-2026 yıllarına ait gerçek suç ve ekonomi istatistiklerini (historicalData dizisi) başlangıç (baseline) verisi olarak alır. "Küresel Analiz" sekmesinde ise Dünya Bankası API'si üzerinden sağlanan UNODC cinayet ve ekonomi verilerini kullanır (Bu veriler geliştirici tarafından fetch_global_data.py scripti ile çekilip global_data.js içerisine statik olarak yazdırılmıştır). Simülasyon, kullanıcı 2027 ve sonrası için değişkenleri güncellediğinde, son tarihsel yılın değerleri ile kullanıcının girdiği hedef değerler arasındaki farkları bularak (delta), her bir bağımsız değişken için belirlenmiş katsayılarla (örneğin işsizlikteki bir birim artışın suç sayısına 50, Gini'deki artışın 2000 birim etki etmesi gibi) deterministik matematiksel hesaplamalar yapar. Üretilen veriler doğrudan grafiklere ve göstergelere aktarılır.

Kontrol Kaldıraçları: İşsizlik Oranı, Enflasyon (TÜFE), Gini Katsayısı, Yakalanma Olasılığı, Ortalama Fiili Ceza Süresi ve Eğitim Bütçesi (% GSYH). Bu kontroller kesinlikle kozmetik değildir. "calculateProjection()" fonksiyonu incelendiğinde, slider üzerinden alınan her bir değerin Toplam Suç Sayısı, Tekrar Suç İşleme, Cezaevi Mevcudu, Denetimli Serbestlik ve Rehabilitasyon çıktılarını dinamik olarak belirleyen matematiksel formüllere doğrudan bağlı olduğu görülmektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Proje statik dosyalardan (HTML, CSS, JS) oluşmaktadır ve GitHub Pages gibi statik sunucularda tamamen sorunsuz çalışmaya uygundur. Repoda bulunan "fetch_global_data.py" betiğinde yerel bir bilgisayar yolu (c:\Users\SENA ÇİFÇİ...) bulunmasına rağmen, bu betik uygulamanın çalışma zamanı (runtime) bağımlılığı değildir. Sadece veritabanını oluşturmak için bir kez çalıştırılmış bir veri çekme betiğidir. Web uygulamasının canlı sürümü hiçbir şekilde localhost veya yerel dosya yolu aramamaktadır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Sistem, çıktı üretmek için "Math.random()" gibi kurgusal gürültüler kullanmak yerine, gerçek verilerden yola çıkarak mantıklı ağırlıklandırmalara sahip bağıntısal denklemler kullanmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Sunulan bağımsız değişkenler (suç - ekonomi - infaz ilişkisi) kriminoloji simülasyonu amacına tam uygundur ve değiştirildiklerinde sisteme doğrudan etki eden fonksiyonel kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Uygulama içerisinde "exportCSV" fonksiyonu sorunsuz kurgulanmıştır ve hem tarihsel verileri hem de üretilen projeksiyon verilerini yapılandırılmış CSV formatında kullanıcıya sunmaktadır.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): GEÇTİ. Raporda, simülasyon sonuçlarına dayalı olarak karar alıcı (Adalet Bakanlığı) için son derece gerçekçi, etik ve bürokratik olarak uygulanabilir bir stratejik eylem planı sunulmuştur. Özellikle ceza sürelerini artırmanın maliyet-etkin olmadığını ampirik olarak kanıtlayarak, bunun yerine mesleki eğitime bütçe ayrılmasını ve alternatif yaptırımlara (elektronik izleme vb.) geçilmesini önermesi, bir politika yapıcı için tam anlamıyla eyleme geçirilebilir kaldıraçlardır. Kısır döngü (tautoloji) veya içi boş jenerik tablolar bulunmamaktadır.

Çözümü Satabilme ve İkna Kabiliyeti: Öğrenci, profesyonel bir veri analisti rolünü başarıyla üstlenmiş ve bulguları doğrudan politika yapıcının "maliyet-etkinlik", "kaynak tahsisi" ve "kamusal getiri" gibi temel endişelerine hitap edecek şekilde sunmuştur. Raporun satış dili son derece bürokratik, ikna edici, analitik ve çözüm odaklıdır.

Veri Temelli Kanıtlar ve Simülasyon Atıfları: Rapor, kendi ürettiği simülasyon verilerine ve grafiklerine son derece hakimdir. Örneğin, eğitim bütçesi senaryosunda tekerrür oranının "%33,1'den %30,9'a" düşeceği veya ortalama ceza süresinin artırılmasının suçu yalnızca "%7,4" azaltırken cezaevi mevcudunu "%78,4" artırıp altyapıyı zorlayacağı gibi spesifik simülasyon çıktılarına çok sayıda somut, sayısal atıf yapılmıştır. Geçmiş verilere dair (örneğin 2020 pandemi dönemindeki rehabilitasyon ve tekerrür ilişkisi) mantıksal çıkarımlar da raporda yer bulmuştur.

Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Metin içerisindeki olası yapay zeka jenerik şablonları, dolgu paragrafları ve robotik geçişler tamamen temizlenmiş, içerik tamamen projenin mekanik parametreleriyle harmanlanmıştır. Raporun muhatabı çok net belirlenmiş , kurumsal üslup baştan sona korunmuş, metin öğrencinin açık kimliği ve iletişim bilgileri ile profesyonelce sonlandırılmış ve kesinlikle emoji kullanılmamıştır.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

Kusursuz teslimat, puan kırılmamıştır.

NİHAİ FİNAL NOTU: 80 XP