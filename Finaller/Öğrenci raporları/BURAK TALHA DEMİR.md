---
gorev_13: 0
final_notu: 0
ogrenci_no: 2511317022
butunleme_notu: 0
---
# final
## DENETİM RAPORU: buraktalhademir/yks-sim-lasyonu

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon verileri, matematiksel Box-Muller dönüşümü kullanılarak üretilen ve gerçek ÖSYM yığılmasını taklit eden sağa çarpık bir aday havuzundan beslenmektedir. Üretilen adaylar, YÖK'ün resmi başarı sırası barajları ve coğrafi lokalizasyon eğilimlerine (kendi bölgesini %35 daha fazla tercih etme psikolojisi) göre filtrelenerek 24'lü tercih listeleri oluşturmaktadır. Bu veriler Gale-Shapley Kararlı Eşleşme Algoritması mimarisine (MaxHeap destekli veri yapısıyla) sokularak işlenmekte ve nihai ulusal kontenjan matrisine dönüştürülmektedir.

Kontrol Kaldıraçları: Kullanıcı; Aday Sayısı (N), Politika Laboratuvarı Senaryoları (Normal, Kriz: Şehir Terk Etme, Teşvik: Anadolu Kontenjan Artırımı), Politika Etki Katsayısı slider'ı ve YÖK Başarı Sırası Barajları aktif/pasif butonunu kontrol edebilmektedir. Bu kaldıraçlar sadece kozmetik unsurlar olmayıp, üniversite popülasyon ağırlıklarını, kontenjan çarpanlarını ve filtre dizilimlerini manipüle ederek eşleşme algoritmasının çıktısını doğrudan ve dinamik olarak etkilemektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Proje tamamen vanilla JavaScript, Bootstrap 5 ve Chart.js kütüphaneleri kullanılarak istemci taraflı (client-side) geliştirilmiştir. Herhangi bir localhost, 127.0.0.1 veya yerel mutlak dosya yolu bağımlılığı bulunmamaktadır. Statik bir mimariye sahip olduğu için GitHub Pages üzerinde sorunsuz şekilde canlıya alınabilir ve teknoloji uyuşmazlığı barındırmaz.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Tıp (50k), Diş (80k), Hukuk (125k) gibi resmi YÖK barajları koda tam entegre edilmiş, rastgele gürültü yerine Gale-Shapley ve Box-Muller tabanlı deterministik-stokastik bilimsel modeller kullanılmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzdeki senaryo ve yoğunluk girdileri, simülasyon motorundaki matematiksel fonksiyonları doğrudan manipüle eden anlamlı ve eyleme geçirilebilir kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Yüksek veri boyutlarında (N=250.000 durumunda) tarayıcının kilitlenmesini önleyen 10.000'lik chunk (parça) bellek yönetimine sahip, Excel uyumlu BOM kodlamalı yapılandırılmış bir CSV dışa aktarım motoru başarıyla kurulmuştur.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# DENETİM RAPORU: buraktalhademir/yks-sim-lasyonu

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon verileri, matematiksel Box-Muller dönüşümü kullanılarak üretilen ve gerçek ÖSYM yığılmasını taklit eden sağa çarpık bir aday havuzundan beslenmektedir. Üretilen adaylar, YÖK'ün resmi başarı sırası barajları ve coğrafi lokalizasyon eğilimlerine (kendi bölgesini %35 daha fazla tercih etme psikolojisi) göre filtrelenerek 24'lü tercih listeleri oluşturmaktadır. Bu veriler Gale-Shapley Kararlı Eşleşme Algoritması mimarisine (MaxHeap destekli veri yapısıyla) sokularak işlenmekte ve nihai ulusal kontenjan matrisine dönüştürülmektedir.

Kontrol Kaldıraçları: Kullanıcı; Aday Sayısı (N), Politika Laboratuvarı Senaryoları (Normal, Kriz: Şehir Terk Etme, Teşvik: Anadolu Kontenjan Artırımı), Politika Etki Katsayısı slider'ı ve YÖK Başarı Sırası Barajları aktif/pasif butonunu kontrol edebilmektedir. Bu kaldıraçlar sadece kozmetik unsurlar olmayıp, üniversite popülasyon ağırlıklarını, kontenjan çarpanlarını ve filtre dizilimlerini manipüle ederek eşleşme algoritmasının çıktısını doğrudan ve dinamik olarak etkilemektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Proje tamamen vanilla JavaScript, Bootstrap 5 ve Chart.js kütüphaneleri kullanılarak istemci taraflı (client-side) geliştirilmiştir. Herhangi bir localhost, 127.0.0.1 veya yerel mutlak dosya yolu bağımlılığı bulunmamaktadır. Statik bir mimariye sahip olduğu için GitHub Pages üzerinde sorunsuz şekilde canlıya alınabilir ve teknoloji uyuşmazlığı barındırmaz.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Tıp (50k), Diş (80k), Hukuk (125k) gibi resmi YÖK barajları koda tam entegre edilmiş, rastgele gürültü yerine Gale-Shapley ve Box-Muller tabanlı deterministik-stokastik bilimsel modeller kullanılmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzdeki senaryo ve yoğunluk girdileri, simülasyon motorundaki matematiksel fonksiyonları doğrudan manipüle eden anlamlı ve eyleme geçirilebilir kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Yüksek veri boyutlarında (N=250.000 durumunda) tarayıcının kilitlenmesini önleyen 10.000'lik chunk (parça) bellek yönetimine sahip, Excel uyumlu BOM kodlamalı yapılandırılmış bir CSV dışa aktarım motoru başarıyla kurulmuştur.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# BÜTÜNLEME

DENETİM RAPORU: yks-sim-lasyonu / buraktalhademir

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: DÜŞÜK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. (Kullanılan `Math.random()` fonksiyonu, `rankAffinity` ve `d.currentPop`değişkenleriyle birlikte öğrencilerin tercih varyansını/stokastik insan davranışını modellemek için meşru bir simülasyon parametresi olarak kurgulanmıştır; sırf grafik üretmek için eklenmiş boş bir gürültü değildir.)

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, 21.602 programlık gerçek ÖSYM 2025 YKS yerleştirme verilerini doğrudan `OSYM_RAW` adlı statik bir dizi olarak kodun içine gömülü (hardcoded) şekilde almaktadır. Bu veri `buildDatabase()`fonksiyonuyla işlenerek bölümlere ayrılmakta, kullanıcı parametreleriyle harmanlanıp simülasyon motoruna (`runSimulationLogic`) beslenmekte ve sonuçlar Chart.js aracılığıyla görselleştirilmektedir.

Kontrol Kaldıraçları: Öğrenci Aday Sayısı, Ekonomik Baskı Faktörü, Beyin Göçü Endeksi, Öğrenci Memleket Bölgesi ve Vakıf Üniversitesi Eğilimi. Bu kontroller (örneğin `ecoPressure` ve `vakifBias`) kod içerisindeki `bias` hesaplamalarında çarpan veya bölen olarak aktif bir şekilde kullanılmaktadır ve tamamen işlevseldir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Proje tamamen statik bir HTML/JS dosyası olarak tasarlanmıştır ve tüm veri içerisine gömülmüştür. Hiçbir yerel sunucu bağımlılığı (localhost) veya dosya yolu çağırma hatası barındırmaz, GitHub Pages üzerinde sorunsuz çalışır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: ÖSYM'nin gerçek veri tabanı kullanılmakta ve simülasyon döngüsü (adayların puanlarına göre sıralama ve eğilim puanlaması yapması) gerçekçi bir yerleştirme modeline dayanmaktadır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüz üzerinden değiştirilen parametreler simülasyonun matematiksel motoruna doğrudan etki etmektedir. Sadece kozmetik değildir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: `exportToCSV()` fonksiyonu kullanılarak elde edilen simülasyon sonuçlarının CSV formatında dışa aktarılması sağlanmıştır.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): KALDI. Rapor, simülasyonun teknik altyapısını, kullanılan algoritmaları (Gale-Shapley, Box-Muller, Max-Heap) ve sistemin performans metriklerini (250.000 adayın 10 saniyede hatasız yerleştirilmesi) son derece detaylı bir şekilde açıklamaktadır. Ancak rapor, bir politika yapıcı veya karar alıcı (örneğin YÖK veya Üniversite Rektörlüğü) için eyleme geçirilebilir hiçbir stratejik kaldıraç, bürokratik eylem planı veya politika önerisi sunmamaktadır. Metin, stratejik bir karar destek belgesinden ziyade, teknik bir yazılım mimarisi ve geliştirme dokümantasyonu seviyesinde kalmıştır. Çözümü Satabilme ve İkna Kabiliyeti: Rapor, geliştirilen yazılımın teknik üstünlüğünü ve algoritma kalitesini kanıtlamak açısından başarılıdır ve teknik bir ekibe sistemi çok iyi satabilir. Fakat hedef kitle olan yöneticilere veya karar alıcılara yönelik bir danışman/bürokrat dili kullanılmamıştır; rapor tamamen akademik ve algoritmik bir ödev diliyle yazılmıştır. Veri Temelli Kanıtlar ve Simülasyon Atıfları: Simülasyonun teknik kapasitesine ve çalışma hızına dair verilere doğrudan atıf yapılmıştır. Ancak simülasyonun ürettiği senaryo sonuçlarına (örneğin; OBP enflasyonunun yerleştirme oranlarını yüzde kaç oranında değiştirdiği veya belirli bir senaryoda MAKÜ'nün doluluk oranının ne kadar arttığına dair ampirik çıktılar) hiçbir atıf yapılmamıştır. Yalnızca koda önceden girilen %35'lik bölgesel eğilim parametresinden (girdi verisinden) bahsedilmiş, somut bir sonuç analizi yapılmamıştır. Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Öğrencinin adı, soyadı, numarası ve kurumu net bir şekilde belirtilmiştir. Metin yapay zeka jenerikliklerinden büyük ölçüde arındırılmış, akıcı ve terminolojik açıdan zengin bir dille yazılmıştır. Bununla birlikte, yöneticiye yönelik kurumsal bir hitap cümlesiyle başlanmamış ve saygı/iyi dilek ifadeleri içeren profesyonel bir kapanış yapılmamıştır.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporda eyleme geçirilebilir bir stratejik kaldıraç, karar alıcıya yönelik bürokratik bir eylem planı veya politika önerisi bulunmadığı, metnin yalnızca teknik bir yazılım dokümantasyonundan ibaret olduğu için "1. Kritik Eşik (Stratejik Eyleme Geçirilebilirlik)" kriterinden kalınmış ve rapor REDDEDİLMİŞTİR (0 XP).
    
- Simülasyon senaryolarından elde edilen ampirik sonuçlara ve verilere dayalı bir argüman sunulmamıştır; sadece sisteme sağlanan matematiksel girdiler anlatılmıştır.
    
- Rapor formatında olması gereken kurumsal hitap ve profesyonel kapanış (saygı/iyi dilek ifadeleri) eksiktir.
    

NİHAİ FİNAL NOTU: 0 XP