---
gorev_13: 75
final_notu: 95
---
# DENETİM RAPORU: emin-emek / isi-stresi-simulasyonu (Öğrenci: Emin Emek)

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, veriyi kullanıcı tarafından manuel olarak ayarlanan arayüz kontrollerinden (slider ve input alanları) veya Open-Meteo API entegrasyonu aracılığıyla canlı meteorolojik kaynaklardan çekmektedir. Toplanan bu veriler, JavaScript tabanlı `calculateScientificModel` fonksiyonuna aktarılmaktadır. Fonksiyon içerisinde Mader ve ark. (2006) ile Li ve ark. (2019) gibi literatürde yer alan gerçek termodinamik ve fizyolojik formüller kullanılarak net ATHI (Ayarlanmış Sıcaklık Nem İndeksi), solunum hızı (RR), vücut/rumen sıcaklığı (RT), refah skoru ve süt verim kaybı hesaplanmaktadır. Hesaplanan veriler hem anlık gösterge paneline dinamik olarak yansıtılmakta hem de zaman serisi formatında bir veri dizisinde (`recordedData`) saklanarak CSV çıktısına dönüştürülmektedir.

Kontrol Kaldıraçları: Kullanıcı; Sıcaklık, Bağıl Nem, Doğal Rüzgar ve Güneş Radyasyonu gibi çevresel faktörleri; Hedef Süt Verimi, Canlı Ağırlık, Irk seçimi ve Laktasyon Dönemi gibi hayvansal faktörleri; Havalandırma Fanı (Adet/Hız), Duşlama Sistemi (Süre/Sıklık), Gölgelik Yüzdesi, Ahır Tipi, Doluluk Oranı ve Hayvan Yoğunluğu gibi yapısal/yönetimsel faktörleri kontrol edebilmektedir. Bu kaldıraçların tamamı arka plandaki matematiksel modeli doğrudan ve biyolojik gerçekçiliğe uygun olarak etkilemektedir; etkileri kozmetik değildir.

Localhost Kontrolü: GEÇTİ - Kod tabanında localhost, 127.0.0.1 veya herhangi bir yerel mutlak dosya yolu (C:/Users/... vb.) referansı bulunmamaktadır. Kullanılan tüm API ve CDN bağlantıları uzak sunucular üzerinden canlıda çalışabilecek şekilde yapılandırılmıştır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Simülasyon mantığı rastgele sayı üreteçlerine veya doğrusal sahte döngülere dayanmamaktadır. Tamamen hayvan besleme ve veteriner hekimlik literatüründeki deterministik formülleri temel alan, mekanik olarak son derece gerçekçi ve tutarlı bir bilimsel model uygulanmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan tüm kontrol elemanları simülasyonun çıktı parametrelerini anlık, dinamik ve mantıksal kısıtlar çerçevesinde değiştirebilme yeteneğine sahiptir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Üretilen zaman serisi verilerini UTF-8 BOM kodlamasıyla yapılandırılmış bir şekilde CSV formatında dışa aktaran ve indirme işlemini başarıyla başlatan çalışan bir JavaScript mekanizması mevcuttur.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Üstlenilen Rol ve Konu Uygunluğu: Öğrenci, İl Tarım ve Orman Müdürlüğü'ne hitap eden bir sektör uzmanı/danışman rolünü üstlenmiştir. Rapor, sadece akademik bir ödev mantığıyla yazılmamış, bölge hayvancılığını korumaya yönelik somut hibe, teşvik ve erken uyarı sistemi önerileri barındıran stratejik bir kamu teklifi olarak tasarlanmıştır. Bu açıdan karar alıcıya yaklaşım son derece başarılıdır.

Anlatım ve Basitlik Düzeyi: THI ve ATHI gibi karmaşık biyo-meteorolojik indeksler ve solunum hızı gibi fizyolojik parametreler, teknik bilgiye sahip olmayan bir yöneticinin bile rahatça anlayabileceği bir sadelikte açıklanmıştır. 5 farklı grafik ve karşılaştırmalı tabloların rapora entegrasyonu görselleştirme kalitesini artırmıştır. Ancak metin ile tablolar arasındaki veri tutarlılığında zafiyet bulunmaktadır.

Yapay Zeka İzleri ve Özensizlik: Metin genelinde yapay zekaya ait basmakalıp geçiş cümleleri temizlenmiş ve özgün bir rapor dili oluşturulmuştur. Ancak, simülasyon çıktılarının ekonomik analize dönüştürüldüğü aşamada tablolar arası veri aktarımı ve etiketlemede net bir özensizlik/koordinasyon hatası tespit edilmiştir.

rapor Dil ve Profesyonelliği: Kurumsal ve bürokratik üslup baştan sona korunmuştur. Uygun bir hitapla başlanmış, saygı ifadesiyle bitirilerek hazırlayan öğrencinin adı açıkça belirtilmiştir. Metin içerisinde hiçbir emoji kullanılmamıştır.

PUAN KIRILMA GEREKÇELERİ

- Yönetici özeti metninde 40 derece sıcaklıkta soğutma sistemi olmayan bir işletmede inek başına günlük 4-5 kg süt kaybı yaşandığı ifade edilmiştir. Ancak Tablo 1 (Senaryo Karşılaştırması) incelendiğinde, Soğutmasız senaryoda 40 derecedeki süt kaybı 6.71 kg olarak verilmiştir. Metin ile tablo arasındaki bu belirgin veri çelişkisi karar alıcı nezdinde raporun güvenilirliğini zedelemektedir.
    
- Tablo 2'de sunulan 100 başlık sürü için yıllık ekonomik kayıp analizinde, hesaplamaların hangi sıcaklık baz alınarak yapıldığı tablonun başlığında veya açıklamasında muğlak bırakılmıştır. Tablo 1'deki verilerle çapraz kontrol yapıldığında, Tablo 2'deki hesaplamaların 40 derece için değil, 38 derecedeki süt kayıpları (6.13 kg, 3.35 kg, 1.06 kg) üzerinden yürütüldüğü görülmektedir. Projeksiyon tablosunun eksik etiketlenmesi veri takibini zorlaştırmıştır.
    

NİHAİ FİNAL NOTU: 75 XP