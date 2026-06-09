---
gorev_13: 80
final_notu: 100
ogrenci_no: 2511317011
---
# DENETİM RAPORU: sema788/e-spor-lol / Sema (Öğrenci Kullanıcı Adı: sema788)

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, Oracle's Elixir, Leaguepedia ve Riot Games Esports API gibi platformlardan derlenen gerçek 2026 League of Legends profesyonel oyuncu istatistiklerini (KDA, CS/dak, DPM, Kill Katılımı, Kazanma Oranı) temel almaktadır. Bu ham veriler JavaScript kaynak kodundaki sabit veri yapısında (PL nesnesi) saklanmaktadır. Kullanıcı girdileri ve literatür tabanlı yaş eğrisi çarpanları işlenerek 2027–2029 yılları için performans projeksiyon verileri üretilmekte, arayüzdeki tabloya aktarılmakta ve Chart.js kütüphanesi vasıtasıyla grafikleştirilmektedir.

Kontrol Kaldıraçları: Kullanıcı, simülasyon çıktılarını doğrudan etkileyen dört ana kaldıraç üzerinde kontrol sahibidir: "Meta uyum yeteneği", "Antrenman yoğunluğu", "Fiziksel & mental form" ve "Takım sinerji skoru". Bu girdiler 'fm()' fonksiyonunda belirli ağırlıklarla işlenerek (%30 meta, %28 antrenman, %22 form, %20 sinerji) tek bir faktör çarpanına dönüştürülmekte ve 'go()' fonksiyonu aracılığıyla tüm gelecek sezon tahminlerini dinamik ve matematiksel olarak değiştirmektedir; girdiler kozmetik değildir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Proje tamamen istemci taraflı web teknolojileriyle (Vanilla HTML, CSS ve JavaScript) geliştirilmiştir. Kod tabanında localhost, 127.0.0.1 veya yerel bilgisayara ait mutlak dosya yolları bulunmamaktadır. Statik bir yapıya sahip olduğundan GitHub Pages üzerinde herhangi bir teknoloji uyuşmazlığı olmadan canlı olarak çalışabilmektedir.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Tahmin mekanizması kontrolsüz rastgele gürültüye (Math.random) değil; e-spor oyuncularının yaş aralıklarına göre performans değişimlerini modelleyen bilimsel bir yayına (Pizzo et al. 2023) dayalı deterministik yaş eğrisi çarpanlarına ve kullanıcı girdilerine bağlı mantıksal bir formüle dayandırılmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Sunulan 4 adet kaydırıcı kontrolü, e-spor performansını etkileyen gerçekçi parametreleri temsil etmekte ve simülasyonun amacına doğrudan hizmet ederek sonuç tablolarını ve grafiklerini anlık olarak güncellemektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Kod yapısında yer alan 'exportOne()' ve 'exportAll()' fonksiyonları, üretilen tüm simülasyon verilerini başlık etiketleriyle birlikte virgülle ayrılmış ve tırnak içine alınmış temiz bir CSV formatına dönüştürerek tarayıcı üzerinden indirilebilmesini sağlamaktadır.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# # FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

## GENEL ANALİZ

- **Üstlenilen Rol ve Konu Uygunluğu:** Sponsor şirket pazarlama müdürünü hedefleyen "E-Spor Sponsorluk Kararlarında Veri Odaklı Oyuncu Seçimi" konusu, bir karar alıcı için doğrudan finansal riskleri azaltan ve bütçe optimizasyonu sağlayan mükemmel bir problem çözme aracıdır. Öğrencinin kurumsal perspektifi benimseme ve çözümü eyleme geçirilebilir somut bir bütçe teklifine dönüştürme başarısı (6.1 Senaryosu) takdir edilmiştir.
    
- **Anlatım ve Basitlik Düzeyi:** Karmaşık e-spor ve League of Legends teknik terimleri ile oyun içi pozisyonları, geleneksel spor analojileriyle (stoper, 10 numara, şutör vb.) desteklenerek teknik bilgiye sahip olmayan bir yöneticinin bile rahatça anlayabileceği bir sadelikte aktarılmıştır. Tablo yapıları ve senaryo karşılaştırmaları rapor kalitesini artırmıştır.
    
- **Yapay Zeka İzleri ve Özensizlik:** Metin, yapay zekanın sıkça ürettiği jenerik dolgu paragraflarından ve basmakalıp geçiş ifadelerinden tamamen arındırılmıştır. Akademik referanslar (Pizzo et al. 2023, Bányai et al. 2019) simülasyonun yaş eğrisi ve faktör ağırlıkları ile mantıksal bir bütünlük içinde harmanlanmıştır.
    
- **Rapor Dil ve Profesyonelliği:** Kurumsal ve akademik üsluba tamamen uygundur. Net bir konu başlığıyla açılış yapılmış, hedef kitleye uygun hitap dili korunmuş, metinde hiçbir emoji kullanılmamış ve kapanış profesyonel bir saygı ifadesiyle öğrencinin tam adı-soyadı belirtilerek tamamlanmıştır.
    

## PUAN KIRILMA GEREKÇELERİ / RED DETAYI

Kusursuz teslimat, puan kırılmamıştır.

## NİHAİ FİNAL NOTU: 80 XP