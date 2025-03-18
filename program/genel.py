import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Excel dosyasını oku
df = pd.read_excel(r"C:\Users\EXCALİBUR\OneDrive\Masaüstü\data\KonukOtel.xlsx", sheet_name="Sheet1")

# 'comment_score' sütununu sayısal hale getir
df["comment_score"] = pd.to_numeric(df["comment_score"], errors="coerce")

# Dile göre yorum sayısı ve ortalama puanı hesapla
language_stats = df.groupby("language").agg(
    yorum_sayisi=("comment_score", "count"),
    ortalama_puan=("comment_score", "mean")
).reset_index()

# Yorum sayısına göre sırala
language_stats = language_stats.sort_values(by="yorum_sayisi", ascending=False)

# Verileri ayır
diller = language_stats["language"]
yorum_sayilari = language_stats["yorum_sayisi"]
ortalama_puanlar = language_stats["ortalama_puan"]

# Grafik boyutu
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Ortalama puan için çubuk grafiği (Mavi)
ax1.bar(diller, ortalama_puanlar, color="blue")
ax1.set_ylabel("Ortalama Puan", color="blue", fontsize=14)
ax1.set_ylim(0, 5.2)
ax1.set_title("Dillere Göre Ortalama Puan", fontsize=16, fontweight="bold")
ax1.set_xticklabels(diller, rotation=30, ha="right", fontsize=12, fontweight="bold")

# Çubukların üzerine değerleri ekleyelim
for i, puan in enumerate(ortalama_puanlar):
    ax1.text(i, puan + 0.1, f"{puan:.2f}", ha="center", fontsize=10, fontweight="bold", color="black")

# Yorum sayısı için çubuk grafiği (Kırmızı)
ax2.bar(diller, yorum_sayilari, color="red")
ax2.set_ylabel("Yorum Sayısı", color="red", fontsize=14)
ax2.set_ylim(0, max(yorum_sayilari) * 1.2)
ax2.set_title("Dillere Göre Yorum Sayısı", fontsize=16, fontweight="bold")
ax2.set_xticklabels(diller, rotation=30, ha="right", fontsize=12, fontweight="bold")

# Çubukların üzerine değerleri ekleyelim
for i, yorum in enumerate(yorum_sayilari):
    ax2.text(i, yorum + 100, f"{yorum}", ha="center", fontsize=10, fontweight="bold", color="black")

# Grafiği kaydet
save_path = r"C:\Users\EXCALİBUR\OneDrive\Masaüstü\dil_yorum_grafik.png"
plt.savefig(save_path, dpi=300, bbox_inches='tight')

# Grafiği göster
plt.show()

print(f"Grafik başarıyla kaydedildi: {save_path}")
