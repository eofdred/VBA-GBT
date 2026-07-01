---
gorev_13: 0
final_notu: 10
ogrenci_no: 2511317017
butunleme_notu: 80
---
# BÜTÜNLEME

DENETİM RAPORU: irem-deneri/s-rd-r-lebilir_sim-lasyon

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, TÜİK ve Çevre Bakanlığı referanslarına dayanan şehir nüfuslarını, kişi başı atık üretimlerini ve atık türü dağılım oranlarını (script.js ve veri_merkezi.py içerisindeki sabit sözlükler) temel girdi olarak almaktadır. Kullanıcının arayüzden belirlediği geri dönüşüm yüzdeleriyle bu deterministik sabitler matematiksel olarak çarpılarak; kurtarılan atık tonajı, lojistik sefer tasarrufu, devlet bütçesi kazancı ve kurtarılan ağaç sayısı hesaplanmaktadır. İşlenen veriler anlık olarak ekrandaki göstergelere, Chart.js grafiğine yansıtılmakta ve dışa aktarıma hazır hale gelmektedir.

Kontrol Kaldıraçları: Kullanıcı, analiz edilecek şehri (temel nüfus ve atık katsayısını belirler) ve 5 farklı atık türünün (Organik, Plastik, Kağıt, Cam, Metal) ayrıştırma ve geri dönüşüm yüzdelerini 0-100 arası çalışan "slider" yapıları ile kontrol etmektedir. Bu faktörler kozmetik değildir; doğrudan hesaplama motoruna (hesaplaVeGuncelle) bağlanarak simülasyon çıktısını, kirlilik endeksini ve tasarruf miktarlarını dinamik olarak değiştirmektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Kod tabanında localhost, 127.0.0.1 veya yerel bilgisayara işaret eden mutlak/dinamik dosya yolları bulunmamaktadır. Proje kapsamında Python ile yazılmış hesaplama motoru dosyaları bulunsa da, simülasyonun web arayüzü (index.html, script.js, style.css) tamamen istemci tarafında çalışacak şekilde (HTML/JS) kusursuz kurgulanmıştır. Herhangi bir backend çerçevesine ihtiyaç duymadığı için GitHub Pages gibi statik sunucularda dağıtımı (deployment) sorunsuz çalışacaktır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Rastgele (Math.random) veya kontrolsüz veri üretimi kullanılmamıştır. Sistem, gerçekçi kabul edilebilecek istatistiksel sabitler üzerinden deterministik ve matematiksel olarak sağlam bir atık dönüşüm mantığı işletmektedir.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Geri dönüşüm oranlarını simüle eden kaydırıcılar (slider) ve şehir seçimi, bir yerel yönetim kanun yapıcısının gerçek hayatta alacağı aksiyonları temsil eden amaca uygun, eyleme geçirilebilir ve sonuçları doğrudan etkileyen kontrollerdir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: "exportToCSV" fonksiyonu sayesinde arayüzde üretilen sonuç verileri (Kirlilik Endeksi, Bütçe Kazancı, Tasarruf vb.) analiz edilmeye uygun, yapılandırılmış bir CSV formatında başarıyla dışa aktarılabilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): GEÇTİ. Rapor, sadece teorik kurgular sunmak yerine karar alıcının (Çevre, Şehircilik ve İklim Değişikliği Bakanlığı) doğrudan uygulayabileceği somut bürokratik kaldıraçlar ve eylem planları içermektedir. Evinde atık ayrıştıran vatandaşlara su faturası indirimi veya toplu taşıma kontörü verilmesi gibi ekonomik teşvik mekanizmaları, organik atıkların kompost tesislerine yönlendirilmesiyle elde edilecek lojistik dönüşüm önerileri ve uygulamanın coğrafi bilgi sistemleri (CBS) ile entegre edilerek ulusal bir izleme ekranına dönüştürülmesi fikri son derece stratejik, uygulanabilir ve etiktir. Herhangi bir tautoloji veya sığ jenerik tablo içermemektedir.

Çözümü Satabilme ve İkna Kabiliyeti: Rapor, atık yönetimini sıradan bir çevre temizliği meselesi olmaktan çıkarıp doğrudan bir makroekonomi ve lojistik optimizasyonu (cari açık, ithalat bağımlılığı, mazot maliyetleri) problemi olarak konumlandırarak muhatabı olan politika yapıcıya çözümü mükemmel bir bürokratik dille "satmaktadır". Plastik şişenin ithal petrole, metal kutunun demir madenine benzetilmesi ikna kabiliyetini ve konunun ciddiyetini artıran başarılı bir yaklaşımdır.

Veri Temelli Kanıtlar ve Simülasyon Atıfları: Rapor kendi simülasyonundan elde edilen verilere güçlü ve doğrudan atıflar yapmaktadır. Sistemde kullanılan lojistik mazot maliyeti (43 TL), çöp kamyonu kapasitesi (10 ton) ve geri kazanım birim fiyatları (örn: Metal tonu 12.000 TL) açıkça belirtilmiştir. Bununla birlikte simülasyon motorunun ürettiği Burdur, Antalya ve İstanbul şehirlerine ait yıllık net tahmini analiz çıktıları (tasarruf edilen tutarlar, kazanılan ağaç sayıları) doğrudan tablo halinde sunularak iddialar ampirik verilerle desteklenmiştir.

Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Yapay zeka izleri, jenerik dolgu paragrafları ve robotik ifadeler tamamen temizlenmiştir. Metin, insan elinden çıkmış profesyonel bir üsluba ve akışa sahiptir. Öğrencinin kimliği, bölümü ve girdiği rol (Veri Bilimi ve Atık Politikaları Analiz Uzmanı) net bir şekilde belirtilmiştir. Kurumsal hitap kurallarına uyulmuş ("Sayın Bakanım, Değerli Bürokratlar;"), resmi bir kapanışla bitirilmiş ("Gereğini tensiplerinize arz ederim.") ve hiçbir laubali ifade veya emoji kullanılmamıştır.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

Kusursuz teslimat, puan kırılmamıştır.

NİHAİ FİNAL NOTU: 80 XP