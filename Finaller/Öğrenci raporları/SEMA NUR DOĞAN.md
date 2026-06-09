---
gorev_13: 70
final_notu: 85
---
# DENETİM RAPORU: semadogaan/bacterialab (Sema Doğan)

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Projede kullanılan `Math.random()` fonksiyonları yalnızca görsel koloni dağılımları ve stokastik varyasyonlar için meşru bir şekilde kullanılmıştır. Büyüme kinetikleri ve fenotipik tepkiler deterministik matematiksel modellere dayanmaktadır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Uygulama, `DataLoader` modülü aracılığıyla `bacteria_dataset.json`, `tissue_models.json`, `interaction_matrix.json` ve `antibiotic_pk.json` dosyalarından yapılandırılmış literatür verilerini okur. Bu veriler `BacteriaStore` üzerinde merkezileştirilir ve `simulation.js` altındaki matematiksel motorlara (Lojistik, Lotka-Volterra, Hill Denklemi, Fick Difüzyonu) aktarılarak işlenir. Çıktılar gerçek zamanlı olarak `app.js` üzerinden Petri kabı simülasyonuna ve grafik arayüzlerine yansıtılır.

Kontrol Kaldıraçları: Kullanıcı sol panelden bakteri türü seçebilir; sağ kontrol panelinden sıcaklık, pH, NaCl ve oksijen tipini değiştirebilir; ayrıca doku tipi, antibiyotik türü, konsantrasyonu ve uygulama yolunu belirleyebilir. Bu parametreler `calcPhFactor`, `calcTempFactor` ve `calcNaClFactor` fonksiyonları üzerinden büyüme hızını doğrudan ve gerçekçi bir şekilde etkilemektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Kod tabanında localhost veya mutlak yerel dizin bağımlılığı bulunmamaktadır. Tüm veri yüklemeleri projenin bağıl yolları üzerinden `fetch` ile gerçekleştirilmektedir. Uygulama tamamen istemci taraflı JavaScript, HTML ve CSS teknolojileriyle geliştirildiğinden statik web barındırma hizmeti sunan GitHub Pages üzerinde sorunsuz bir şekilde çalışmaktadır.

EŞİK DEĞERLENDİRMELERI

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Mikrobiyolojik büyüme, rekabet ve farmakokinetik süreçler; Lotka-Volterra, Hill ve Fick difüzyon denklemleri gibi kabul görmüş akademik ve deterministik modellere dayandırılarak yüksek mekanik gerçekçilikle kurgulanmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Kullanıcıya sunulan tüm fiziksel, kimyasal ve tıbbi parametreler simülasyonun amacına hizmet eden anlamlı ve eyleme geçirilebilir kaldıraçlardır; çıktı mekaniğini doğrudan manipüle etmektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: `downloadBacteriaCSV`, `getLogCSVForPetri` ve `downloadBacteriaJSON` fonksiyonları sayesinde simülasyon çıktıları, laboratuvar günlükleri ve veri setleri CSV ve JSON formatlarında dışa aktarılabilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Üstlenilen Rol ve Konu Uygunluğu: Öğrenci, çok etkenli doku enfeksiyonlarında antibiyotik optimizasyonu gibi klinik ve farmakolojik açıdan son derece karmaşık, problem çözücü bir konuyu ele almıştır. Ancak üstlenilen rol bağlamında büyük bir yönetimsel oryantasyon hatası mevcuttur. Rapor, bir karar alıcıya, yöneticiye veya bürokrata projenin değerini "satan", eyleme geçirilebilir somut teklifler sunan bir idari/yönetimsel dil yerine; tamamen akademik bir ödev, makale veya tez özeti formatında kaleme alınmıştır. Karar alıcıya hitap hissi ve projenin ticari/idari ikna kabiliyeti oldukça zayıftır.

Anlatım ve Basitlik Düzeyi: Metin, "5 yaşındaki birine veya teknik eğitimi olmayan bir yöneticiye anlatır gibi" sadeleştirmekten çok uzaktır. Ağır akademik ve teknik bir terminoloji ($R^2$, RMSE, Hill Denklemi, Lotka-Volterra rekabet katsayıları vb.) doğrudan kullanılmıştır. Raporun geneli formüller ve teorik altyapılarla doldurulmuş, karmaşıklık düzeyi bir yöneticinin hızlı karar almasını kolaylaştıracak şekilde basitleştirilmemiştir.

Yapay Zeka İzleri ve Özensizlik: Metinde doğrudan kopyala-yapıştır yapılmış yapay zeka dolgu paragraflarına veya unutulmuş AI kod yorum satırlarına rastlanmamıştır. Bölümler mantıklı bir akışla yapılandırılmıştır. Ancak "Giriş", "Yöntem" ve "Bulgular" gibi bölümlendirmeler, yapay zekanın standart akademik rapor üretme şablonlarını ve dil kalıplarını çağrıştırmaktadır.

Rapor Dil ve Profesyonelliği: Raporun konusu net olarak belirtilmiş ve akademik yazım kurallarına uygun bir dil tercih edilmiştir. Metin içerisinde emoji kullanımına rastlanmamıştır. Ancak kurumsal/idari raporlama kuralları açısından çok kritik iki profesyonellik ihlali mevcuttur: Rapor kurumsal/profesyonel bir hitap cümlesiyle ("Sayın Hakem Heyeti", "Sayın Yönetici" vb.) başlamamakta ve saygı/iyi dilek bildiren profesyonel bir kapanış cümlesiyle bitmemektedir. Öğrencinin adı, soyadı ve numarası başlıkta açıkça belirtilmiştir.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Rapor, bir yöneticiyi veya karar alıcıyı ikna etmeye yönelik bir "çözüm satma" diliyle değil, tamamen geleneksel bir akademik makale/ödev üslubuyla yazıldığı için puan kırılmıştır.
    
- Metin, hedef kitlenin (yönetici/bürokrat) anlayabileceği sadeliğe indirgenmemiş, formüller ve yoğun teknik terimlerle ağırlaştırılmıştır.
    
- Raporda kurumsal ve profesyonel bir hitap metni bulunmamaktadır.
    
- Raporun sonunda saygı/iyi dilek bildiren profesyonel bir kapanış ifadesine yer verilmemiştir.
    

NİHAİ FİNAL NOTU: 70 XP