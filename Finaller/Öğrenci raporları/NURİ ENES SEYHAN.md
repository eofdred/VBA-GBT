---
gorev_13: 75
final_notu: 90
ogrenci_no: 2511317020
---
# DENETİM RAPORU: seyhannurienes-afk

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, kullanıcının arayüzden sağladığı günlük uyku, haftalık sosyal aktivite saati, çalışma stratejisi, yarı zamanlı iş saati ve günlük kafein miktarı gibi parametrelerden beslenmektedir. Bu girdiler zaman döngüsü içerisinde kümülatif yorgunluk, anlık motivasyon ve verimlilik gibi içsel stok değişkenlerini Euler yöntemiyle (dt=1 gün) beslemekte ve değiştirmektedir. Elde edilen veriler ders bazlı öğrenme katsayıları ve sınav notu algoritmaları üzerinden işlenerek mezuniyet GPA değerine ve kümülatif tükenmişlik oranlarına dönüştürülmektedir. Çıktılar Plotly.js kütüphanesi aracılığıyla grafiksel olarak görselleştirilmekte ve eş zamanlı olarak senaryo bazlı bir veri tablosunda yapılandırılarak CSV formatında dışa aktarıma hazır hale getirilmektedir.

Kontrol Kaldıraçları: Kullanıcı; uyku süresi, sosyal aktivite, çalışma stratejisi gecikmesi, yarı zamanlı iş yükü ve kafein alımı gibi sistem girdilerini slider öğeleri üzerinden dinamik olarak kontrol edebilmektedir. Ayrıca ders planlayıcı alanında derslerin seçimi, soru sayısı ve konu zorluğu ayarlanabilmektedir. Bu kaldıraçlar kozmetik değildir; girilen değerler simülasyondaki ders çalışma sürelerini, ders verimliliğini ve kümülatif yorgunluk artış/azalış katsayılarını matematiksel fonksiyonlar üzerinden doğrudan etkilemektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Kod tabanında localhost, 127.0.0.1 veya kullanıcı bilgisayarına bağımlı mutlak dosya yolları bulunmamaktadır. Uygulama tamamen istemci taraflı (client-side) çalışan statik HTML, CSS ve JavaScript teknolojileriyle kurgulanmıştır. Üçüncü parti grafik kütüphanesi harici bir CDN bağlantısı üzerinden güvenli bir şekilde çekilmektedir. Herhangi bir sunucu taraflı dinamik dil (Python, PHP vb.) uyuşmazlığı bulunmadığı için GitHub Pages üzerinde statik olarak sorunsuz bir şekilde barındırılabilir ve kilitlenme yaşamadan canlıda çalıştırılabilir.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Model, akademik performans ve tükenmişlik dengesini zamana bağlı diferansiyel denklemlere dayalı birikim mantığıyla gerçekçi bir şekilde formüle etmiştir. Sınav notlarındaki rastgele varyasyonlar için Box-Muller dönüşümü yöntemiyle çalışan bir normal dağıtım gürültü fonksiyonu (randomNormal) eklenmiştir. Bu durum bilimsel temelli meşru bir stokastik simülasyona işaret etmektedir ve sahte veri manipülasyonu içermemektedir. Kodda işlevsiz bırakılmış AI yorum satırı veya boş fonksiyon bulunmamaktadır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan tüm giriş parametreleri ve ders planlayıcı bileşenleri simülasyonun amacına doğrudan hizmet eden anlamlı kaldıraçlardır. Bu değerlerin değiştirilmesi, 4 yıllık akademik takvim boyunca kümülatif yorgunluk limitlerini ve başarı olasılıklarını dinamik ve mantıklı bir biçimde manipüle etmektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Sistem, hem manuel eklenen senaryoları hem de otomatik üretilen 100 farklı rastgele senaryoya ait verileri yapılandırılmış bir matris üzerinde toplamakta ve downloadMasterCSV fonksiyonu ile CSV formatında dışa aktarabilmektedir. Çıktı oluşturulurken Türkçe karakterlerin Excel üzerinde bozulmaması amacıyla veri setinin başına BOM ön eki düzgün bir şekilde yerleştirilmiştir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Üstlenilen Rol ve Konu Uygunluğu: Öğrenci, akademik performans yönetimi üzerine "Veri Destekli Öğrenci Yaşam Rehberi" hazırlayarak bir uzman/danışman rolü üstlenmiştir. Ele alınan konu, zaman yönetimi ve tükenmişlik analizi açısından karar alıcılar için eyleme geçirilebilir somut öneriler sunmaktadır. Ancak raporun hitap hedefi doğrudan bir kurumsal yönetici veya üst merci yerine "Sevgili Öğrenci" şeklinde son kullanıcıya yöneliktir. Bu durum projenin bir karar alıcıya "satılması" ve ikna edilmesi noktasında hafif bir rol sapmasına neden olmuştur.

Anlatım ve Basitlik Düzeyi: Metin, sistem dinamiği ve Euler entegrasyonu gibi teknik altyapıları son derece sade ve anlaşılır bir dille, adeta herkesin kavrayabileceği bir düzeyde açıklamaktadır. Raporda yer alan grafik türlerine (Bar Chart, Line Chart, Boxplot, Heatmap) ve bu grafiklerdeki spesifik verilere (%61.9 tükenmişlik, %70 kritik hata payı, -1.00 kusursuz ters korelasyon vb.) yapılan doğrudan atıflar son derece güçlü, net ve kanıta dayalıdır.

Yapay Zeka İzleri ve Özensizlik: Öğrenci simülasyon çıktılarını rapora başarıyla entegre etmiş olsa da yapay zekanın sıklıkla ürettiği bazı basmakalıp jenerik dolgu cümlelerini ve robotik geçiş ifadelerini tamamen temizlememiştir. Girişteki "Üniversite hayatı sadece ders kitaplarından ibaret değildir..." ifadesi ve "ters orantılı bir vals yaptığını" gibi edebi/jenerik AI kalıpları metinde ham bırakılmıştır.

rapor Dil ve Profesyonelliği: Raporun konusu net, kurumsal kurallara uygun biçimde emoji barındırmayan temiz bir dille yazılmıştır. Saygı ve iyi dilek ifadesiyle sonlandırılmış olup raporun en altında öğrencinin tam adı ve soyadı (Nuri Enes Seyhan) net bir şekilde belirtilmiştir. Hitap şeklinin bir yöneticiye yönelik olmaması dışında profesyonel format kurallarına tamamen uyulmuştur.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporun hitap ve satış dili, kurumsal bir yöneticiyi veya karar alıcıyı ikna etmek üzere kurgulanmak yerine doğrudan son kullanıcıya (öğrenciye) yönelik bir rehber/broşür formatında hazırlanmıştır. Bu durum karar alıcıya yaklaşım ve çözüm satabilme kriterinden puan kırılmasına sebep olmuştur.
    
- Metnin belirli bölümlerinde yapay zekanın jenerik ve basmakalıp dolgu cümleleri (Örn: "üniversite hayatı sadece ders kitaplarından ibaret değildir", "ters orantılı bir vals") süzgeçten geçirilmeden doğrudan kullanılmıştır.
    

NİHAİ FİNAL NOTU: 75 XP