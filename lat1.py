import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca file CSV
data = pd.read_csv('nilai_siswa.csv')

# Menampilkan informasi dasar
print(data.info())
print(data.head())
print(data.describe())

# Statistik dasar
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

# 🔹 Menampilkan nilai untuk setiap mata pelajaran
print("\n===== Nilai per Mata Pelajaran =====")
for mapel in data['Matpel'].unique():
    print(f"\nNilai {mapel}:")
    nilai_mapel = data[data['Matpel'] == mapel]
    print(nilai_mapel)

# 🔹 Nilai maksimum & minimum per mapel
print("\n===== Nilai maksimum dan minimum per mata pelajaran =====")
print(data.groupby('Matpel')['Nilai'].agg(['max', 'min']))

# 🔹 Grafik batang rata-rata nilai per mapel
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar', color='lightblue', edgecolor='black')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

# 🔹 Boxplot
sns.boxplot(x='Matpel', y='Nilai', data=data, palette='Set2')
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()
