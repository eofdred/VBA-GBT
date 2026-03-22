import csv
import random

def generate_normal_in_range(mean, std_dev, min_val, max_val):
    """Belirli bir aralıkta normal dağılımlı (çan eğrisi) rasgele sayı üretir."""
    while True:
        value = random.gauss(mean, std_dev)
        if min_val <= value <= max_val:
            return round(value, 2) # 2 ondalık basamaklı olacak şekilde yuvarlama

def main():
    num_records = 500
    
    # Boy parametreleri: aralık [150, 190], ortalama = 170, standart sapma = ~6.5
    height_mean = 170
    height_std = 6.5
    
    # Kilo parametreleri: aralık [50, 100], ortalama = 75, standart sapma = ~8.3
    weight_mean = 75
    weight_std = 8.3
    
    data = []
    # Sütun başlıkları
    data.append(["ID", "Boy", "Kilo"])
    
    for i in range(1, num_records + 1):
        boy = generate_normal_in_range(height_mean, height_std, 150, 190)
        kilo = generate_normal_in_range(weight_mean, weight_std, 50, 100)
        data.append([i, boy, kilo])
        
    # data.csv dosyasına yazma
    with open("data.csv", mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)
        
    print("500 kişilik veri başarıyla 'data.csv' dosyasına oluşturuldu!")

if __name__ == "__main__":
    main()
