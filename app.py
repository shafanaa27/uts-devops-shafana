print("=== PROGRAM JALAN ===")
import pandas as pd 
import os 

nilai_str = os.getenv('DATA_NILAI', '85,90,78,92,88') 
nilai = list(map(int, nilai_str.split(','))) 

data = {'Nilai': nilai} 
df = pd.DataFrame(data) 

print('Analisis Data') 
print(f"Rata-rata Nilai: {df['Nilai'].mean()}") 
print('selesai') 

#buat folder
os.makedirs('/app/output', exist_ok=True)

#simpan csv 
df.to_csv('/app/output/hasil.csv', index=False) 
print("hasil disimpan") 
print('selesai')
