#%%
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

path = "profesiones.xlsx"

profesiones = pd.read_excel(path)

print(profesiones)
# %%

plt.bar(profesiones["Profesiones"], len(profesiones["Profesiones"]))
plt.bar(profesiones["Profesiones"], profesiones["Hombres"], 0.35, label='Hombres')
plt.bar(profesiones["Profesiones"], profesiones["Mujeres"], 0.35, label='Mujeres', alpha = 0.5)
plt.xlabel('Profesiones')
plt.ylabel('Diferencia Salarial')
plt.title('Brecha Salarial de Género Argentina Septiembre 2019')
plt.xticks(profesiones["Profesiones"], rotation = 35, ha = "right")
plt.legend()

plt.show()
# %%
