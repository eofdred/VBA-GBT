DENETİM RAPORU: ustunkayaeylul72/trafik_kazalari / Eylül ÜSTÜNKAYA

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, 1975-2023 yılları arasındaki tarihsel can kaybı ve araç-mil seyahati (VMT) verilerini doğrudan NHTSA FARS veri tabanından almaktadır. 2024-2035 yılları arasındaki gelecek projeksiyonları ise 2023 yılı taban değerleri referans alınarak, kullanıcı tarafından belirlenen risk ve koruyucu faktör oranlarına göre katsayı tabanlı matematiksel formüllerle hesaplanmaktadır. Elde edilen sonuçlar Chart.js kütüphanesi yardımıyla interaktif grafiklere aktarılmakta, aynı zamanda ham veri olarak CSV ve JSON formatlarında dışa aktarılabilmektedir.

Kontrol Kaldıraçları: Kullanıcı arayüzü; alkol etkili sürüş, hız ihlali, kemersiz yolcu ölümleri, dikkat dağınıklığı, emniyet kemeri kullanım oranı, ADAS teknoloji penetrasyonu, yıllık VMT büyüme hızı ve yol iyileştirme endeksi olmak üzere sekiz adet dinamik kontrol sunmaktadır. Bu kaldıraçlar kozmetik birer unsur olmayıp arka plandaki risk çarpanını (r) doğrudan değiştirmekte, can kaybı ve ölüm oranları üzerinde doğrusal ve anlamlı değişimler yaratmaktadır.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Projenin canlı simülasyon arayüzü, harici kütüphaneleri CDN üzerinden yükleyen tek bir statik HTML yapısıyla kurulmuştur ve GitHub Pages üzerinde sorunsuz şekilde çalışmaktadır. Word raporunu otomatik oluşturan Python betiği ise mutlak yerel dizin yolları yerine göreceli dosya yolları kullanmakta ve sistem üzerinde herhangi bir yerel bilgisayar kısıtı veya kilitlenme yaratmamaktadır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Projede kontrolsüz rastgele sayılar veya sahte gürültü üretimi bulunmamaktadır. Gelecek tahminleri NHTSA ve IIHS literatür verilerinden türetilmiş gerçekçi katsayılara dayanan işlevsel bir modelle kurgulanmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan tüm kontrol parametreleri trafik güvenliği politikalarıyla doğrudan ilişkili, anlamlı ve simülasyon çıktılarını dinamik olarak manipüle edebilen eyleme geçirilebilir kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Üretilen zaman serisi simülasyon verileri ve girdi faktör değerleri, harici veri analizine uygun yapılandırılmış CSV ve JSON formatlarında başarıyla dışa aktarılmaktadır.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): GEÇTİ - Gerekçe: Raporda, hitap edilen kurum olan Karayolları Genel Müdürlüğü Trafik Güvenliği Dairesi Başkanlığının kurumsal yetki sınırları ve stratejik karar mekanizmalarıyla doğrudan uyumlu, ampirik sonuçlara dayanan, net ve gerçekçi bürokratik politika önerileri sunulmuştur. Girdileri anlamsızca tekrarlayan kısır döngüsel (tautolojik) yapılar veya sığ genel geçer tablolar yerine; mobil denetimlerin artırılması, ADAS donanımlı araçlara yönelik teşvikler ve yol altyapısı iyileştirmeleri gibi eyleme geçirilebilir somut bir eylem planı kurgulanmıştır.

Çözümü Satabilme ve İkna Kabiliyeti: Öğrenci girdiği analist rolünü başarıyla sürdürmüş ve konuyu jenerik bir akademik ödev formatından çıkararak karar alıcı için net bir problem çözücü teklif şeklinde yapılandırmıştır. Simülasyonu rasyonel bir bütçe planlama aracı olarak konumlandırması ve kısıtlı bütçeyle maksimum hayat kurtarma hedefine odaklanması, ikna kabiliyetini ve satış dilini son derece güçlü kılmaktadır.

Veri Temelli Kanıtlar ve Simülasyon Atıfları: Rapor, öğrencinin kendi geliştirdiği simülasyon modelinden elde edilen verilere ve senaryo sonuçlarına çok net ve somut atıflar içermektedir. Vision Zero senaryosunda 2035 yılı tahmini can kaybının 6.111 seviyesine düşmesi, emniyet kemeri politikasıyla tek başına 2.200 can kurtarılması ve alkol denetimleriyle 4.000'in üzerinde insanın hayatta kalması gibi ampirik bulgular simülasyon sonuçlarından doğrudan kanıt olarak sunulmuştur.

Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Yapay zeka çıktısı hissi veren ham dolgu paragrafları, robotik geçişler veya jenerik başlıklar tamamen temizlenmiş; kurumsal standartlara uygun profesyonel bir dil inşa edilmiştir. Uygun bir hitapla başlayıp kurumsal üsluba yakışan bir saygı ifadesiyle sonlandırılmıştır. Rapor metninde hiçbir emoji kullanılmamış olup öğrencinin tam adı ve soyadı (Eylül ÜSTÜNKAYA) net bir şekilde doğrulanabilmektedir.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

Kusursuz teslimat, puan kırılmamıştır.

NİHAİ FİNAL NOTU: 80 XP