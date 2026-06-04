# DENETİM RAPORU: genesis-risk-terminali / Azra Özçelik

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Simülasyonda kullanılan rastgele sayı üretimi, finans mühendisliği standartlarına dayanan Geometrik Brown Hareketi ve Monte Carlo projeksiyon yönteminin (Stokastik Wiener Süreci) bir parçasıdır. Kullanıcı girdileri simülasyon çıktılarını doğrudan matematiksel olarak etkilemektedir.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, ilk 60 gün için kod içerisine statik olarak eklenmiş olan 2024 yılı Nisan ve Haziran ayları arasındaki gerçek Bitcoin piyasa kapanış fiyatlarından beslenmektedir. Gelecek 40 günlük kriz projeksiyonlarında ise bu verilerin bittiği noktadan itibaren kullanıcı girdilerine dayalı bir stokastik formül çalıştırılmaktadır. Elde edilen fiyat trendleri, aktif ajan tasfiyeleri, panik endeksi ve tasfiye şiddeti verileri Chart.js grafik motoruna ve dinamik bir canlı veri tablosuna aktarılmaktadır.

Kontrol Kaldıraçları: Kullanıcı; Volatilite Çarpanı (v), Balina Satış Baskısı (w), Piyasa Derinliği (d) ve Başlangıç Aktif Ajanlar parametrelerini arayüzde yer alan slider bileşenleri aracılığıyla anlık olarak değiştirebilmektedir. Bu faktörler fiyat yönelimini (drift) ve stokastik şok (Wiener süreci) miktarını doğrudan etkileyerek simülasyonun çıktı mantığını dinamik olarak değiştirmektedir ve kozmetik değildir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Kod tabanında localhost, yerel sistem yolları veya harici yerel dosya bağımlılıkları barındıran hiçbir kod satırı bulunmamaktadır. Proje tamamen HTML, CSS ve istemci taraflı JavaScript teknolojileriyle kurgulandığı için, statik bir barındırma hizmeti olan GitHub Pages üzerinde teknoloji uyuşmazlığı yaşamadan sorunsuz şekilde çalışmaktadır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Rastgele veri üreten sahte scriptler yerine ilk 60 gün boyunca %100 gerçek Bitcoin geçmiş verileri kullanılmış, gelecek projeksiyonu için ise kantitatif finans standartlarında kabul gören Monte Carlo ve Geometrik Brown Hareketi algoritmaları entegre edilmiştir.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Sunulan 4 ana parametre kontrolü, borsanın risk yönetim kurulunun stratejik karar alma süreçlerine hizmet eden, anlamlı, piyasaya doğrudan matematiksel etkisi olan ve eyleme geçirilebilir kaldıraçları temsil etmektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Simülasyon sonucunda üretilen 100 günlük veriler, raporlama ve analiz amacıyla kullanılmaya uygun, yapılandırılmış bir CSV formatında dışa aktarılabilmekte ve tarayıcı üzerinden indirilebilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): GEÇTİ - Rapor, muhatabı olan Kripto Varlık Borsası Risk Yönetim Kurulu'nun kurumsal yetki sınırları dahilinde uygulanabilecek, son derece somut, etik ve gerçekçi bir bürokratik eylem planı sunmaktadır. Matematiksel girdileri aynen tekrarlayan bir kısır döngü (tautoloji) veya sığ jenerik tablolar barındırmamaktadır. Aksine, simülasyondan elde edilen ampirik risk metriklerinin canlı emir defterlerine (Order Book) entegre edilmesini ve kritik eşiklerde kaldıraçlı işlemleri durduracak bir "Akıllı Devre Kesici" (Smart Circuit Breaker) sisteminin inşa edilmesini önermektedir. Ayrıca kullanıcı tabanında finansal okuryazarlığı artırmak üzere teknik sözlük ve arşiv modüllerinin ücretsiz kullanıma açılması gibi stratejik hamleler içermektedir.

Çözümü Satabilme ve İkna Kabiliyeti: Öğrenci girdiği veri bilimi öğrencisi ve FinTech uzman adayı rolünü kurumsal protokollere tam uyumlu şekilde sürdürmüştür. Likidite krizi gibi karmaşık bir finansal problemi "su havuzu ve büyük kaya" analojisiyle basitleştirerek karar alıcılar için konuyu son derece anlaşılır ve problem çözücü bir dille sunmuştur. Projeyi borsa yönetimine başarılı bir şekilde "satabilmiş", kariyer ve iş birliği teklifini kurumsal fayda odaklı bir eylem planına bağlayarak yüksek ikna kabiliyeti sergilemiştir.

Veri Temelli Kanıtlar ve Simülasyon Atıfları: Rapor, genel geçer teorik bilgilerle sınırlı kalmamış, öğrencinin kendi geliştirdiği simülatörün çıktılarına doğrudan ve spesifik ampirik atıflar yapmıştır. Raporda yer alan "Piyasa Derinliğimiz 40 birimin altına düştüğünde ve aynı anda dışarıdan 3.5 şiddetinin üzerinde bir Balina Satış Baskısı geldiğinde, borsamızda durdurulamaz bir tasfiye zinciri başlamaktadır" ifadesi, simülasyondaki sayısal verilere ve stres testi parametrelerine doğrudan atıfta bulunulduğunun net bir kanıtıdır.

Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Yapay zekadan alınmış ham, basmakalıp dolgu paragrafları veya temizlenmemiş jenerik yorum satırları raporda bulunmamaktadır. Rapor net ve kurumsal bir hitap yapısıyla başlamakta, saygın bir iyi dilek ifadesiyle bitmekte ve öğrencinin tam adı-soyadı (Azra Özçelik) metinde açıkça doğrulanabilmektedir. Rapor genelinde kurumsal kurallara aykırı hiçbir laubali ifade veya emoji kullanılmamıştır.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

Kusursuz teslimat, puan kırılmamıştır.

NİHAİ FİNAL NOTU: 80 XP