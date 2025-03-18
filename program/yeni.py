import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as ticker

# Masaüstü yolu
desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Masaüstü")

# Yorum verilerini elle giriyoruz
data = {
    'language': ['Almanca', 'Arapça', 'Felemenkçe', 'Fransızca', 'İngilizce', 'İspanyolca', 'İsveçce', 'İtalyanca', 'Lehçe', 'Portekizce', 'Rusça', 'Türkçe'],
    'Pozitif': [76, 0, 92, 60, 4386, 3, 11, 3, 21, 0, 46, 83],
    'Nötr': [574, 8, 317, 1027, 396, 24, 148, 175, 96, 2, 2296, 2192],
    'Negatif': [22, 0, 8, 19, 259, 0, 0, 5, 2, 0, 24, 18]
}

# Veriyi DataFrame olarak oluştur
df = pd.DataFrame(data)

# Duygu kategorilerini belirleme
sentiment_categories = ['Pozitif', 'Nötr', 'Negatif']

# Duygu dağılımını dillere göre gruplama
sentiment_counts = df.set_index('language')[sentiment_categories]

# Renkler (Açık mavi, açık yeşil, daha koyu sarı)
colors = ['lightblue', 'lightgreen', 'gold']  # Koyu sarı için 'gold' kullanıldı

# Grafik oluştur (Yan yana sütun grafik)
ax = sentiment_counts.plot(kind='bar', stacked=False, figsize=(12, 6), color=colors,
                           edgecolor='black', width=0.8)

# Yorum sayısı için logaritmik ölçek
ax.set_yscale('log')

# Y ekseni etiketlerini kaldırma
ax.yaxis.set_ticks_position('none')

# Her sütunun üstüne değeri yaz (Font boyutunu küçültme ve bold yapma)
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                fontsize=8, color='black',  # Font boyutu burada değiştirildi
                fontweight='bold',  # Yazı tipi kalın (bold) yapıldı
                xytext=(0, 5), textcoords='offset points')

# Grafik detayları
plt.xlabel("Diller", fontweight='bold')  # X ekseni etiketini bold yap
plt.ylabel("Yorum Sayısı (Logaritmik)", fontweight='bold')  # Y ekseni etiketini bold yap
plt.title("Dillere Göre Konuk Yorumları", fontweight='bold')  # Başlık bold yap
plt.legend(title="Duygu", title_fontsize='large')  # Başlık için yazı tipi boyutu belirle
plt.xticks(rotation=45, fontweight='bold')  # X ekseni etiketlerini bold yap
plt.grid(axis='y', linestyle="--", alpha=0.7)

# Grafiği masaüstüne PNG olarak kaydet
save_path = os.path.join(desktop_path, "KonukOtel_Sentiment_Logarithmic_ManualData.png")
plt.savefig(save_path, dpi=300, bbox_inches="tight")

# Grafiği göster
plt.show()

print(f"Grafik başarıyla kaydedildi: {save_path}")
