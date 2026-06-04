# DENETİM RAPORU: senacifci5-prog/toplumsalsiddetsimulasyonu / Sena Çiftçi

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: DÜŞÜK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. `app.py` ve `crime_simulation.py` dosyalarında kullanılan `simulate_risk` fonksiyonu, kullanıcının girdi değerlerine (işsizlik, gini, eğitim, yolsuzluk) bağlı olarak normalize edilmiş veriler üzerinden ağırlıklı bir risk skoru hesaplamaktadır. `extracted/streamlit_app.py` dosyasındaki gelecek yıllara yönelik tahminleme modeli ise Poisson dağılımına ve rastgele gürültü eklenmiş stokastik simülasyon ilkelerine dayandığı için bilimsel olarak meşru bir rastgelelik modelidir.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Proje, Birleşmiş Milletler Uyuşturucu ve Suç Ofisi (U.N.O.D.C.) ve Dünya Bankası (WDI) kaynaklı Excel ve ZIP içerisindeki CSV formatındaki gerçek verileri temel almaktadır. Veriler pandas kütüphanesiyle temizlenmekte, birleştirilmekte ve sonuçlar veri analizi grafiklerine (Matplotlib/Seaborn) veya dışa aktarılabilir CSV/JSON/Excel dosyalarına dönüştürülmektedir.

Kontrol Kaldıraçları: Kullanıcı; ülke seçimi, işsizlik değişimi (%), Gini katsayısı değişimi, eğitim harcaması değişimi ve yolsuzluk değişimi gibi parametreleri slider bileşenleri üzerinden kontrol edebilmektedir. Ayrıca tahminleme simülasyonunda yıl sayısı, rastgelelik standart sapması ve yıllık büyüme oranı ayarlanabilmektedir. Bu kaldıraçlar risk skorunu ve Poisson tabanlı üretilen sayıları doğrudan ve matematiksel olarak etkilemektedir.

Localhost ve Dağıtım Uygunluğu: KALDI - Projede `DATA_DIR = Path.home() / 'Downloads'` şeklinde kullanıcının yerel bilgisayarındaki Downloads klasörüne doğrudan ve katı bir bağımlılık mevcuttur. `check_files()` fonksiyonu bu dosyaların yerelde varlığını zorunlu kılmakta, bulamadığında ise `st.stop()` komutuyla uygulamayı tamamen kilitlemektedir. Projede yerel dosya yollarına ("C:\Users\SENA ÇİFÇİ...") dair dokümantasyon bağımlılığı da yer almaktadır. Bu katı yerel bağımlılıklar ve Streamlit mimarisinin canlı dağıtım gereksinimleri (statik barındırma uyuşmazlığı riski) nedeniyle kriter karşılanamamıştır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Simülasyon, U.N.O.D.C. ve Dünya Bankası'ndan alınan gerçek sosyo-ekonomik verilere ve meşru bir risk indeksleme/Poisson modeline dayanmaktadır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Uygulamada suç risk faktörlerini dinamik olarak simüle eden anlamlı amaca uygun slider kontrolleri kurgulanmıştır ve bu girdiler çıktıyı doğrudan değiştirmektedir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Simülasyon sonuçları CSV, JSON ve Excel formatlarında dışa aktarılabilmektedir.

NİHAİ DURUM: REDDEDİLDİ (NOT: 0)