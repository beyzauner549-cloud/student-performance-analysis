import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print(df.head())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("StudentsPerformance.csv")

# İlk 5 satır
print(df.head())

# 1 - Çizgi Grafiği (math score)
plt.figure(figsize=(8,4))
plt.plot(df['math score'])
plt.title("Math Score Line Plot")
plt.xlabel("Index")
plt.ylabel("Math Score")
plt.show()
print("Yorum: Çizgi grafiğinde öğrencilerin matematik puanlarının dalgalı bir dağılım gösterdiği görülmektedir.")

# 2 - Dağılım Grafiği (math vs reading)
plt.figure(figsize=(8,4))
plt.scatter(df['math score'], df['reading score'])
plt.title("Math vs Reading Scatter Plot")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.show()
print("Yorum: Matematik ve okuma puanları arasında genel olarak pozitif bir ilişki vardır.")

# 3 - Bar Grafiği (Parental Education)
plt.figure(figsize=(8,4))
df['parental level of education'].value_counts().plot(kind='bar')
plt.title("Parental Education Bar Plot")
plt.xlabel("Education Level")
plt.ylabel("Count")
plt.show()
print("Yorum: En çok görülen ebeveyn eğitim seviyesi 'some college' ve 'associate’s degree'dir.")

# 4 - Korelasyon Isı Haritası
plt.figure(figsize=(8,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()
print("Yorum: Math, reading ve writing puanlarının birbirleriyle yüksek korelasyona sahip olduğu gözlenmektedir.")

# 5 - Pasta Grafiği (Gender)
plt.figure(figsize=(6,6))
df['gender'].value_counts().plot(kind='pie', autopct="%1.1f%%")
plt.title("Gender Distribution Pie Chart")
plt.ylabel("")
plt.show()
print("Yorum: Veri setindeki kız ve erkek öğrenci oranları dengeli bir dağılım göstermektedir.")
import folium

# 4a - Türkiye merkezli harita
m = folium.Map(location=[38.5, 34.5], zoom_start=6)

# 4b - Markerlar
folium.Marker(
    location=[41.38871, 33.78273],
    popup="Kastamonu Şube",
    tooltip="Kastamonu",
    icon=folium.Icon(color="blue")
).add_to(m)

folium.Marker(
    location=[40.74104, 30.33129],
    popup="Sakarya Şube",
    tooltip="Sakarya",
    icon=folium.Icon(color="green")
).add_to(m)

folium.Marker(
    location=[37.0000, 35.3213],
    popup="Adana Şube",
    tooltip="Adana",
    icon=folium.Icon(color="red")
).add_to(m)

# 4c - Polyline rota
coords = [
    [40.74104, 30.33129],  # Sakarya
    [41.38871, 33.78273],  # Kastamonu
    [37.0000, 35.3213]     # Adana
]

folium.PolyLine(coords, color="blue", weight=4).add_to(m)

# 4d - Konya şehrinin etrafına Circle ekleme
folium.Circle(
    location=[37.874642, 32.493155],
    radius=40000,  # 40 km
    color='red',
    fill=True,
    fill_color='red',
    fill_opacity=0.3,
    popup="Konya Bölgesi (40 km)"
).add_to(m)

# haritayı kaydet
m.save("turkiye_harita.html")
print("Harita başarıyla oluşturuldu: turkiye_harita.html")
