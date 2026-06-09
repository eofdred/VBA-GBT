---
gorev_13: 75
final_notu: 100
ogrenci_no: 2511317006
---
# DENETİM RAPORU: aykuutt/calfcare-sim

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. `simulation.js` dosyasındaki `CalfAgent`, `WorkerAgent` ve `EnvironmentAgent` sınıfları, birbirini mantıksal ve matematiksel olarak etkileyen stokastik bir Etmen Tabanlı Model (ABM) mekanizmasına dayanmaktadır. `Math.random()` kullanımı yalnızca işçilerin yorgunluk seviyelerine bağlı olarak gelişen anlık hata olasılıkları gibi meşru stokastik süreçleri yönetmek için kullanılmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon, başlangıç verilerini kullanıcı arayüzündeki girdilerden (ahır tipi, ırk, bütçe, bakıcı sayısı, havalandırma, hijyen skoru, kolostrum saati) almaktadır. Çevre sıcaklığı ve nem verileri, Open-Meteo API'si aracılığıyla doğrudan Burdur lokasyonu (Enlem: 37.7183, Boylam: 30.2823) için gerçek zamanlı olarak çekilmektedir. Veriler her saat başı (`tick()`) güncellenerek buzağının sağlık/bağışıklık durumunu ve işletme bütçesini dinamik olarak değiştirmekte, sonuçlar ise arayüzdeki grafiğe ve kıyaslama tablosuna aktarılmaktadır.

Kontrol Kaldıraçları: Kullanıcı ahır tipini, buzağı ırkını, başlangıç bütçesini, bakıcı sayısını, havalandırma gücünü, başlangıç hijyen skorunu ve kolostrum verilme saatini kontrol edebilmektedir. Bu kaldıraçlar simülasyonun çıktı mantığını doğrudan etkilemektedir. Örneğin; kolostrumun ilk 2 saat içinde verilmemesi pasif bağışıklığın (IgG) saat başı düşmesine, amonyak seviyesinin yükselmesi ve nemin %80'i aşması ise pnömoni riskiyle buzağının sağlık skorunun düşmesine sebep olmaktadır. Aynı şekilde, seçilen ırkın genetik tolerans eşiği ile ahır tipinin yalıtım özelliklerine göre termal şok mekanizması tetiklenmektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Kod tabanında `localhost`, `127.0.0.1` veya yerel bilgisayara ait mutlak dosya yolları (`C:/Users/...` gibi) bulunmamaktadır. Uygulama tamamen istemci taraflı (Pure Vanilla JS, HTML, CSS) olarak kurgulanmış olup, herhangi bir dinamik backend framework bağımlılığı taşımadığı için GitHub Pages gibi statik barındırma hizmetleri üzerinde sorunsuz çalışabilecek mimariye sahiptir.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Literatürdeki hayvan refahı prensiplerini baz alan C.O.R.E. (Colostrum, Operation, Risk, Environment) çerçevesi kod seviyesinde matematiksel formüllerle (Amonyak birikimi, işçi vardiya/yorgunluk döngüsü, nem çarpanlı pnömoni riski ve ırk bazlı termal şok) eksiksiz kurgulanmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzde sunulan tüm slider ve select kutuları, simülasyonun gidişatını ve buzağının hayatta kalma oranlarını (başarı/ölüm/iflas durumlarını) doğrudan ve anlamlı bir şekilde değiştiren operasyonel kaldıraçlardır. Sırf kontrol sayısını artırmaya yönelik kozmetik bir parametreye rastlanmamıştır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: `app.js` içerisindeki `btnExportCSV` bileşeni vasıtasıyla, simülasyonda gerçekleştirilen tüm denemelerin geçmiş verileri (Irk, Ahır Tipi, Bakıcı Sayısı, Havalandırma, Kolostrum Saati, Final Sağlık/Bağışıklık, Bütçe ve Sonuç durumları) yapılandırılmış CSV formatında (`calfcare_analiz_raporu.csv`) dışa aktarılabilmektedir.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ Üstlenilen Rol ve Konu Uygunluğu: Öğrenci, Burdur çiftlik yönetimine yönelik bir danışman/çözüm ortağı rolünü üstlenmiştir. Hayvancılık işletmelerindeki yüksek maliyetli buzağı ölümleri gibi kritik ve gerçek bir probleme odaklanması, karar alıcılar için son derece problem çözücü ve ticari olarak eyleme geçirilebilir somut bir teklif niteliğindedir. Anlatım ve Basitlik Düzeyi: Rapordaki anlatım son derece yalın, anlaşılır ve hedef kitleyi teknik terimlerle boğmayan bir sadeliktedir ("sihirli süt", "cüzdanımızda ne kadar para kalacağı" gibi ifadeler). Rapora entegre edilen üç adet grafik (Kolostrum Durumu, Irk Performansı, Ahır Tipleri) ve bunlara bağlı sayısal analizler, karmaşık verileri bir yöneticinin ilk bakışta anlayabileceği şekilde başarıyla görselleştirmiştir. Yapay Zeka İzleri ve Özensizlik: Metinde yapay zekanın ürettiği basmakalıp dolgu paragraflarına, robotik geçiş ifadelerine veya jenerik başlık yapılarına rastlanmamıştır. Öğrenci süreci tamamen kendi süzgecinden geçirerek samimi ve özgün bir üslup yakalamıştır. Ancak "bende", "Burdurun", "kar-zarar miktarını (72 saatlik periyot) için" gibi bazı imla, noktalama ve yazım hataları kopyala-yapıştır özensizliğinden ziyade bireysel yazım dikkatsizliğini göstermektedir. Rapor Dil ve Profesyonelliği: Rapor net bir başlığa ve konuya sahiptir. "Sayın Burdur Çiftliği" hitabıyla kurumsal bir bölüme başlanmış, içerikte kesinlikle emoji kullanılmamıştır. Raporun sonunda "Hazırlayan: Aykut Çakıcı" ifadesiyle ad-soyad net bir şekilde belirtilmiştir. Ancak raporun kapanışında bir saygı/iyi dilek ifadesi (Saygılarımla vb.) eksiktir ve doğrudan "Kararı size bırakıyoruz! Birlikte veri odaklı ve kayıpsın bir hayvancılık modeli inşa edebiliriz" cümlesiyle bitirilmiştir.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporun genelinde "bende bu konuda", "yanını cevabını", "Burdurun", "kayıpsın bir" gibi belirgin yazım, imla ve Türkçe dil bilgisi hataları bulunması nedeniyle profesyonel rapor dilinden puan kırılmıştır.
    
- Raporun kapanışında kurumsal yazışma kurallarına uygun profesyonel bir saygı/iyi dilek ifadesinin (Örn: Saygılarımla, İyi çalışmalar dilerim vb.) eksik bırakılması nedeniyle puan kırılmıştır.
    

NİHAİ FİNAL NOTU: 75 XP