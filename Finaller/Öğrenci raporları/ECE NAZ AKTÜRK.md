# DENETİM RAPORU: ece-naz/hava_yolu

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Öğrencinin kurguladığı simülasyon yapısı, Kaggle'daki gerçek bir havayolu yolcu memnuniyeti veri setinin mimarisine sadık kalınarak oluşturulmuş bir popülasyon sentezleme mekanizmasına dayanmaktadır. script.js dosyasındaki `calculateScore` fonksiyonu, Math.random() çıktısını kontrolsüz bir gürültü olarak kullanmak yerine, her yolcu için kalıcı ve sabit bir sapma payı (fixedNoise) üretmek amacıyla kullanmıştır. Kullanıcı arayüzündeki slider girdileri (Wi-Fi, Koltuk, İkram vb.), yolcuların ham puanları ile doğrudan matematiksel olarak işlenmekte ve eşik değerlerine göre memnuniyet durumunu (Satisfied, Neutral, Dissatisfied) dinamik olarak değiştirmektedir. Sistemde hileli veya göz boyamaya yönelik kör bir rastgelelik bulunmamaktadır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Veri akışı, kullanıcının filtre ayarlarına (Uçuş Sınıfı, Müşteri Sadakati, Seyahat Amacı) bağlı olarak `generatePopulation` fonksiyonunun 1000 kişilik bir sentetik yolcu popülasyonu üretmesiyle başlar. Her yolcu nesnesi, demografik özelliklerine göre taban hizmet puanları (baseWifi, baseSeat vb.) alır. Bu veriler `calculateScore` fonksiyonunda ağırlıklı bir memnuniyet puanına (100 üzerinden) dönüştürülür. Çıktılar HTML5 Canvas üzerinde canlı parçacık simülasyonu (Particle sınıfı) olarak görselleştirilirken, Chart.js grafikleri (Donut, Radar, Geçiş Analizi) ve 50 satırlık bir önizleme tablosu anlık olarak güncellenmektedir.

Kontrol Kaldıraçları: Kullanıcı, Wi-Fi Altyapısı, Koltuk Konforu, İkram Kalitesi, Uçak İçi Eğlence, Çevrimiçi Rezervasyon, Kabin Temizliği (-5 ile +5 arası) ve Rötar Süresi (-30 ile +30 dk arası) kaldıracaklarını yönetebilmektedir. Bu kaldıraçlar simülasyon çıktılarını doğrudan etkilemektedir; örneğin rötar süresinin artırılması formüldeki ceza puanını (finalDelay / 10) artırarak yolcuların olumsuz yönde statü değiştirmesine neden olmaktadır. Kontroller kozmetik değildir, amaca doğrudan hizmet eder.

Localhost Kontrolü: GEÇTİ - Kod yapısı incelendiğinde harici kütüphaneler CDN üzerinden çekilmiş olup, dosya yolları göreceli (relative) olarak kurgulanmıştır. Kod tabanında localhost, 127.0.0.1 veya yerel mutlak dosya yolu referansları bulunmamaktadır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Uçuş sınıfı (Business sınıfına +10 puan bonus) ve seyahat amacının memnuniyet üzerindeki etkisi formüle edilmiştir. Veri akışı ve durum geçiş mantığı (Transition History) matematiksel bir modelleme ile hatasız çalışmaktadır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde yer alan slider ve select elementleri eyleme geçirilebilir operasyonel kararları temsil eder. Bu parametrelerdeki değişimler simülasyon haritasındaki parçacıkların konumunu ve memnuniyet grafiklerini dinamik olarak etkilemektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: `downloadCsv` fonksiyonu yardımıyla, simülasyondaki 1000 yolcunun demografik bilgileri, kullanıcı modifikatörleri eklenmiş nihai hizmet puanları, başlangıç ve güncel memnuniyet durumları "Yolcu_Memnuniyeti_Veri_Seti.csv" adıyla yapılandırılmış CSV formatında dışa aktarılabilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Üstlenilen Rol ve Konu Uygunluğu: Öğrenci, bir havacılık analitiği ve veri bilimi uzmanı rolünü mükemmel bir şekilde üstlenmiştir. Rapor, bir havayolu şirketinin yönetim kurulu ve karar alıcı mekanizmaları için doğrudan eyleme geçirilebilir, operasyonel darboğazları deşifre eden ve bütçe optimizasyonu sağlayan stratejik bir problem çözümüne odaklanmıştır. Rol yapma derinliği oldukça yüksektir. Anlatım ve Basitlik Düzeyi: Rapordaki anlatım son derece akıcı, profesyonel ve gereksiz teknik terim kalabalığından arındırılmıştır. "Düşük maliyetle müşteri koruma", "nötr yolcu riski" gibi karmaşık iş zekası kavramları bir yöneticinin saniyeler içinde yorumlayabileceği makro göstergeler düzeyine indirgenerek sadeleştirilmiştir. Grafiklerin (Doughnut, Radar, Bar) işlevleri ve simülasyondaki karşılıkları çok net özetlenmiştir. Yapay Zeka İzleri ve Özensizlik: Metin baştan sona tutarlı, kurumsal bir süzgeçten geçirilmiş ve entegrasyon kalitesi yüksek bir dille yazılmıştır. Yapay zekanın ürettiği basmakalıp dolgu paragrafları veya jenerik başlık düzenleri bulunmamaktadır. İçerik tamamen özelleştirilmiş ve konuya sadık kalınarak yapılandırılmıştır. Rapor Dil ve Profesyonelliği: Rapor kurumsal bir yönetim kurulu hitabı ve stratejik problem tanımıyla başlamakta, resmi/kurumsal bir üslup korumakta ve saygı/iş birliği içeren profesyonel bir kapanış metniyle sonlanmaktadır. Metin içerisinde hiçbir emojiye yer verilmemiştir. Ancak en kritik kusur; rapor metninin veya sonunun hiçbir yerinde öğrencinin ad-soyad bilgisine yer verilmemiş olmasıdır.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporda adınız ve soyadınız açıkça yazmadığı, kimliğiniz net olarak tespit edilemediği ve sınıf listesinde dedektiflik yapılmasına sebebiyet verdiği için kurallar gereği rapor doğrudan REDDEDİLMİŞTİR.
    

NİHAİ FİNAL NOTU: 0 **XP**