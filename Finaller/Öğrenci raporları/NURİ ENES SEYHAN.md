# DENETİM RAPORU: seyhannurienes-afk

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Kullanılan rastgele normal dağıtım fonksiyonu (randomNormal) simülasyondaki stokastik akademik sınav başarı değişkenliğini gerçeğe uygun modellemek amacıyla kullanılmıştır ve kullanıcı girdileri simülasyon çıktılarını matematiksel ve mantıksal olarak doğrudan etkilemektedir.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, verisini kullanıcı arayüzündeki girdilerden ve ders planlayıcı panelinden almaktadır. Girdiler, Euler Metodu (dt=1 gün) tabanlı bir diferansiyel denklem yaklaşımıyla işlenerek kümülatif yorgunluk, motivasyon ve tükenmişlik stoklarına aktarılmaktadır. Çıktılar Plotly.js kütüphanesi yardımıyla grafiklere yansıtılmakta ve bir veri tablosunda yapılandırılarak CSV formatına dönüştürülmektedir.

Kontrol Kaldıraçları: Kullanıcı uyku süresi, haftalık sosyal zaman, çalışma stratejisi (cram günleri), yarı zamanlı iş yükü ve günlük kafein miktarını kontrol edebilmektedir. Bu faktörler model içerisindeki verimlilik ve motivasyon değişim oranlarını (R döngüsü vb.) doğrudan etkileyerek nihai GPA ve tükenmişlik çıktılarını dinamik olarak değiştirmektedir.

Localhost Kontrolü: GEÇTİ - Kod tabanında harici CDN bağlantıları dışında herhangi bir yerel bilgisayar mutlak dosya yolu veya localhost referansı bulunmamaktadır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Akademik hayatın kümülatif yorgunluk, ders zorluk dereceleri ve ders çalışma verimliliği üzerindeki etkileri endojen ve egzojen sistem dinamiği kurallarına uygun olarak mantıklı bir nedensellik ilişkisiyle modellenmiştir.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan slider ve çoklu seçim elemanları simülasyonun amacına doğrudan hizmet eden anlamlı kaldıraçlardır ve her biri matematiksel modelde karşılığa sahiptir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Simülasyon verileri ve üretilen 100 farklı senaryo, Türkçe karakter kodlama standardına uygun (BOM destekli) yapılandırılmış CSV formatında dışa aktarılabilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

#  FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Üstlenilen Rol ve Konu Uygunluğu: Öğrenci bir "akademik danışman / abi" rolünü üstlenerek üniversite yaşam dinamiklerini simüle etmiştir. Konu, bir öğrencinin mental ve akademik başarısını optimize etmek isteyen okul yöneticileri veya danışmanlar için problem çözücü niteliktedir. Ancak, karar alıcı kurumsal bir merciye (bölüm başkanlığı, dekanlık veya rektörlük) hitap eden ve projenin değerini üst yönetime kurumsal bir dille "satan" bir yapı yerine, doğrudan alt hedef kitleye (öğrenciye) seslenen bir rehber havasında kurgulanmıştır.

Anlatım ve Basitlik Düzeyi: Metin oldukça sade, akıcı ve karmaşık diferansiyel yaklaşımları bile herkesin anlayabileceği metaforlarla basitleştiren bir anlatıma sahiptir. Grafik tasarımları, korelasyon matrisi ve kutu grafikleri veri takibini son derece kolaylaştırmaktadır.

Yapay Zeka İzleri ve Özensizlik: Metinde yapay zekanın sıklıkla ürettiği jenerik dolgu paragrafları ("Üniversite hayatı sadece ders kitaplarından ibaret değildir...", "Kısa vadeli zaferler, uzun vadeli çöküş getirir") ve basmakalıp başlık formaları ("Yönetici Özeti", "Araştırma Metodolojisi") süzgeçten geçirilmeden ham bırakılmıştır.

rapor Dil ve Profesyonelliği: Raporda kurumsal bir üsluba yakışmayan, laubali ve kuralları ihlal eden bir kapanış dili kullanılmıştır. Hitap ve üslup akademik ciddiyetten uzaktır. En kritik hata ise raporun sonunda öğrencinin resmi tam adı ve soyadı yerine "Nuri Abin" şeklinde ciddiyetsiz bir imza kullanılmış olmasıdır.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporda öğrencinin resmi tam adı ve soyadı yazmadığı, kimliği net olarak tespit edilemediği ve sınıf listesiyle eşleştirilemediği için rapor REDDEDİLMİŞTİR.
    

NİHAİ FİNAL NOTU: 0 XP