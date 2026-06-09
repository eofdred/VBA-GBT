---
gorev_13: 0
final_notu: 0
---
# DENETİM RAPORU: buraktalhademir/yks-sim-lasyonu

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon verileri, matematiksel Box-Muller dönüşümü kullanılarak üretilen ve gerçek ÖSYM yığılmasını taklit eden sağa çarpık bir aday havuzundan beslenmektedir. Üretilen adaylar, YÖK'ün resmi başarı sırası barajları ve coğrafi lokalizasyon eğilimlerine (kendi bölgesini %35 daha fazla tercih etme psikolojisi) göre filtrelenerek 24'lü tercih listeleri oluşturmaktadır. Bu veriler Gale-Shapley Kararlı Eşleşme Algoritması mimarisine (MaxHeap destekli veri yapısıyla) sokularak işlenmekte ve nihai ulusal kontenjan matrisine dönüştürülmektedir.

Kontrol Kaldıraçları: Kullanıcı; Aday Sayısı (N), Politika Laboratuvarı Senaryoları (Normal, Kriz: Şehir Terk Etme, Teşvik: Anadolu Kontenjan Artırımı), Politika Etki Katsayısı slider'ı ve YÖK Başarı Sırası Barajları aktif/pasif butonunu kontrol edebilmektedir. Bu kaldıraçlar sadece kozmetik unsurlar olmayıp, üniversite popülasyon ağırlıklarını, kontenjan çarpanlarını ve filtre dizilimlerini manipüle ederek eşleşme algoritmasının çıktısını doğrudan ve dinamik olarak etkilemektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Proje tamamen vanilla JavaScript, Bootstrap 5 ve Chart.js kütüphaneleri kullanılarak istemci taraflı (client-side) geliştirilmiştir. Herhangi bir localhost, 127.0.0.1 veya yerel mutlak dosya yolu bağımlılığı bulunmamaktadır. Statik bir mimariye sahip olduğu için GitHub Pages üzerinde sorunsuz şekilde canlıya alınabilir ve teknoloji uyuşmazlığı barındırmaz.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Tıp (50k), Diş (80k), Hukuk (125k) gibi resmi YÖK barajları koda tam entegre edilmiş, rastgele gürültü yerine Gale-Shapley ve Box-Muller tabanlı deterministik-stokastik bilimsel modeller kullanılmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzdeki senaryo ve yoğunluk girdileri, simülasyon motorundaki matematiksel fonksiyonları doğrudan manipüle eden anlamlı ve eyleme geçirilebilir kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Yüksek veri boyutlarında (N=250.000 durumunda) tarayıcının kilitlenmesini önleyen 10.000'lik chunk (parça) bellek yönetimine sahip, Excel uyumlu BOM kodlamalı yapılandırılmış bir CSV dışa aktarım motoru başarıyla kurulmuştur.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# DENETİM RAPORU: buraktalhademir/yks-sim-lasyonu

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon verileri, matematiksel Box-Muller dönüşümü kullanılarak üretilen ve gerçek ÖSYM yığılmasını taklit eden sağa çarpık bir aday havuzundan beslenmektedir. Üretilen adaylar, YÖK'ün resmi başarı sırası barajları ve coğrafi lokalizasyon eğilimlerine (kendi bölgesini %35 daha fazla tercih etme psikolojisi) göre filtrelenerek 24'lü tercih listeleri oluşturmaktadır. Bu veriler Gale-Shapley Kararlı Eşleşme Algoritması mimarisine (MaxHeap destekli veri yapısıyla) sokularak işlenmekte ve nihai ulusal kontenjan matrisine dönüştürülmektedir.

Kontrol Kaldıraçları: Kullanıcı; Aday Sayısı (N), Politika Laboratuvarı Senaryoları (Normal, Kriz: Şehir Terk Etme, Teşvik: Anadolu Kontenjan Artırımı), Politika Etki Katsayısı slider'ı ve YÖK Başarı Sırası Barajları aktif/pasif butonunu kontrol edebilmektedir. Bu kaldıraçlar sadece kozmetik unsurlar olmayıp, üniversite popülasyon ağırlıklarını, kontenjan çarpanlarını ve filtre dizilimlerini manipüle ederek eşleşme algoritmasının çıktısını doğrudan ve dinamik olarak etkilemektedir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Proje tamamen vanilla JavaScript, Bootstrap 5 ve Chart.js kütüphaneleri kullanılarak istemci taraflı (client-side) geliştirilmiştir. Herhangi bir localhost, 127.0.0.1 veya yerel mutlak dosya yolu bağımlılığı bulunmamaktadır. Statik bir mimariye sahip olduğu için GitHub Pages üzerinde sorunsuz şekilde canlıya alınabilir ve teknoloji uyuşmazlığı barındırmaz.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Tıp (50k), Diş (80k), Hukuk (125k) gibi resmi YÖK barajları koda tam entegre edilmiş, rastgele gürültü yerine Gale-Shapley ve Box-Muller tabanlı deterministik-stokastik bilimsel modeller kullanılmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Arayüzdeki senaryo ve yoğunluk girdileri, simülasyon motorundaki matematiksel fonksiyonları doğrudan manipüle eden anlamlı ve eyleme geçirilebilir kaldıraçlardır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Yüksek veri boyutlarında (N=250.000 durumunda) tarayıcının kilitlenmesini önleyen 10.000'lik chunk (parça) bellek yönetimine sahip, Excel uyumlu BOM kodlamalı yapılandırılmış bir CSV dışa aktarım motoru başarıyla kurulmuştur.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN