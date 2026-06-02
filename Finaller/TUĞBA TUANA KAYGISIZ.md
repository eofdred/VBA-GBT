# DENETİM RAPORU: tugbatuanakaygisiz-web/coral_simulation / Tuğba Tuana Kaygısız

AKADEMİK DÜRÜSTLÜK VE HİLE KARARI

Hile/Manipülasyon Riski: YOK

Sahte Veri/Manipülasyon Tespiti: HAYIR

Hile Kanıtı: Kod dürüstlüğü doğrulanmıştır. Simülasyon çıktıları ham veya rastgele `Math.random()` gürültüsünden ibaret değildir; arka planda okyanus akıntıları, sıcaklık anomalileri, hücreler arası stres yayılımı ve Lotka-Volterra denklemleri tam mekanik entegrasyonla çalışmaktadır.

TEKNİK ANALİZ

Veri Akışı (Data Lineage): Uygulama, tarihsel veri tabanı olarak 5 Pasifik bölgesine ait (American Samoa, Main Hawaiian Islands, Mariana Archipelago, Northwestern Hawaiian Islands, Pacific Remote Island Areas) gerçek NOAA NCRMP (Ulusal Mercan Resifi İzleme Programı) ve NOAA NCEI gözlem verilerini kod içine gömülü sabit bir veri mimarisi (`DATA`) olarak kabul eder. 2013-2023 yılları arasındaki bu ham veriler, grafikler üzerinde bağımsız altın yıldız (`star point`) işaretçileri olarak doğrulanabilir şekilde sergilenir. 2024 yılı sonrasındaki gelecek projeksiyonu ise IPCC'nin SSP2-4.5 (orta emisyon) senaryosu çapa noktaları (`PROJ_ANCHORS`) baz alınarak anlık matematiksel interpolasyon zinciriyle hesaplanır, zamana ve kullanıcı politikalarına bağlı olarak eş zamanlı biçimde 2D Canvas matrisine (Reef Haritası/Isı Haritası) ve Chart.js zaman serisi grafiklerine akar.

Kontrol Kaldıraçları: Sistem; 6 adet emisyon kaynağı slider'ı (Endüstri, Ulaşım, Tarım, Orman Kaybı, Temiz Enerji, CCS), 3 adet uluslararası iklim anlaşması toggle butonu (ABD, Çin, AB), 4 farklı okyanus ve resif politikası girdisi (Alkalinite Güçlendirme, Turizm Düzenlemesi, Balıkçılık Kotaları, Uluslararası GEF Fonu) ve 1 adet Erken Uyarı Sistemi (EWS) onay kutusu olmak üzere toplam 14 adet fonksiyonel kontrol kaldıracı sunmaktadır. Bunlara ek olarak, harita üzerinde fare ile dinamik ve geometrik Deniz Koruma Alanları (MPA) çizilebilmektedir. Kontroller kesinlikle kozmetik değildir; örneğin çizilen bir MPA alanı ilgili hücrelerin stres birikim katsayısını (`stressAccMult`) doğrudan %77 oranında düşürmekte, komşu hücrelere virütik stres bulaşmasını %70 azaltmakta ve doğal iyileşme hızını 3.25 kat artırmaktadır. Emisyon ayarları ise matematiksel formülasyon ile küresel sıcaklık değişim delta değerini (`projDelta`) doğrudan manipüle etmektedir.

Localhost Kontrolü: GEÇTİ. Kod tabanı bütünüyle incelenmiş olup, hiçbir statik yerel bağlantı adresi (`localhost`, `127.0.0.1`) ya da C:/ sürücüsüne işaret eden yerel mutlak dosya yolu referansına rastlanmamıştır. Varlıklar bağımsız bağıntılı rölatif yollarla yönetilmektedir.

EŞİK DEĞERLENDİRMELERİ

Eşik 1 (Gerçekçilik ve Mantık): GEÇTİ - Gerekçe: Simülasyon motorunda rastgele sayılarla gürültü üretmek yerine, 2D Simplex Noise algoritması prosedürel türbülans için entegre edilmiştir. Ayrıca 3 farklı okyanus akıntı merkezinin hareket formülleri, IDW (Inverse Distance Weighting) komşuluk enterpolasyonu ve Lotka-Volterra av-avcı (av balığı ve yırtıcı şahin/köpekbalığı popülasyon dengesi) diferansiyel denklemleri ekolojik kurallara tam uyumlu ve gerçekçidir. Ekolojik taşıma kapasitesi (K), mercan canlılık indeksine doğrudan bağlanmıştır.

Eşik 2 (Kontrol Edilebilirlik): GEÇTİ - Gerekçe: Kullanıcı kanun yapıcı rolünde tüm sisteme müdahale edebilmektedir. Sürgüler, politika butonları ve harita üzerinde interaktif olarak mousedown/mousemove/mouseup olaylarıyla çizilen dinamik Deniz Koruma Alanları (MPA) simülasyonun gidişatını ve durum geçiş eşik değerlerini anlık olarak etkiler. BAU, Optimal ve MPA Only adlarında 3 hazır politika senaryo butonu da sisteme kusursuzca bağlanmıştır.

