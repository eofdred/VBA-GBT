---
gorev_13: 75
final_notu: 85
---
DENETİM RAPORU: cerengzell/is-bulma-simulasyonu / Ceren Betül Gözel

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon temel verilerini TÜİK 2024 Yükseköğretim İstihdam Göstergeleri (Temmuz 2025 güncellemesi), Baert et al. (2021) ve NACE Job Outlook 2021 akademik literatüründen almaktadır. Kullanıcı girdileri, Hızlandırılmış Başarısızlık Süresi (AFT) Log-Normal Dağılım Modeli ve Abramowitz & Stegun yaklaşımı kullanan bir kümülatif normal dağılım fonksiyonu (normalCDF) üzerinden işlenmektedir. Hesaplanan veriler nihai olarak nokta tahmin süresi, yüzde 95 güven aralığı ve 24 aylık kümülatif olasılık serisi halinde arayüze ve dışa aktarım fonksiyonlarına iletilmektedir.

Kontrol Kaldıraçları: Kullanıcı; Mezun Olunan Bölüm (17 farklı lisans alanı), Not Ortalaması (GPA: 1.00 - 4.00 arası sürgü) ve Toplam Dış Staj / İş Tecrübesi (0 - 24 ay arası sürgü) faktörlerini kontrol edebilmektedir. Bu faktörler model içindeki akademik referans çarpanlarını ve log-normal mu parametresini matematiksel olarak doğrudan değiştirmektedir. Değişimler çıktı sürelerini ve kümülatif işe yerleşme eğrisini dinamik, gerçekçi ve anlamlı bir şekilde etkilediği için kontroller kozmetik değildir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Web arayüzü saf HTML5, CSS3 ve istemci taraflı JavaScript (vanilla JS) kullanmaktadır; kod tabanında localhost, 127.0.0.1 veya yerel sistem mutlak yollarına bağımlılık bulunmamaktadır. Bu sayede uygulama GitHub Pages üzerinde statik olarak sorunsuz şekilde barındırılabilmektedir. Depoda bulunan Python tabanlı "rapor_olustur.py" dosyası ise web uygulamasının çalışması için bir backend bağımlılığı oluşturmamakta, yerel ortamda DOCX raporu derlemek için kullanılan bağımsız bir akademik araç işlevi görmektedir.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Simülasyon, ekonometri literatüründe kabul gören ve sağa çarpık istihdam sürelerini modellemeye uygun olan AFT Log-Normal altyapısına yapılandırılmıştır. Grafik çizdirmek amacıyla sahte veya kontrolsüz rastgele sayılar (Math.random) kullanılmamış, tamamen meşru istatistiksel dağılım formülleri işletilmiştir.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Sunulan arayüz kontrolleri (bölüm seçimi, GPA ve staj süresi), mezun istihdam olasılıklarını doğrudan etkileyen eyleme geçirilebilir kaldıraçlardır. Kontroller amaca hizmet etmekte olup simülasyon çıktıları üzerinde doğrusal olmayan istatistiksel varyasyonlar üretmektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: app.js dosyası içerisinde yer alan exportCSV ve exportJSON fonksiyonları; girdi parametrelerini, model katsayılarını ve 24 aylık kümülatif olasılık serisini yapılandırılmış formatlarda dışa aktarabilmektedir. CSV aktarımında Excel uyumluluğu için UTF-8 BOM (\uFEFF) yapısı da doğru şekilde kurulmuştur.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): GEÇTİ - Raporda ampirik sonuçlar, öngörüler ve net bir stratejik vizyon sunulmuştur. Üniversite kariyer merkezleri, yükseköğretim kurumları, İK platformları ve eğitim politikası yapıcıları için eyleme geçirilebilir, mantıklı ve kurumsal yetki sınırlarına uygun bir çerçeve çizilmiştir. Model kendi kendini doğrulayan bir döngü (tautoloji) içermemekte; staj tecrübesi ve akademik başarı gibi somut ve yönetilebilir kaldıraçların iş piyasasındaki etkilerini rasyonel bir eylem planıyla analiz etmektedir.

Çözümü Satabilme ve İkna Kabiliyeti: Öğrenci, geliştirdiği projeyi sadece teorik veya teknik bir ödev olarak bırakmamış, kurumsal bir iş birliği teklifi (MezunScope) formatında karar alıcıya başarılı bir şekilde sunmuştur. Kariyer danışmanlığı ekosistemindeki somut değer önerileri ve platformun karar destek aracı olma niteliği net bir dille ifade edilmiş, problem çözücü ve ikna edici bir satış dili yakalanmıştır.

Veri Temelli Kanıtlar ve Simülasyon Atıfları: Raporda, geliştirilen simülasyonun ürettiği ampirik verilere, tablolara ve grafiklere doğrudan ve güçlü atıflar yapılmıştır. Güçlü, orta ve zayıf mezun profillerinin beklenen iş bulma süreleri (6.4 ay, 10.5 ay, 20.5 ay) ile bunlara ait yüzde 95 güven aralığı değerleri ve kümülatif olasılık eğrisindeki spesifik oranlar (6. ve 12. ay verileri) somut kanıt olarak metne yansıtılmıştır.

Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Yapay zeka çıktılarının ham bırakılmadığı, içerikteki teknik ve ekonometrik terminolojinin (AFT Log-Normal, Abramowitz ve Stegun yaklaşımı vb.) öğrencinin kendi süzgecinden geçirilerek rapora entegre edildiği görülmektedir. Raporun konusu net olup, öğrencinin adı, soyadı, unvanı, teslim tarihi ve alıcı bilgisi tam ve profesyonel bir kurumsal yazışma düzeninde sunulmuştur. Ancak rapor genelinde akademik ve kurumsal üsluba tam olarak uymayan yoğun bir görsel simge kullanımı mevcuttur.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

Rapor metninde (bölüm başlıklarında, profil tanımlamalarında, bilgi kutularında ve vurgularda) yoğun şekilde emoji kullanılması, resmi kurumsal raporlama ve akademik sunum standartlarına uymamaktadır. Bu biçimsel ve format düzeyindeki eksiklik nedeniyle taban puandan 5 puan kırılmıştır.

NİHAİ FİNAL NOTU: 75 XP