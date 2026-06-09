---
gorev_13: 0
final_notu: 10
---
# DENETİM RAPORU: melihyavuk/toplumun-para-harcamas- / Melih Yavuk

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Simülasyon veriyi iki kanaldan almaktadır: Birincisi kod içinde statik olarak tanımlanmış OECD tabanlı ülke bütçe sepeti ağırlıkları, ikincisi ise corsproxy.io aracılığıyla Dünya Bankası API uç noktalarından (FP.CPI.TOTL.ZG ve FR.INR.RINR göstergeleri) çekilen canlı enflasyon ve reel faiz verileridir. API bağlantısında sorun yaşanması ihtimaline karşı mantıklı bir varsayılan veri seti (fallback) kurgulanmıştır. Girdiler matematiksel formüllerle işlenerek Chart.js grafiklerine ve HTML tablolarına dinamik olarak aktarılmaktadır.

Kontrol Kaldıraçları: Kullanıcı; referans ülke seçimi, veri yılı seçimi, üç farklı senaryo butonu, entegrasyon oranı (eta) slider'ı, fütüristik finansal hedef girdileri, günlük bütçe harcama formu ve DePIN staking miktar kontrolü gibi geniş bir kaldıraç setine sahiptir. Bu faktörlerin değiştirilmesi, formüller (alpha, beta, gamma, delta katsayıları) üzerinden bütçe paylarını, karbon salınım azaltımını, hedef sürelerini ve staking getiri projeksiyonlarını gerçekçi ve dinamik olarak etkilemektedir. Değişimler kozmetik değildir.

Localhost ve Dağıtım Uygunluğu: GEÇTİ - Kod tabanında hiçbir localhost veya yerel bilgisayara ait mutlak dosya yolu bağımlılığı bulunmamaktadır. Proje tamamen istemci taraflı (pure HTML/CSS/JS) teknolojilerle inşa edildiğinden, GitHub Pages gibi statik web barındırma hizmetleri üzerinde teknoloji uyuşmazlığı olmadan sorunsuz bir şekilde çalışmaktadır.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Dünya Bankası'ndan çekilen gerçek makroekonomik veriler ile kurgusal antigravitasyonel altyapı maliyet düşüşleri (AGEM) mantıklı bir korelasyon içinde formülize edilmiştir. Çıktılar rastgele gürültü (Math.random) ile değil, kullanıcı girdilerine bağlı deterministik denklemlerle üretilmektedir.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Sunulan arayüz kontrolleri simülasyonun amacına doğrudan hizmet eden, politika yapıcının veya bireysel kullanıcının karar mekanizmalarını simüle eden anlamlı kaldıraçlardır. Gereksiz veya işlevsiz hiçbir kontrole yer verilmemiştir.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Projede "Akademik PDF Rapor Hazırlayıcı" modülü bulunmaktadır. Bu modül, CSS @media print kuralları ve Times New Roman tipografisine sahip özel bir HTML şablonu (printArea) kullanarak tüm simülasyon çıktılarını ve kullanıcı bütçe verilerini resmi bir akademik rapor formatında PDF olarak kaydetmeye veya yazdırmaya olanak tanımaktadır.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

# FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

GENEL ANALİZ

Stratejik Eyleme Geçirilebilirlik ve Eylem Planı (Kritik Eşik): KALDI - Raporda ampirik veriler ve simülasyon çıktıları sunulmuş olsa da, eylem planının ve politika önerilerinin temelini oluşturan teknoloji tamamen bilim kurgu unsurlarına ve fiziksel olarak imkansız varsayımlara (antigravitasyon/yerçekimsizleştirme) dayanmaktadır. T.C. Yatırım Ofisi gibi resmi bir kamu merciinden var olmayan bir teknoloji için 500 milyon USD bütçe talep edilmesi ve havada asılı duran sıfır arsa maliyetli konut projeleri önerilmesi, "karar alıcıdan imkansız eylemler talep edilmesi" kapsamına girmektedir. Gerçekçi, uygulanabilir ve bürokratik mevzuata uygun bir stratejik eylem planı barındırmadığı için rapor bu kritik eşikten kalmıştır.

Çözümü Satabilme ve İkna Kabiliyeti: Öğrenci, "Baş Ekonomist ve Kurucu" rolünü benimseyerek hitap, talep ve teklif dengesini biçimsel olarak kurmuştur. Ancak önerilen çözümün rasyonel bir zemini olmaması ve "sihirli makine" argümanlarına dayanması sebebiyle, bir kamu yöneticisini veya yatırım ofisini ikna edebilme yetisi tamamen işlevsiz kalmıştır. Gerçekçi bir ekonomik problemi fantastik unsurlarla çözme çabası projenin satılabilirliğini engellemektedir.

Veri Temelli Kanıtlar ve Simülasyon Atıfları: Raporda, simülasyonun arka planında yer alan Eta ($\eta$) entegrasyon katsayısına, TÜİK ve OECD tabanlı hanehalkı bütçe sepeti ağırlıklarına doğrudan atıfta bulunulmuştur. Tablo 1 bünyesinde mevcut durum ile simülasyon çıktısı olan birim değerler ve yüzdesel değişim oranları (%65 konut düşüşü, %722.5 serbest harcama artışı gibi) spesifik verilerle rapora yansıtılmıştır. Öğrenci kendi simülasyon çıktılarını rapora işlemeyi başarmıştır.

Yapay Zeka Entegrasyonu ve Rapor Profesyonelliği: Rapor; başlık, muhatap, tarih ve hazırlayan kişi bilgileri ile kurumsal formata uygun şekilde yapılandırılmıştır. Yapay zekaya ait jenerik dolgu paragrafları büyük oranda temizlenmiştir. Ancak raporda kullanılan "sihirli uçan balonlar", "sihirli bir makine", "enflasyon canavarı yok olacak", "aileler çocuklarına daha çok oyuncak alabilecek" gibi çocuksu ve gayriciddi ifadeler, bir kamu kurumuna sunulacak nihai raporda olması gereken kurumsal, profesyonel ve bürokratik üsluba tamamen aykırıdır. Rapor genelinde emoji kullanılmamıştır.

PUAN KIRILMA GEREKÇELERİ / RED DETAYI

- Raporda sunulan eylem planı ve politika önerileri, var olmayan ve fiziken imkansız bir teknolojiye (antigravitasyon) dayandığı, kamu karar alıcısından imkansız eylemler talep ettiği için "1. Kritik Eşik (Stratejik Eyleme Geçirilebilirlik)" kriterinden KALDI almıştır ve rapor doğrudan REDDEDİLMİŞTİR.
    
- Rapor metninde kullanılan "sihirli balonlar", "sihirli makine", "enflasyon canavarı" gibi ifadeler resmi yazışma ve kurumsal raporlama ilkelerine aykırı olup, laubali ve gayriciddi bir dil barındırdığı için profesyonellik ölçütlerini karşılamamaktadır.
    

NİHAİ FİNAL NOTU: 0 XP