---
gorev_13: 60
final_notu: 90
ogrenci_no: 2511317012
---
# DENETİM RAPORU: sudecukurtas/opt-ma

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Simülasyonda kullanılan Math.random() ifadeleri, deterministik formüllerin etrafında stokastik (rastgele) sapmaları simüle etmek, kurye rotalarındaki anlık değişimleri ve dinamik paket hareketlerini (parçacık modellemesi) kuyruk teorisine uygun şekilde canlandırmak amacıyla meşru bir simülasyon modeli çerçevesinde kullanılmıştır. Kullanıcı girdileri simülasyon çıktılarını doğrudan etkilemektedir.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Veri kaynağı olarak Türkiye'deki 11 büyük ilin gerçekçi nüfus ve coğrafi koordinat (lat/lng) verileri baz alınmıştır. Simülasyon motoru (tick fonksiyonu); sipariş akış hızı, il nüfus ağırlıkları ve filo kompozisyonu faktörlerini işleyerek anlık sipariş, SLA başarısı ve CO2 salınımı verilerini üretmektedir. Çıktılar dinamik bir HTML5 Canvas üzerinde parçacık animasyonlarıyla görselleştirilmekte, telemetri loglarına yazılmakta ve CSV formatında dışa aktarılabilmektedir.

Kontrol Kaldıraçları: Kullanıcı; genel trafik yoğunluğu, hava durumu (güneşli, yağmurlu, karlı), müşteri adreste yok oranı, sipariş akış hızı, illere göre aktif kurye dağıtımı ve filo kompozisyonu (motosiklet, panelvan, elektrikli araç oranları) gibi eyleme geçirilebilir kaldıraçları kontrol edebilmektedir. Bu parametrelerin değiştirilmesi simülasyonun SLA başarısını, teslimat sürelerini ve net CO2 salınımını matematiksel olarak doğrudan değiştirmektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Kod tamamen statik HTML, CSS ve saf JavaScript (Vanilla JS) ile yazılmıştır. Herhangi bir localhost bağımlılığı veya mutlak yerel dosya yolu içermemektedir. GitHub Pages mimarisine tam uyumludur ve statik sunucuda sorunsuz çalışmaktadır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: İllerin nüfus ağırlıkları sipariş üretim hızını doğrudan etkilemektedir. Hava durumu ve trafik yoğunluğu gibi çevresel faktörler SLA başarı oranına ve ortalama teslimat sürelerine mantıksal bir formülle (weatherPenalty vb.) yansıtılmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Sunulan slider, radio buton ve toggle kontrolleri simülasyonun amacına (lojistik dijital ikizi ve kontrol kulesi yönetimi) doğrudan hizmet eden, anlamlı kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: downloadCSV fonksiyonu aracılığıyla simülasyonun ürettiği il bazlı kurye, sipariş, SLA% ve CO2 verileri yapılandırılmış CSV formatında dışa aktarılabilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Üstlenilen Rol ve Konu Uygunluğu: Öğrenci, Lojistik Optimizasyon ve Veri Analitiği Departmanı rolünü üstlenerek Yönetim Kurulu Seviyesinde son derece profesyonel ve kurumsal bir stratejik rapor hazırlamıştır. Seçilen konu ve lojistik kontrol kulesi dijital ikiz simülasyonu üzerinden darboğaz tespiti yapılması, karar alıcılar için doğrudan problem çözücü ve eyleme geçirilebilir somut öneriler sunmaktadır. Anlatım ve Basitlik Düzeyi: Rapordaki anlatım dili, karmaşık lojistik algoritmalarını ve matematiksel modelleri (SLA hedef modeli, emisyon hesaplama modeli) bir yöneticinin hızla kavrayabileceği netlikte ve sadelikte açıklamaktadır. Sunulan operasyonel veri matrisi (tablo) ve metin içi KPI göstergeleri analizi basitleştirerek anlaşılırlığı en üst düzeye çıkarmıştır. Yapay Zeka İzleri ve Özensizlik: Metin baştan sona incelendiğinde, yapay zekanın üretebileceği basmakalıp dolgu paragraflarına veya jenerik başlıklara rastlanmamıştır. Öğrenci, AI çıktısı olabilecek yapıları tamamen kendi süzgecinden geçirerek şirkete ve konuya özgü, birbiriyle tutarlı mantıksal argümanlar örgüsü (İstanbul'daki 50 kuryelik eksiklik ile SLA çöküşü ve iş gücü kaybı arasındaki bağ gibi) oluşturmuştur. Rapor Dil ve Profesyonelliği: Rapor kurumsal üslup kurallarına tam olarak uymaktadır. Konu net bir şekilde tanımlanmış, "Şirket İçi / Yönetim Kurulu Seviyesi Stratejik Rapor" başlığıyla kurumsal bir hitap ve ciddiyetle açılmıştır. Metin içerisinde hiçbir emojiye yer verilmemiştir. Rapor, "Yönetim Onayına Sunulmuştur" ifadesiyle kurumsal bir saygı/kapanış diliyle sonlandırılmış ancak "Hazırlayan" ve kapanış kısımlarında departman/komite ismi verilirken öğrencinin kendi kişisel ad-soyadı metne eklenmemiştir.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporun kurumsal kimlik ve teslimat kuralları gereği, metnin başında veya sonunda öğrencinin kendi gerçek ad-soyadı açıkça yazılmalıdır. Raporda hazırlayan kişi olarak sadece "Lojistik Optimizasyon ve Veri Analitiği Departmanı" ve "Lojistik Analiz ve Planlama Komitesi" ibareleri kullanılmış, öğrencinin adı-soyadı yazılmamıştır. Bu durum "adını yazmayı unutma/eksiklik" kapsamında değerlendirilerek matris gereği hafif puan kırılmasına yol açmıştır.
    

NİHAİ FİNAL NOTU: 75 XP