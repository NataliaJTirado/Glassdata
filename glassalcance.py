import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

df = pd.read_csv('Alcance Facebook _ Instagram - Alcance.csv.csv',header=1)
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')

# Verifica que todas las filas tengan valores válidos en la columna de fecha
df = df.dropna(subset=['Fecha'])

# Define el rango de fechas

start_date_pre_publicidad = pd.Timestamp('2024-09-09')
end_date_pre_publicidad = pd.Timestamp('2024-10-21')

# Filtra los datos que estén dentro del rango de fechas
face_organico = df[(df['Fecha'] >= start_date_pre_publicidad ) &
                    (df['Fecha'] <= end_date_pre_publicidad ) &
                    (df['Red de alcance'] == 'Facebook')]

ig_organico = df[(df['Fecha'] >= start_date_pre_publicidad ) &
                    (df['Fecha'] <= end_date_pre_publicidad ) &
                    (df['Red de alcance'] == 'Instagram')]

face_organico_prom = face_organico[face_organico['Red de alcance'] == 'Facebook']['Cantidad'].mean()
ig_organico_prom = ig_organico[ig_organico['Red de alcance'] == 'Instagram']['Cantidad'].mean()

print("Alcance promedio antes de pagar publicidad en Facebook",face_organico_prom)
print("Alcance promedio antes de pagar publicidad en Instagram",ig_organico_prom,"\n")

start_date_publicidad = pd.Timestamp('2024-10-22')
end_date_publicidad = pd.Timestamp('2024-10-27')

# Filtra los datos que estén dentro del rango de fechas
fechas_pagadas_face = df[(df['Fecha'] >= start_date_publicidad) &
                    (df['Fecha'] <= end_date_publicidad) &
                    (df['Red de alcance'] == 'Facebook')]

fechas_pagadas_ig = df[(df['Fecha'] >= start_date_publicidad) &
                    (df['Fecha'] <= end_date_publicidad) &
                    (df['Red de alcance'] == 'Instagram')]

facebook_prom = fechas_pagadas_face[fechas_pagadas_face['Red de alcance'] == 'Facebook']['Cantidad'].mean()
ig_prom = fechas_pagadas_ig[fechas_pagadas_ig['Red de alcance'] == 'Instagram']['Cantidad'].mean()

print("Alcance promedio mientras se pago publicidad en Facebook",facebook_prom)
print("Alcance promedio mientras se pago publicidad en Instagram",ig_prom,"\n")

start_date_post_publicidad = pd.Timestamp('2024-10-27')
end_date_post_publicidad = pd.Timestamp('2024-11-15')

face_post_publicidad = df[(df['Fecha'] >= start_date_post_publicidad) &
                    (df['Fecha'] <= end_date_post_publicidad) &
                    (df['Red de alcance'] == 'Facebook')]

ig_post_publicidad = df[(df['Fecha'] >= start_date_post_publicidad) &
                    (df['Fecha'] <= end_date_post_publicidad) &
                    (df['Red de alcance'] == 'Instagram')]

post_facebook_prom = face_post_publicidad[face_post_publicidad['Red de alcance'] == 'Facebook']['Cantidad'].mean()
post_ig_prom = ig_post_publicidad[ig_post_publicidad['Red de alcance'] == 'Instagram']['Cantidad'].mean()

print("Alcance promedio despues de que se pago publicidad en Facebook",post_facebook_prom)
print("Alcance promedio despues de que se pago publicidad en Instagram",post_ig_prom)

# Calcula el cambio porcentual para Facebook
facebook_percentage_change = ((facebook_prom - face_organico_prom) / face_organico_prom) * 100

# Calcula el cambio porcentual para Instagram
instagram_percentage_change = ((ig_prom - ig_organico_prom) / ig_organico_prom) * 100

# Verifica si el incremento fue mayor o igual al 20%
facebook_increase = facebook_percentage_change >= 20
instagram_increase = instagram_percentage_change >= 20

# Imprime los resultados
print(f"Cambio porcentual en Facebook: {facebook_percentage_change:.2f}%")
print(f"¿El alcance en Facebook aumentó en un 20% o más? {'Sí' if facebook_increase else 'No'}\n")

print(f"Cambio porcentual en Instagram: {instagram_percentage_change:.2f}%")
print(f"¿El alcance en Instagram aumentó en un 20% o más? {'Sí' if instagram_increase else 'No'}")

import matplotlib.pyplot as plt

# Datos para el gráfico de barras
labels = ['Pre-Publicidad', 'Publicidad', 'Post-Publicidad']
facebook_means = [face_organico_prom, facebook_prom, post_facebook_prom]
instagram_means = [ig_organico_prom, ig_prom, post_ig_prom]

# Cálculo de los cambios porcentuales
facebook_percentage_change = ((facebook_prom - face_organico_prom) / face_organico_prom) * 100
instagram_percentage_change = ((ig_prom - ig_organico_prom) / ig_organico_prom) * 100

# Crear el gráfico de barras
fig, ax = plt.subplots()
bar_width = 0.4
x = range(len(labels))

# Barras para Facebook
facebook_bars = ax.bar(x, facebook_means, bar_width, label='Facebook')

# Barras para Instagram (desplazadas a la derecha)
instagram_bars = ax.bar([p + bar_width for p in x], instagram_means, bar_width, label='Instagram')

# Etiquetas y personalización
ax.set_xlabel('Etapa de Publicidad')
ax.set_ylabel('Alcance Promedio')
ax.set_title('Comparación del Alcance Promedio por Etapa de Publicidad')
ax.set_xticks([p + bar_width / 2 for p in x])
ax.set_xticklabels(labels)
ax.legend()

# Agregar anotaciones para el cambio porcentual
for i, bar in enumerate(facebook_bars):
    if i == 1:  # Anotación para "Publicidad"
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 100,  # Altura ajustada para que no tape la barra
            f'{facebook_percentage_change:.2f}% {"↑" if facebook_percentage_change >= 20 else "↓"}',
            ha='center',
            fontsize=10,
            color='green' if facebook_percentage_change >= 20 else 'red'
        )

for i, bar in enumerate(instagram_bars):
    if i == 1:  # Anotación para "Publicidad"
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 100,
            f'{instagram_percentage_change:.2f}% {"↑" if instagram_percentage_change >= 20 else "↓"}',
            ha='center',
            fontsize=10,
            color='green' if instagram_percentage_change >= 20 else 'red'
        )

# Mostrar el gráfico
plt.show()