Eşik 3 (Veri Dışa Aktarımı): GEÇTİ - Gerekçe: Kod içerisinde her 3 adımda bir (`LOG_INTERVAL = 3`) simülasyonun o anki tüm parametrelerini (yıl, ay, bölge, sst, dhw, ortalama stres, mercan örtüsü %, balık popülasyonları, aktif emisyon oranları ve 2100 tahmini) anlık olarak yakalayan bir günlükleme yapısı (`simLog[]`) kurulmuştur. Arayüzdeki "⬇ CSV" butonu, JavaScript Blob API ve URL.createObjectURL mekanizmasını kullanarak tüm bu veriyi tam yapılandırılmış, akademik analize uygun bir CSV dosyası olarak dışa aktarabilmektedir. Canlı satır sayacı rozeti de yeşil renk koduyla arayüzde çalışmaktadır.

NİHAİ DURUM: NOTLANDIRMAYA UYGUN

## FİNAL RAPORU VE İLETİŞİM DEĞERLENDİRMESİ

### GENEL ANALİZ

- **Üstlenilen Rol ve Konu Uygunluğu:** Öğrenci, teknik anlamda bir bilimsel danışman veya çevre uzmanı rolünü veri setleri üzerinden başarıyla temellendirmiş; NOAA NCRMP gözlem verilerini ve IPCC SSP2-4.5 emisyon projeksiyonlarını konuya derinlemesine entegre etmiştir. Ancak hazırlanan döküman, bir kanun yapıcıya veya karar alıcı üst düzey bir yöneticiye somut çözümler sunan ve eyleme çağıran bir "politika/karar belgesi" üslubundan ziyade, standart bir "akademik ödev/makale teknik raporu" formatında kalmıştır. Yöneticiye hitap hissi arka planda kalmıştır.
    
- **Anlatım ve Basitlik Düzeyi:** "5 yaşındaki birine anlatır gibi" anlatım ilkesine tam olarak uyulmamıştır. Metin; "zooxanthellae", "hücresel otomata", "Moore mahallesi", "Lotka-Volterra av-avcı denklemleri" ve "Inverse Distance Weighting interpolasyonu" gibi ağır teknik ve akademik jargona fazlasıyla boğulmuştur. Sektörü hiç bilmeyen bir yöneticinin bu parametrelerin nihai etkilerini tek okumada kavraması oldukça güçtür. Tablo tasarımı işlevsel olsa da dildeki karmaşıklık sadelik notunu düşürmektedir.
    
- **Yapay Zeka İzleri ve Özensizlik:** Öğrenci giriş kısmında yapay zeka destekli araçlardan yararlandığını açıkça ifade etmiştir. Bununla birlikte metinde, yapay zekaya has tipik basmakalıp kalıplar ("Simülasyon aşağıdaki temel hedefleri karşılamak üzere tasarlanmıştır", "Bu simülasyon birçok açıdan benzer araştırma araçlarından ayrışmaktadır") ve düzenlenmemiş robotik dolgu paragrafları yoğun şekilde hissedilmektedir. Öğrenci metni kendi özgün diliyle yeterince harmanlamamıştır.
    
- **E-Posta Dil ve Profesyonelliği:** Öğrencinin teslim ettiği dökümanda, dökümanı kurumsal bir dille yöneticiye sunması gereken "E-Posta Gövdesi" (Konu satırı, profesyonel hitap, emoji kısıtlaması, saygı ifadesi ve imza) tamamen eksiktir. Herhangi bir e-posta metni sunulmadığı için bu kriterden tam puan kaybı yaşanmıştır.
    

### PUAN KIRILMA GEREKÇELERİ

- Raporda "5 yaşındaki birine anlatır gibi" ilkesine uyulmayıp, sektörü bilmeyen bir yöneticinin anlayamayacağı düzeyde ağır akademik/teknik jargon (Moore mahallesi, Lotka-Volterra diferansiyel denklemleri, IDW enterpolasyonu vb.) kullanıldığı için puan kırılmıştır.
    
- Metin, bir yöneticiye hitap eden karar alıcı sade bir dilden ziyade klasik akademik ödev üslubuyla yazıldığı için puan kırılmıştır.
    
- Yapay zekaya ait basmakalıp başlıklar, geçiş cümleleri ve dolgu metin yapıları dökümandan tamamen temizlenmediği için puan kırılmıştır.
    
- Rapor sunumu için yapılması zorunlu olan profesyonel kurumsal e-posta iletişimi (konu, hitap, emoji kontrolü, imza) metinde hiç yer almadığı için puan kırılmıştır.
    

**NİHAİ FİNAL NOTU:** 70 XP