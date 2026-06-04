# DENETİM RAPORU: umutklcc/hvac-simu

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Sabit veya ham rastgele sayılar (Math.random()) yerine Burdur meteorolojik verilerini temel alan 24 saatlik gerçekçi bir sıcaklık döngüsü dizisi (burdur_sicaklik_dongusu) ve güneş ışınım faktörü matrisi kullanılmıştır. Çıktılar bu döngüsel veriler ile kullanıcı girdilerinin matematiksel kombinasyonuna dayanmaktadır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, statik olarak tanımlanmış 24 saatlik Burdur sıcaklık ve güneş ışınım verilerini girdi olarak alır. Kullanıcının arayüzden seçtiği bina alanı, yalıtım tipi (U-değeri), doluluk, cihaz yükü ve set sıcaklığı parametreleri TS 825 standartlarına uygun transmisyon ve infiltrasyon formülleriyle işlenir. Çıktı olarak anlık ısıl denge matrisi (kW), saatlik maliyetler (TL) ve karbon emisyonu hesaplanarak arayüze basılır ve dışa aktarılır.

Kontrol Kaldıraçları: Isıtma/soğutma kaynağı seçimi, U-Katsayısı (yalıtım tipi), net iklimlendirilen alan, personel kapasitesi, ekipman ısı yoğunluğu, hedef sıcaklık seti, işletme stratejisi (AI/Standart) ve ilk yatırım bütçesi kontrol edilebilmektedir. Bu kaldıraçlar "hvac_cost" ve "hesapla" fonksiyonları içindeki mühendislik denklemlerini doğrudan etkileyerek dinamik sonuçlar üretmektedir.

Localhost Kontrolü: GEÇTİ - Kod içerisinde herhangi bir yerel sunucu (localhost, 127.0.0.1) veya mutlak yerel dosya yolu referansına rastlanmamıştır. Dış bağlantı olarak sadece MGM resmi istatistik linkleri kullanılmıştır.

EŞİK DEĞERLENDİRMELERI

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: ASHRAE standartlarına uygun içsel kazanç, havalandırma yükü ve dış kabuk transmisyon kayıpları formülize edilmiştir. Sıcaklık ve strateji değişimine göre COP/EER değerlerinin dinamik olarak güncellenmesi mekanik gerçekçiliği doğrulamaktadır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Sunulan slider ve select elementleri bir tesis yöneticisinin enerji tasarrufu ve ROI analizi yapabilmesi için doğrudan anlamlı ve eyleme geçirilebilir parametrelerdir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Üretilen 24 saatlik detaylı makro mühendislik ve ısıl denge matrisi, "indirResmiExcel" fonksiyonu aracılığıyla yapılandırılmış Microsoft Excel XML formatında (.xls) dışa aktarılabilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Üstlenilen Rol ve Konu Uygunluğu: Öğrenci, veri bilimi öğrencisi kimliğiyle T.C. Enerji ve Tabii Kaynaklar Bakanlığı'na hitaben üst düzey bir fizibilite ve proje teklifi sunmuştur. Seçilen konu, kamu binalarında bütçe şeffaflığı sağlama ve enerji maliyetlerini düşürme noktasında karar alıcılar için doğrudan problem çözücü ve eyleme geçirilebilir bir nitelik taşımaktadır. Anlatım ve Basitlik Düzeyi: Karmaşık termodinamik ve yazılım süreçleri (Predictive Set-Back, dinamik EER, termal atalet) bir bürokratın veya yöneticinin en rahat anlayabileceği şekilde, doğrudan finansal ve operasyonel çıktılara indirgenerek sadeleştirilmiştir. "Mühendislik kW yükü sabit kalırken finansal TL faturasının düşürülebilmesi" ifadesi bu sadeliğin ve amaca yönelik anlatımın en güçlü kanıtıdır. Yapay Zeka İzleri ve Özensizlik: Metinde yapay zekanın ürettiği basmakalıp dolgu paragraflarına veya jenerik "buraya analiz yazılacak" tarzı düzeltilmemiş ifadelere rastlanmamıştır. Proje başlığından sonuç ve arz bölümlerine kadar tutarlı, yapılandırılmış ve süzgeçten geçirilmiş özgün bir dil hakimdir. Rapor Dil ve Profesyonelliği: Rapor kurumsal ve resmi bir hitap diliyle kurgulanmış, Bakanlık makamına uygun saygı ifadeleri arz edilerek tamamlanmıştır. Metin içerisinde hiçbir şekilde ciddiyeti bozan emoji kullanımına yer verilmemiştir. Raporun sonunda öğrencinin adı ve soyadı (Emin Umut KILIÇ) net bir şekilde belirtilerek kimlik doğrulanabilirliği tam olarak sağlanmıştır.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

Kusursuz teslimat, puan kırılmamıştır.

Yazılan simülasyondaki değişkenlere (Burdur meteorolojik verileri, 3°C - 5°C gece sıcaklıkları, Chiller EER = 4.8 verimlilik katsayısı, %27,6 şebeke çekim azaltımı ve el yazısıyla girilen küsuratlı bütçe girdileri) raporda doğrudan ve spesifik atıflar yapılarak simülasyon-rapor entegrasyonu mükemmel bir şekilde sağlanmıştır.

NİHAİ FİNAL NOTU: 80 XP