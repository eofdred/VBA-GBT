# DENETİM RAPORU: cerengzell/is-bulma-simulasyonu

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Simülasyondaki rastgelelik, ekonometrik hayatta kalma analizlerinde standart olarak kullanılan Hızlandırılmış Başarısızlık Süresi (AFT) Log-Normal Dağılım Modeli'ne dayanmaktadır. Kod tabanında sırf grafik çizdirmek amacıyla üretilmiş kör bir rastgele gürültü (Math.random()) mekanizması bulunmamaktadır; her girdi çıktıya doğrudan matematiksel etki etmektedir.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Veri kaynağı, TÜİK Temmuz 2025 (2024 yılı verisi) Yükseköğretim İstihdam Göstergeleri'nden alınan baz değerlere dayanmaktadır. Bu baz veriler, kullanıcının arayüzden seçtiği bölüm girdisiyle `DEPARTMENTS` dizisinden eşleştirilir. Kullanıcının belirlediği GPA (not ortalaması) ve staj süresi girdileri, Baert et al. (2021) ve NACE Job Outlook 2021 literatüründen esinlenen sabit katsayılar (`coefGPA = -0.25`, `coefStaj = -0.04`, `academicRefMultiplier`) ile işlenerek AFT formülü üzerinden beklenen iş bulma süresine (`expectedTime`) dönüştürülür. Nihai çıktılar standart normal kümülatif dağılım fonksiyonu (Abramowitz and Stegun yaklaşımı kullanan `normalCDF` fonksiyonu) ile binde bir hassasiyetle hesaplanarak Chart.js çizgi grafiğine ve metinsel panellere aktarılır.

Kontrol Kaldıraçları: Kullanıcı; Mezun Olunan Bölüm (dropdown), Not Ortalaması (range slider: 1.00 - 4.00) ve Toplam Dış Staj / İş Tecrübesi (range slider: 0 - 24 ay) faktörlerini kontrol edebilmektedir. Bu kaldıraçlar doğrudan matematiksel modele girdi olarak verilmekte, her değişimde `updatePrediction` fonksiyonu tetiklenerek kümülatif işe yerleşme eğrisini ve beklenen süreleri gerçek zamanlı olarak dinamik biçimde güncellemektedir. Kontroller kozmetik değildir, simülasyonun amacına doğrudan hizmet eder.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Kod tamamen istemci taraflı (client-side) HTML, CSS ve saf JavaScript (Vanilla JS) mimarisiyle yazılmıştır. Kod tabanında localhost, 127.0.0.1 veya yerel makineye bağımlı mutlak dosya yolları bulunmamaktadır. Proje statik web barındırma yapısına tam uyumlu olduğundan GitHub Pages üzerinde herhangi bir teknoloji uyuşmazlığı olmadan sorunsuz şekilde çalışır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Ekonometrik Survival Analizi (AFT Log-Normal modeli) arka planda eksiksiz kurgulanmıştır. Model parametreleri gerçek akademik literatür ve resmi TÜİK verileriyle tutarlıdır. Yapay zeka kalıntısı boş kod bloğu veya işlevsiz fonksiyon bulunmamaktadır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Kullanıcıya sunulan tüm kaldıraçlar simülasyon senaryosuna ve amacına doğrudan etki eder. Katsayılar mantıklı tasarlanmıştır; GPA artışı ve staj süresinin uzaması, beklenen iş bulma süresini istatistiksel kurallara uygun olarak azaltır.

Eşik 3 (Veri Dışa Aktarımı): KALDI - Gerekçe: Tasarlanan simülasyonda kullanıcı girdileri ve model tarafından 1. aydan 24. aya kadar üretilen kümülatif ihtimal verileri (`probData`, `timeLabels`) yapılandırılmış bir formatta (CSV veya JSON olarak) yerel sisteme indirilmek üzere herhangi bir dışa aktarma (export) butonu veya fonksiyonu ile desteklenmemiştir. Veriler sadece grafik üzerinde görselleştirilmektedir.

NİHAİ DURUM: REDDEDİLDİ (NOT: 0)