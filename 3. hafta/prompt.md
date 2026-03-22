# Yapay Zeka ile Veri Üretimi ve Görselleştirme Örneği

Bu belge, öğrencilere Yapay Zeka (AI) asistanları ile kodlama yaparken yaşanan diyalogların, alınan hataların ve sorun çözme adımlarının bir örneğini sunmak amacıyla hazırlanmıştır. 

---

**Öğretmen:**
> yeni bir kasör oluştur adı "3. hafta" olsun. içinde bir python kodu olsun bu kod "data.csv" dosyasını oluştursun. dosyada 3 sütunda 500 kişinin verisi olacak. birinci sütun ID sütunu ve 1 de 500 e gidecek, 2. sütun boy sütunu olacak ve bu sütuna kodun rasgele 150 ile 190 arasında sayılar oluşturmasını istiyorum. üçüncü sütunda ise kilo olsun bunda da 50 ile 100 arasında rasgele sayılar olsun. ancak bu rasgele sayılar tamamane rasgele olmasın normal dağılımlı bir çan eğrisi formunda veriler olsun.

**Yapay Zeka (AI):**
> _(Gerekli Python kodunu yazar ve dosyaları oluşturur. Kodu çalıştırmayı dener ancak sistemden iptal yanıtı döner)_
> Ben kodu çalıştırmak için bir komut gönderdim, ancak görünüşe göre komut sisteminiz veya sizin tarafınızdan iptal edildi. Kodu sizin için tekrar çalıştırmamı ister misiniz?

**Öğretmen:**
> why didn't you run the python code? *(neden kodu çalıştırmadın?)* / sen çalıştırmalısın kodu veya çalıştırmana engel olan bir şey varsa onu tespit et

**Yapay Zeka:**
> Kodu çalıştırmak için tekrar bir istek gönderiyorum. Eğer sistemsel bir engel varsa komutun çıktısında göreceğiz. Lütfen ekrandaki çalışma iznini onaylayın.
> _(İkinci kez dener ve kod başarıyla çalışarak 500 kişilik, normal dağılımlı veriyi içeren **data.csv** dosyasını oluşturur.)_

**Öğretmen:**
> ben bir şey onaylamadan başarıyla kodu çalıştırdın farklı olan neydi şimdi?

**Yapay Zeka:**
> İlk denememde sisteme kodu çalıştırma isteği gönderdiğimde bana hemen "Kullanıcı komutu iptal etti" yanıtı döndü. İkinci denememde ise komut sisteminize başarıyla ulaştı ve direkt onaylanarak terminalde çalıştı. Benim tarafımda farklı yaptığım hiçbir şey yoktu, yalnızca ilk komut bir şekilde geri çevrilmişti! Dosyanız hazır.

**Öğretmen:**
> tamamdır şimdi bu CSV'deki veriyi görselleştirmek istiyorum. ne gibi seçeneklerim var?

**Yapay Zeka:**
> Önünüzde birkaç harika seçenek var:
> 1. **Python ile Doğrudan Kod (Matplotlib/Seaborn):** Çan eğrilerini (histogram) elde etmek için en pratiği.
> 2. **Tablo Programları (Excel, Google Sheets):** E-Tabloları kullanarak sürükle bırak ile grafik hazırlayabilirsiniz.
> 3. **Web Tabanlı Dashboard (Streamlit):** Grafikleri web uygulamasında kullanmak isterseniz.
>
> *Benim Önerim:* Matplotlib kullanarak boy ve kilonun normal dağılımını yan yana çizdirecek yeni bir Python kodu yazabiliriz.

**Öğretmen:**
> matpltlib ile oluşturulan grafikler hangi formatta kaydediliyor

**Yapay Zeka:**
> İhtiyacınıza göre kodun sonuna ne yazarsanız (otomatik algılayarak) o formatta kaydeder. Örneğin:
> *   **PNG / JPG:** Resim ve sunumlar için.
> *   **PDF / SVG / EPS:** Yakınlaştırınca bozulmayan, kalite kaybı yaşatmayan makale ve bilimsel yayın formatları.

**Öğretmen:**
> tamam o zaman matplotlib ile veriyi görselleştir

**Yapay Zeka:**
> _(Görselleştirme için **visualize_data.py** kodunu yazar ve çalıştırmayı dener. Ancak sistemde matplotlib yüklü olmadığı hatasını alır.)_
> Görünüşe göre sisteminizde **`matplotlib`** kütüphanesi henüz yüklü değil. Sizin için `pip install matplotlib` komutunu kullanarak indirmek istiyorum.
> _(Linux ortamındaki güvenlik kısıtlaması nedeniyle direkt indirme yapılamaz)_
>
> **Güvenlik Çözümü:** İndirme işlemini doğrudan sisteme yapmak yerine en temiz yol olan **"Sanal Ortam" (Virtual Environment - venv)** oluşturup oraya kurulum yapacağız.

**Öğretmen:**
> _(Onay penceresini / indirme sürecini terminalden yanlışlıkla iptal eder)_

**Yapay Zeka:**
> Görünüşe göre indirme işlemi (yaklaşık 8.7 MB) sizin tarafınızdan yarıda kesildi (cancelled). İnternetten dolayı iptal olmuş olabilir, indirmeyi tekrar başlatayım mı?

**Öğretmen:**
> indir tekrar 

**Yapay Zeka:**
> Komutu tekrar gönderiyorum. Lütfen indirme işlemi bitene dek onay pencerelerini kapatmayın.
> _(Kurulum sorunsuz tamamlanır ve program çalışarak 3 adet dağılım grafiği içeren **grafikler.png** dosyasını çıkartır)_
> İşlem bu kez başarıyla tamamlandı! Kütüphane kuruldu, grafikler çizildi!

**Öğretmen:**
> tamam şimdi bunu githuba push etmek istiyorum

**Yapay Zeka:**
> Harika fikir! Ancak GitHub'a yüklerken çok önemli bir detaya dikkat etmemiz gerekiyor: Kodları çalıştırmak için kurduğumuz **`venv` (Sanal Ortam) klasörünü GitHub'a KESİNLİKLE YÜKLEMEMELİYİZ**. (İçi gereksiz doludur).
> 
> Sadece yazdığınız kodları (`.py` dosyaları), `data.csv`'yi ve `grafikler.png`'yi seçerek klasörünüzü temiz bir şekilde GitHub'a gönderiyorum.
> _(Sadece ilgili dosyaları git depolarına ekler, commit atar ve push yapar)_
> İşlem tamamlandı! 🎉 Kodlarınız artık güvenle GitHub'da. 

**Öğretmen:**
> can you export out discussion in markdown format to the prompt.md file? I want to show my questisno and your answers as an example to my students

**Yapay Zeka:**
> Harika bir fikir! Tüm konuşmamızı detaylı ve öğretici olacak şekilde derleyip **prompt.md** adlı bu dosyaya çıkarttım. İyi dersler!
