# DENETİM RAPORU: semadogaan / BacteriaLab

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, verilerini "bacteria_dataset.json" dosyasından dinamik olarak çekmektedir. "DataLoader" sınıfı veriyi yükler ve "BacteriaStore" üzerinde anlamlandırarak tek bir birleşik model oluşturur. Seçilen bakteri türünün büyüme parametreleri, petri kabındaki anlık çevre değişkenleri (pH, sıcaklık, tuzluluk, oksijen) ile birleştirilerek "simulation.js" ve "renderer.js" içerisindeki matematiksel denklemlere (Baranyi-Roberts büyüme modeli yaklaşımı, Ratkowsky ve kardinal pH modelleri gibi bilimsel temelli formüller) aktarılır. Çıktı olarak Canvas üzerinde DLA (Diffusion-Limited Aggregation) ve blob algoritmalarıyla görsel koloni yayılımı üretilir ve "ChartManager" aracılığıyla 10 farklı grafik analizi (OD600 büyüme eğrisi, besin tüketimi, popülasyon dinamikleri, stres indeksi vb.) beslenir.

Kontrol Kaldıraçları: Kullanıcı her petri kabı için Zaman (Time), Sıcaklık (Temperature), pH, NaCl (Tuzluluk) kaydırıcılarını kontrol edebilmekte ve Oksijen seviyesini (Aerobic, Micro, Anaerobic) butonlar aracılığıyla değiştirebilmektedir. Bu kaldıraçlar sadece kozmetik değildir; kod yapısında "calcPhFactor", "calcTempFactor" ve "calcNaClFactor" fonksiyonları aracılığıyla "envFactor" değerini doğrudan etkilemekte, bu da kolonilerin büyüme hızını, boyutunu, rengini ve grafiklerdeki eğrileri dinamik ve matematiksel olarak değiştirmektedir.

Localhost Kontrolü: GEÇTİ - Canlıda çalışan kod tabanında yürütmeyi engelleyen herhangi bir sabitlenmiş localhost, 127.0.0.1 veya yerel bilgisayara ait mutlak dosya yolu referansı tespit edilmemiştir. Veri çekme ve görsel yükleme işlemleri tamamen taşınabilir şekilde göreceli (relative) yollarla kurgulanmıştır. README dosyasındaki localhost referansı yalnızca yerel test sunucusu kurulum yönergelerini içeren bir dokümantasyondur.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Proje, rastgele sayı gürültüsü üreterek göz boyamak yerine, 30 farklı bakteri türüne ait minimum, optimum ve maksimum büyüme tolerans sınırlarını içeren gerçekçi bir bilimsel veri setini temel almaktadır. Büyüme fazları (Lag, Log, Durağan, Ölüm), besin tükenmesi ve türler arası rekabet denklemleri mantıksal bir veri akışı ile simüle edilmektedir.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan tüm çevre kontrolleri simülasyon motoruna entegre edilmiştir. Faktörlerin değiştirilmesi durumunda, anlık büyüme katsayıları yeniden hesaplanmakta, Canvas çizimleri güncellenmekte ve grafik çıktıları dinamik olarak değişmektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Uygulama, üretilen simülasyon verilerinin ve deney kayıtlarının analiz edilebilmesi amacıyla gelişmiş dışa aktarım seçenekleri sunmaktadır. Deney günlükleri petri bazlı veya toplu olarak CSV formatında indirilebilmekte, ham bakteri veri seti CSV ve JSON olarak alınabilmekte ve grafik koordinat verileri "DataExportEngine" vasıtasıyla CSV'ye dönüştürülebilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN