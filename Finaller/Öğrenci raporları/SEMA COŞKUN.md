# DENETİM RAPORU: sema788/e-spor-lol

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. `index.html` dosyası incelendiğinde, simülasyon çıktılarının rastgele sayılar (Math.random) yerine, 2026 yılına ait gerçek taban istatistiklerin kullanıcı girdileri ve literatüre dayalı bir yaş eğrisi fonksiyonu (`ageCurve`) ile matematiksel olarak işlenmesiyle dinamik olarak hesaplandığı görülmüştür.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, taban verisi olarak Oracle's Elixir ve Leaguepedia gibi resmi kaynaklardan alınan 2026 yılı profesyonel League of Legends oyuncu istatistiklerini (`PL` nesnesi) kullanmaktadır. Bu veriler, JavaScript fonksiyonları aracılığıyla kullanıcının seçtiği parametreler ve yaş çarpanı ile işlenerek 2027–2029 yılları için Performans Skoru ve Kazanma Oranı trendlerine dönüştürülmektedir. Çıktılar Chart.js kütüphanesi yardımıyla grafiksel olarak ve HTML tablo yapısıyla arayüzde sunulmaktadır.

Kontrol Kaldıraçları: Kullanıcı; Meta Uyum Yeteneği (%30), Antrenman Yoğunluğu (%28), Fiziksel & Mental Form (%22) ve Takım Sinerji Skoru (%20) olmak üzere dört adet anlamlı ve eyleme geçirilebilir kaldıraç kontrolüne sahiptir. Bu kaydırıcıların (slider) değiştirilmesi `fm()` ve `go()` fonksiyonlarını tetikleyerek formül çarpanını (`mult`) ve dolayısıyla simülasyonun çıktı değerlerini dinamik ve gerçekçi bir şekilde değiştirmektedir.

Localhost Kontrolü: GEÇTİ - Kod tabanında 'http://localhost', yerel IP veya yerel mutlak dosya yolu referanslarına rastlanmamıştır. CDN bağlantıları ve global referanslar kullanılmıştır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Projeksiyon modeli akademik bir referansa (Pizzo et al. 2023) dayandırılmış olup, oyuncu yaşlarına göre azalan veya artan bir performans eğrisi mantıksal bir örüntüde kurgulanmıştır. Veri akışı tutarlı ve doğrusaldır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan 4 adet girdi kontrolü, e-spor ekosistemindeki performansı doğrudan etkileyen eyleme geçirilebilir parametreleri temsil etmektedir ve simülasyon çıktılarını doğrudan etkilemektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Kod içerisinde yer alan `exportOne()` ve `exportAll()` fonksiyonları, üretilen tahmin verilerini yapılandırılmış CSV formatında ve UTF-8 BOM standardına uygun olarak başarılı bir şekilde dışa aktarmaktadır.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

## FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

### GENEL ANALİZ

- **Üstlenilen Rol ve Konu Uygunluğu:** Öğrenci, e-spor ekosistemine uzak bir kurumsal yatırımcıya veya şirket pazarlama müdürüne hitap eden bir e-spor danışmanı rolünü üstlenmiştir. Konu seçimi ve sponsorluk yatırımlarının geri dönüşü (ROI) üzerine kurulan gelecek senaryoları, bir karar alıcı için finansal riskleri yönetmek adına oldukça pratik ve stratejik bir nitelik taşımaktadır.
    
- **Anlatım ve Basitlik Düzeyi:** Rapordaki dil son derece akıcı ve sade olup, karmaşık oyun mekanikleri geleneksel spor analojileriyle (futbol stoperi, basketbol şutörü vb.) desteklenerek anlaşılır kılınmıştır. Oyuncu projeksiyon tahminleri, yaş eğrisi analizleri ve bütçe planlamaları karar alıcının kolayca takip edebileceği net tablolar halinde yapılandırılmıştır.
    
- **Yapay Zeka İzleri ve Özensizlik:** Metin genelinde yapay zekaya ait jenerik dolgu paragraflarına, basmakalıp robotik geçiş ifadelerine veya ham bırakılmış kalıp başlıklara rastlanmamıştır. Yapay zeka çıktısı özgün bir süzgeçten geçirilmiş ve e-spor jargonuna uygun şekilde düzenlenmiştir.
    
- **rapor Dil ve Profesyonelliği:** Rapor kurumsal bir üsluba sahiptir, içerikte emoji kullanılmamıştır ve uygun bir saygı/kapanış ifadesi yer almaktadır. Ancak projenin hem kapak hem de imza kısmında öğrencinin resmi kayıtlarda doğrulanabilecek tam adı ve soyadı bulunmamaktadır; rapor sadece "Sema" ön adıyla sonlandırılmıştır.
    

### PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporda ve teslim edilen kurumsal iletişim kanallarında tam adınız ve soyadınız yer almamaktadır.
    
- Sınıf listesinde aynı ada sahip birden fazla öğrenci (iki adet Sema) bulunması nedeniyle, teslim edilen raporun kime ait olduğu hususunda kimlik doğrulanabilirliği sağlanamamış ve dedektiflik yapılması gerekmiştir. Kurumsal ve akademik raporlama standartlarına aykırı olan bu kimlik belirsizliği nedeniyle raporunuz doğrudan REDDEDİLMİŞTİR.
    

**NİHAİ FİNAL NOTU:** 0 XP