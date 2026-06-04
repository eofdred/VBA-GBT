# DENETİM RAPORU: cerengzell/is-bulma-simulasyonu / Ceren Güzel

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Projedeki rastgelelik katsayısı (noiseSigma = 0.35), ekonometri literatüründe kabul gören Hızlandırılmış Başarısızlık Süresi (AFT) Log-Normal Dağılım Modeli kapsamında meşru ve bilimsel bir stokastik belirsizliği temsil etmektedir. Matematiksel model, Abramowitz ve Stegun yaklaşımı kullanan bir standart normal kümülatif dağılım fonksiyonuna (normalCDF) dayanmakta olup, kullanıcı girdileri çıktıyı doğrudan ve deterministik bir mantıkla etkilemektedir. Sırf grafik çizdirmek amacıyla üretilmiş ham veya kontrolsüz bir rastgelelik bulunmamaktadır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Veri kaynağı, TÜİK Temmuz 2025 güncellemesi tabanlı 2024 yılı Yükseköğretim İstihdam Göstergeleridir. Seçilen bölümün baz süresi (muBase) girdi olarak alınır; ardından kullanıcının belirlediği GPA ve staj süresi katsayılar üzerinden işlenerek log-normal dağılım parametrelerine dönüştürülür. Çıktı olarak beklenen iş bulma süresi, %95 güven aralığı ve Chart.js vasıtasıyla 24 aylık kümülatif işe yerleşme ihtimal eğrisi üretilir.

Kontrol Kaldıraçları: Kullanıcı; "Mezun Olunan Bölüm" (dropdown), "Not Ortalaması" (slider) ve "Toplam Dış Staj Süresi" (slider) değişkenlerini kontrol edebilmektedir. Bu kaldıraçlar kozmetik değildir; AFT formülündeki katsayıları doğrudan değiştirerek hem beklenen süreyi hem de kümülatif olasılık eğrisini dinamik olarak yeniden hesaplar. Staj süresinin 0 olması veya 0'dan büyük olması durumunda modele akademik literatür referanslı (Baert et al. ve NACE) farklı çarpanlar uygulanmaktadır.

Localhost Kontrolü: GEÇTİ - Kod tabanında localhost, 127.0.0.1 veya yerel mutlak dosya yollarına ait herhangi bir referans bulunmamaktadır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: TÜİK resmi verileri ve hakemli literatür bulguları, log-normal AFT hayatta kalma analizi (survival analysis) modeliyle başarılı bir şekilde formüle edilmiştir.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Sisteme entegre edilen üç temel girdi, öğrenci istihdam edilebilirliği senaryosuna doğrudan hizmet eden, anlamlı ve çıktı dağılımını doğrudan manipüle eden eyleme geçirilebilir kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): KALDI - Gerekçe: Projenin kaynak kodları ve arayüz yapısı incelendiğinde, simülasyon çıktılarının veya üretilen kümülatif olasılık verilerinin analiz amacıyla dışa aktarılmasını sağlayan herhangi bir veri dışa aktarım mekanizması (CSV, JSON butonu veya fonksiyonu) kurgulanmamıştır.

NİHAİ DURUM: REDDEDİLDİ (NOT: 0)