# DENETİM RAPORU: plt0051ct-rgb / sosyal-medya-simulatoru

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, kullanıcının arayüzden girdiği takipçi sayısı, prodüksiyon kalitesi, kanca (hook) ve elde tutma (hold) oranlarını girdi olarak alır. Bu girdiler, paylaşım saatine bağlı trafik çarpanları ve hesap durumu kısıtlamalarıyla işlenerek her saat adımı (tick) için izlenme, izleme süresi ve etkileşim sayılarını hesaplar. Üretilen veriler "simData" dizisinde yapılandırılmış olarak biriktirilir, Chart.js entegrasyonu ile grafiklere aktarılır ve dışa aktarım için hazır bulundurulur.

Kontrol Kaldıraçları: Kullanıcı; prodüksiyon kalitesi, kanca oranı, elde tutma oranı, etkileşim oranı, hesap uyum skoru, paylaşım saati, takipçi sayısı, simülasyon süresi ve rastgele tohum (seed) değerini kontrol edebilmektedir. Bu kaldıraçlar simülasyonun akışını kozmetik olarak değil; algoritmik dağıtım havuzunu, shadow-ban sınırlarını ve saatlik izlenme çarpanlarını matematiksel formüllerle doğrudan değiştirmektedir.

Localhost Kontrolü: GEÇTİ - Kaynak kod içerisinde "http://localhost", "127.0.0.1" veya yerel bilgisayara ait mutlak dosya yolları (C:/Users/... vb.) bulunmamaktadır. CDN üzerinden Chart.js ve Google Fonts kütüphaneleri çağrılmıştır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: İzleyici davranışı, platform dokümantasyonlarına uygun şekilde bir huni akışı (izlenim -> kanca -> elde tutma) üzerinden Markov geçiş olasılıkları ile modellenmiştir. Rastgelelik unsuru ham Math.random() yerine, tekrarlanabilir analize izin veren "mulberry32" algoritmalı kontrollü sahte rastgele sayı üretecine (seeded PRNG) dayandırılmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan tüm slider ve input bileşenleri, simülasyonun amacına doğrudan hizmet eden ve çıktı verilerini (örneğin hesap sağlığı 50'nin altına düştüğünde dağıtımı yüzde 85 oranında kısıtlayan shadow-ban mekanizması gibi) dinamik olarak etkileyen anlamlı kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: downloadCSV fonksiyonu, simülasyonda oluşan her saatlik veriyi (gösterim, hook gecen, sonuna izleyen, begeni, yorum, paylasim sayısı, algoritma skoru vb.) virgülle ayrılmış nesne anahtarlarıyla yapılandırılmış bir CSV dosyası olarak dışa aktarabilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Üstlenilen Rol ve Konu Uygunluğu: Öğrenci, kurumsal sosyal medya stratejisinden sorumlu İletişim Direktörü veya Sosyal Medya Yöneticisi pozisyonlarını hedefleyerek son derece net, amaca yönelik ve problem çözücü bir bağlam inşa etmiştir. Üniversiteler veya belediyeler gibi kurumsal yapıların içerik üretim bütçelerini optimize etmeye yönelik, eyleme geçirilebilir somut stratejik teklifler sunmaktadır. Anlatım ve Basitlik Düzeyi: Simülasyonun arkasındaki matematiksel ve teknik arka plan (Markov geçiş modeli, sahte rastgele sayı üreteci), karar alıcının rahatça anlayabileceği "izleyici akış hunisi" benzetmesiyle basitleştirilerek aktarılmıştır. Rapor, kendi simülasyonundan elde ettiği kesin sayısal verilere (Örn: Senaryo 4'teki shadow-ban durumunda erişimin %85 kısıtlanarak izlenmenin 12.000'den 580'e düşmesi gibi) doğrudan ve güçlü atıflar yapmaktadır. Yapay Zeka İzleri ve Özensizlik: Prototip geliştirme aşamasında yapay zekadan yararlanıldığı dürüstçe rapor edilmiştir. Buna karşın, metin yapay zekanın ürettiği basmakalıp dolgu paragraflarından, jenerik yuvarlak ifadelerden tamamen arındırılmış; TikTok Newsroom ve Hootsuite gibi gerçek dünya verileriyle tamamen özgünleştirilmiştir. rapor Dil ve Profesyonelliği: Raporda kurumsal ciddiyeti bozacak hiçbir emojiye yer verilmemiş, konu ve kapsam net şekilde sınırlandırılmıştır. Öğrencinin adı, soyadı, numarası ve kurumsal bilgileri eksiksiz şekilde mevcuttur. Ancak rapor metni, kurumsal üslubun gerektirdiği resmi bir hitap/selamlama ifadesiyle başlamamakta ve kaynakça/kapanış bölümünde resmi bir saygı/iyi dilek kapanış ifadesi (Örn: "Saygılarımla", "Bilgilerinize arz ederim") barındırmamaktadır.

PUAN KIRILMA GEREKÇELERİ

- Raporun kurumsal yazışma ve profesyonel raporlama standartlarına uygun resmi bir hitap/selamlama cümlesiyle başlamaması ve metin bitişinde ad-soyad yer almasına rağmen geleneksel saygı/kapanış ifadesinin eksik bırakılması nedeniyle -5 puan kırılmıştır.
    

NİHAİ FİNAL NOTU: 75 XP