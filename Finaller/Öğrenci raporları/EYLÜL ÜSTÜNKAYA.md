DENETİM RAPORU: ustunkayaeylul72/trafik_kazalari / Eylül ÜSTÜNKAYA

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YÜKSEK

Sahte Veri/Manipülasyon Tespiti: EVET

Hile Kanıtı: index.html ve rapor_olustur.py dosyalarında yer alan simülasyon mantığı incelendiğinde, 2024-2035 yılları arası gelecek projeksiyonları hesaplanırken grafik_projeksiyon.png çıktısında ölümlerin aniden sıfır seviyesine düştüğü görülmektedir. Bunun sebebi projeksiyonHesapla fonksiyonundaki formüldür: vmt katsayısı hesaplanırken 2023 yılı taban alınarak "3183 * Math.pow(1 + f.vmt / 100, yil - 2023)" formülü kurulmuştur. Ancak nihai ölüm sayısı (olu) hesaplanırken "(oran * vmt) / 100" formülü uygulanmıştır. Matematiksel olarak 100M VMT başına ölüm oranı (oran) 1.28 civarındayken, elde edilen vmt değeri ~3200 seviyesindedir. Dolayısıyla "(1.28 * 3200) / 100" işlemi yaklaşık 40-50 aralığında bir sonuç üretmektedir. Tarihsel FARS verilerindeki yıllık can kaybı 40.000 seviyesindeyken, simülasyon başladığı anda sonuçların mantıksız bir şekilde 40-50 bandına (grafiklerde sıfır gibi görünmektedir) çakılması modelleme hatasından kaynaklanmaktadır. Ayrıca grafik_bar.png dosyasında 2035 yılı tahmini can kaybı değerleri 6 ile 153 arasında gösterilmektedir. Buna karşın, öğrencinin hazırladığı Trafik_Kazalari_Analiz_Raporu (1).docx dosyasının 4.1 maddesinde "1980 Sarhoş Sürüş Dönemi şartları bugün uygulansaydı ölümlerin 110 binlere fırlayacağını gördük" ifadesi yazmaktadır. Kodun ürettiği değerler (153 ölüm) ile raporda beyan edilen değerler (110.000 ölüm) birbiriyle tamamen çelişmektedir. Öğrenci, simülasyonun hatalı sonuçlar verdiğini fark etmesine rağmen grafiklerdeki eksen ölçeğini manipüle ederek durumu gizlemeye çalışmış ve rapora tamamen uydurma veriler yazmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, tarihsel verileri (1975-2023) NHTSA FARS veritabanından nesne (object) yapısı içinde almaktadır. Gelecek projeksiyonları (2024-2035) ise arayüzdeki slider girdilerine göre katsayı tabanlı bir formülle işlenerek anlık olarak grafiklere (Chart.js) aktarılmakta ve CSV/JSON formatında dışa aktarıma sunulmaktadır.

Kontrol Kaldıraçları: Alkol etkili sürüş, hız ihlali, kemersiz yolcu ölümleri, dikkat dağınıklığı, emniyet kemeri kullanım oranı, ADAS teknoloji penetrasyonu, yıllık VMT büyüme hızı ve yol iyileştirme endeksi olmak üzere 8 adet eyleme geçirilebilir kontrol mekanizması sunulmuştur. Bu kaldıraçlar çıktı mantığını matematiksel olarak etkilemektedir ancak formül hatası nedeniyle anlamlı sonuç üretmemektedir.

Localhost Kontrolü: KALDI - rapor_olustur.py scripti içerisinde "C:\Users\Eylül\Downloads\Trafik_Kazalari_Analiz_Raporu_v2.docx" şeklinde kullanıcı bilgisayarına ait mutlak ve yerel bir dosya yolu referansı kullanılmıştır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): KALDI - Gerekçe: 2023 yılına kadar 40.000 seviyesinde seyreden tarihsel veriler, simülasyonun başladığı 2024 yılı itibarıyla formüldeki matematiksel ölçeklendirme hatası nedeniyle aniden 40-50 seviyelerine düşmektedir. Gerçekçi bir simülasyon mekanizması kurulmamış, veri sürekliliği ve mantığı bozulmuştur.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüz üzerinde amacına uygun, kanun yapıcılar için eyleme geçirilebilir parametreler ve hazır senaryo modları sunulmuştur. Girdiler simülasyon çıktısını matematiksel olarak etkilemektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Üretilen simülasyon verileri analiz edilmeye uygun yapılandırılmış CSV ve JSON formatlarında dışa aktarılabilmektedir.

NİHAİ DURUM: REDDEDİLDİ (NOT: 0)