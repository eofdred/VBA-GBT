DENETİM RAPORU: aykuutt / calfcare-sim (Öğrenci: Aykut)

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Yapılan incelemede, kullanılan `Math.random()` fonksiyonunun kontrolsüz sahte veri üretmek için değil; bakıcının yorgunluk seviyesine bağlı olarak gelişen insan hatası olasılığını (`P(hata) = Yorgunluk * 0.4`) stokastik bir model çerçevesinde simüle etmek için meşru bir şekilde kullanıldığı tespit edilmiştir.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, başlangıç aşamasında Open-Meteo API üzerinden Burdur iline ait gerçek zamanlı sıcaklık ve bağıl nem verilerini çekmektedir. Bu çevresel veriler, zaman döngüsü içindeki sinüs dalgalanmaları ve seçilen ahır tipi çarpanları ile işlenerek dinamik bir çevre ısısı oluşturur. Buzağı (CalfAgent) ve Bakıcı (WorkerAgent) otonom etmenleri, bu çevre verileri ve kullanıcı girdileri doğrultusunda her saat başı (`tick()`) durum güncellemesi yaşar. Elde edilen anlık veriler Chart.js ile grafikleştirilir ve HTML tablosunda yapılandırılmış özet satırlarına dönüştürülerek CSV formatında dışa aktarılır.

Kontrol Kaldıraçları: Kullanıcı; Ahır Tipi, Buzağı Irkı, Başlangıç Bütçesi, Bakıcı Sayısı, Havalandırma Gücü, Başlangıç Hijyen Skoru ve Kolostrum Verilme Saeti gibi doğrudan simülasyonun amacına hizmet eden anlamlı kaldıraçları kontrol edebilmektedir. Bu parametreler sistem davranışını doğrudan etkiler. Örneğin, seçilen ırkın genetik tolerans eşiği (Angus 5°C, Simental 8°C, Holstein 12°C) ile dinamik çevre sıcaklığı kıyaslanarak "Termal Şok" mekanizması tetiklenmekte ve bu durum doğrudan buzağının sağlık skoruna eksi yazmaktadır.

Localhost Kontrolü: KALDI - `generate_report.py` isimli raporlama bileşeninde, yerel bilgisayara ait mutlak dosya yolu (`C:\Users\Lenovo\.gemini\antigravity\brain\...`) kullanılarak grafik ekleme kurgusu yapılmıştır. Bu durum, projenin taşınabilirliğini engellemekte ve yerel dosya yolu referansı kısıtlamasına takılmaktadır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Literatürdeki "One Welfare" ve buzağı refahı ilkelerine uygun olarak geliştirilen C.O.R.E. modeli, amonyak-nem ilişkisi (Zatürre/Pnömoni riski için nem %80'i aşınca hasarın ikiye katlanması) ve kolostrum zamanlamasının pasif bağışıklık (IgG) üzerindeki etkilerini matematiksel bir korelasyonla gerçekçi bir şekilde işletmektedir.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan tüm kontroller (slider ve select elementleri) simülasyon çıktısını, bütçe erime hızını ve ölüm/başarı senaryolarını doğrudan etkileyen eyleme geçirilebilir kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Simülasyon sonuçları, veri analizine ve akademik raporlamaya uygun şekilde yapılandırılmış virgülle ayrılmış değerler (CSV) formatında başarılı bir şekilde dışa aktarılabilmektedir.

NİHAİ DURUM: REDDEDİLDİ (NOT: 0)

Gerekçe: Projenin genel kod mimarisi, etmen tabanlı kurgusu ve biyolojik gerçekçilik seviyesi oldukça yüksek ve başarılı olmasına rağmen; dağıtım ve raporlama kodlarında yer alan yerel mutlak dosya yolu (C:/Users/...) kullanımı nedeniyle localhost/yerel yol kırmızı çizgisi aşılamamış ve proje doğrudan elenmiştir.