---
gorev_13: 75
final_notu: 95
---
# DENETİM RAPORU: baserdilara94-ui / Eco-Route (Dilara Başer)

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Projedeki otomatik senaryo üretimi butonu, test ve toplu veri analizi amacıyla sınırlandırılmış aralıklarda meşru rastgele girdiler üreterek simülasyon modelini çalıştırmaktadır; ana matematiksel model ise tamamen deterministik olup kullanıcı girdilerine doğrudan bağlıdır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, verilerini kullanıcı arayüzündeki kontrol kaldıraçlarından (slider/input) veya otomatik senaryo test aracından alır. Alınan bu veriler `calculateAQI` fonksiyonu içinde hareket/rölanti oranları, PM2.5 emisyon katsayıları, rüzgar dağılımı (bina kat sayısı engeli dahil) ve yeşil alan filtrasyonu hesaplamalarından geçirilerek nihai Hava Kalitesi İndeksine (AQI) dönüştürülür. Elde edilen çıktılar Chart.js grafiğinde görselleştirilir, durum rozetleri atanır, AQI seviyesine göre en uygun alternatif güzergah önerilir ve veriler dinamik tablolara eklenir.

Kontrol Kaldıraçları: Kullanıcı; Standart Araç (Fosil), Elektrikli Araç (EV), Işık Bekleme Süresi, Rüzgar Hızı, Yeşil Alan Oranı ve Bina Kat Sayısı parametrelerini doğrudan değiştirebilmektedir. Bu faktörler simülasyon çıktısını doğrudan ve mantıksal olarak etkilemektedir; örneğin bina kat sayısının artırılması rüzgarın temizleyici etkisini matematiksel olarak azaltırken, yeşil alan oranının artırılması partikül filtrasyonunu artırmaktadır. Kontroller kozmetik değildir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Kod tabanında localhost, yerel IP adresleri (127.0.0.1) veya yerel bilgisayara ait mutlak dosya yollarına bağımlılık tespit edilmemiştir. Uygulama tamamen istemci taraflı (HTML/CSS/JS) teknolojilerle inşa edildiğinden GitHub Pages gibi statik web barındırma platformlarında sorunsuz bir şekilde canlı olarak çalışmaya uygundur. Not: Repoda bulunan harici `script.js` dosyası, `index.html` içinde çağrılmamış olup atıl (eski bir versiyondan kalma) durumdadır; ancak `index.html` kendi içindeki inline script bloğuyla tüm sistemi bağımsız ve hatasız bir şekilde yürütebilmektedir.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Girdiler ile AQI çıktıları arasında EPA MOVES3 ve EEA EMEP gibi bilimsel kılavuzları referans alan, rölanti ve emisyon mantığına oturtulmuş gerçekçi matematiksel bir ilişki kurgulanmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan 6 farklı kaldıraç, bir yerel yönetim simülasyonu senaryosuna doğrudan hizmet eden, anlamlı ve çıktı dengelerini dinamik olarak değiştiren eyleme geçirilebilir parametrelerdir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Hem manuel hem de otomatik senaryo geçmişi verileri, yapılandırılmış nesne dizilerinde tutulmakta ve UTF-8 BOM (`\uFEFF`) kodlaması eklenerek Türkçe karakter uyumlu CSV dosyaları olarak dışa aktarılabilmektedir.

NİHAI DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Üstlenilen Rol ve Konu Uygunluğu: Öğrenci, şirket bünyesinde sürdürülebilirlik ve lojistik süreçlerini yöneten bir uzman/danışman rolünü başarıyla üstlenmiştir. Lojistik operasyonlarında araç tercihlerinin ve kentsel morfolojinin (bina kat sayısı, yeşil alan) hava kalitesine etkisini modellemek, karar alıcı bir yönetici için hem şirket itibarı (ESG hedefleri) hem de operasyonel rotasyon kararları açısından doğrudan problem çözücü ve stratejik bir nitelik taşımaktadır.

Anlatım ve Basitlik Düzeyi: Rapordaki anlatım oldukça sade, net ve takip edilebilirdir. Kanyon etkisi, rölanti emisyonları ve partikül filtreleme gibi teknik kavramlar aşırı ağdalı bir akademik dile boğulmadan, bir yöneticinin hızla kavrayabileceği netlikte aktarılmıştır. Tablo ve grafik altı açıklamaları simülasyon çıktılarının okunabilirliğini ciddi şekilde artırmaktadır.

Yapay Zeka İzleri ve Özensizlik: Metinde yapay zekaya ait basmakalıp dolgu paragraflarına veya düzenlenmemiş jenerik yapılara rastlanmamıştır. Öğrenci; EPA MOVES3, EEA EMEP ve WHO gibi bilimsel kılavuzları entegre ederek metni kendi süzgecinden geçirmiş, projenin özgün girdileriyle tutarlı, özenli bir rapor dili oluşturmuştur.

rapor Dil ve Profesyonelliği: Rapor kurumsal ve ciddi bir üslup ile kaleme alınmıştır. Metin içerisinde hiçbir emojiye yer verilmemiş, grafik etiketleri ve başlıklar profesyonel standartlara uygun hazırlanmıştır. Öğrencinin adı ve soyadı raporun sonunda net bir şekilde yer almaktadır. Ancak, profesyonel rapor standartlarının gerektirdiği resmi bir başlangıç hitabı (Örn: Yönetim Kurulu Genel Müdürlüğüne vb.) ve isimden hemen önce yer alması beklenen kurumsal saygı/kapanış ifadesi (Örn: Saygılarımla, Bilgilerinize sunarım vb.) eksiktir.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Rapora kurumsal üsluba uygun resmi bir hitap cümlesiyle başlanmadığı için puan kırılmıştır.
    
- Raporun kapanış kısmında, öğrenci adı-soyadından önce resmiyet arz eden bir saygı veya iyi dilek ifadesi eksik bırakıldığı için puan kırılmıştır.
    

NİHAİ FİNAL NOTU: 75 XP