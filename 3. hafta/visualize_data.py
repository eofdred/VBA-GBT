import csv
import matplotlib.pyplot as plt

def main():
    boylar = []
    kilolar = []
    
    # Veriyi Oku
    with open('data.csv', mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader) # Başlık satırını atla (ID, Boy, Kilo)
        for row in reader:
            boylar.append(float(row[1]))
            kilolar.append(float(row[2]))
            
    # Görselleştirme Ayarları
    # Yan yana 3 grafik oluştur (1 satır, 3 sütun)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # 1. Boy Histogramı (Çan Eğrisi formu)
    ax1.hist(boylar, bins=20, color='skyblue', edgecolor='black', alpha=0.8)
    ax1.set_title('Boy Dağılımı (Histogram)')
    ax1.set_xlabel('Boy (cm)')
    ax1.set_ylabel('Kişi Sayısı')
    
    # 2. Kilo Histogramı (Çan Eğrisi formu)
    ax2.hist(kilolar, bins=20, color='lightgreen', edgecolor='black', alpha=0.8)
    ax2.set_title('Kilo Dağılımı (Histogram)')
    ax2.set_xlabel('Kilo (kg)')
    
    # 3. Boy vs Kilo (Dağılım Grafiği)
    ax3.scatter(boylar, kilolar, color='coral', alpha=0.6, edgecolor='black')
    ax3.set_title('Boy ve Kilo İlişkisi (Dağılım)')
    ax3.set_xlabel('Boy (cm)')
    ax3.set_ylabel('Kilo (kg)')
    
    # Grafikleri düzgün şekilde yerleştir ve kaydet
    plt.tight_layout()
    plt.savefig('grafikler.png', dpi=300) # PNG formatında yüksek çözünürlük(300 dpi) ile kaydet
    
    print("Mükemmel! Grafikler başarıyla 'grafikler.png' adıyla kaydedildi.")

if __name__ == "__main__":
    main()
