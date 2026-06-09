---
gorev_13: 70
final_notu: 90
ogrenci_no: 2511317024
---
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

- **Üstlenilen Rol ve Konu Uygunluğu:** Öğrenci, bir karar alıcıya veya üst düzey yöneticiye somut çözümler ve politika teklifleri sunan profesyonel bir uzman/danışman rolünü benimsemek yerine, çalışmayı tamamen klasik bir üniversite ödevi ve akademik teknik rapor dilinde sunmuştur. Yöneticiye hitap etme, kurumsal bir perspektif sunma ve eyleme geçirilebilir stratejiler önerme hissi zayıf kalmış, metin akademik ödev sınırlarının dışına çıkamamıştır.
    
- **Anlatım ve Basitlik Düzeyi:** "5 yaşındaki birine anlatır gibi" ilkesi belirgin şekilde göz ardı edilmiştir. Sektöre yabancı bir yöneticinin tek okumada kavramasını zorlaştıracak düzeyde yoğun akademik jargon (zooxanthellae algleri, hücresel otomata yaklaşımı, Moore mahallesi, Lotka-Volterra diferansiyel denklemleri) ve karmaşık matematiksel formüller sadeleştirilmeden doğrudan rapora yansıtılmıştır. Geleceğe yönelik projeksiyonlar yönetsel bir özet niteliği taşımamaktadır.
    
- **Yapay Zeka İzleri ve Özensizlik:** Metin genel olarak düzenli görünse de, yapay zeka araçları tarafından üretilen basmakalıp geçiş cümleleri, jenerik kısıtlamalar listesi ve içi boş dolgu paragrafları belirgindir. Öğrenci yapay zekadan aldığı çıktıları kendi özgün kurumsal diliyle yeterince harmanlamamış ve ham yapıları temizlememiştir.
    
- **Rapor Dil ve Profesyonelliği:** Rapor konusu net bir şekilde tanımlanmış ve teknik raporda emoji kullanılmamış olması kurumsal üslup açısından olumlu bir puan olmuştur. Ancak profesyonel bir raporun sahip olması gereken uygun bir hitap başlığı (Sayın Yetkili / Sayın Yönetici) ile başlama kuralına uyulmamış, metin sonunda kurumsal nezaket içeren bir kapanış ve resmi imza bloğu yapılandırılmamıştır.
    

### PUAN KIRILMA GEREKÇELERİ

- Rapor, bir probleme çözüm sunan profesyonel bir vizyon yerine sıradan bir akademik ödev/makale formatında yazıldığı ve karar alıcıya hitap hissi zayıf olduğu için puan kırılmıştır.
    
- "5 yaşındaki birine anlatır gibi" anlatım ilkesine uyulmayarak, teknik ve biyolojik jargonlar ile diferansiyel denklemler yöneticinin anlayabileceği sadeliğe indirgenmediği için puan kırılmıştır.
    
- Kurumsal raporlama standartlarının gerektirdiği resmi hitap başlığı ile profesyonel saygı ve kapanış ifadeleri eksik bırakıldığı için puan kırılmıştır.
    
- Yapay zeka çıktısı olduğu belirgin olan jenerik dolgu metinleri ve basmakalıp paragraflar kurumsal bir süzgeçten geçirilip temizlenmediği için puan kırılmıştır.
    

**NİHAİ FİNAL NOTU:** 70 XP