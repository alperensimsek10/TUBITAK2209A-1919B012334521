import pandas as pd
import matplotlib.pyplot as plt
import os

# Dosya yolu
file_path = r"C:\Users\EXCALIBUR\OneDrive\Masaüstü\KonukOtel.xlsx"
save_path = r"C:\Users\EXCALIBUR\OneDrive\Masaüstü\"

# Veriyi oku
df = pd.read_excel(file_path)

# Sayısal verileri float'a çevir
numeric_cols = ['comment_score', 'hotel_score']
df[numeric_cols] = df[numeric_cols].astype(float)

# Her dil için grafik oluştur
for language in df['language'].unique():
    lang_data = df[df['language'] == language]
    sentiments = ['Pozitif', 'Nötr', 'Negatif']
    guest_counts = [
        (lang_data['guest_sentiment'] == 'Positive').sum(),
        (lang_data['guest_sentiment'] == 'Neutral').sum(),
        (lang_data['guest_sentiment'] == 'Negative').sum()
    ]
    hotel_counts = [
        (lang_data['guest_sentiment'] == 'Positive').sum(),
        (lang_data['guest_sentiment'] == 'Neutral').sum(),
        (lang_data['guest_sentiment'] == 'Negative').sum()
    ]

    # Ortalama puanları hesapla
    avg_guest_score = lang_data['comment_score'].mean()
    avg_hotel_score = lang_data['hotel_score'].mean()

    # Grafik çiz
    fig, ax = plt.subplots(figsize=(8, 6))
    bar_width = 0.35
    x = range(len(sentiments))

    ax.bar(x, guest_counts, bar_width, label='Konuk', color='brown')
    ax.bar([p + bar_width for p in x], hotel_counts, bar_width, label='Otel', color='blue')

    # Başlık ve etiketler
    ax.set_xlabel("Yorum Türü")
    ax.set_ylabel("Yorum Sayısı")
    ax.set_title(f"{language} - Kullanıcı ve Otel Yorum Analizi")
    ax.set_xticks([p + bar_width / 2 for p in x])
    ax.set_xticklabels(sentiments)
    ax.legend()

    # Ortalama puanları ekle
    ax.text(0, max(guest_counts) * 0.9, f"{avg_guest_score:.1f}", fontsize=12, color='black', fontweight='bold')
    ax.text(1, max(hotel_counts) * 0.9, f"{avg_hotel_score:.1f}", fontsize=12, color='black', fontweight='bold')

    # PNG olarak kaydet
    save_file = os.path.join(save_path, f"{language}_yorum_analizi.png")
    plt.savefig(save_file, dpi=300)
    plt.close()

print("Grafikler başarıyla kaydedildi!")