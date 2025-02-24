import pandas as pd


archivo_excel = "rfm.xlsx"  
hoja = "Base"  

df = pd.read_excel(archivo_excel, sheet_name=hoja)

columna = "Recencia"
datos = df[columna].dropna()

no_ceros = datos[datos > 0]

# Determinar el número de bins (mínimo 2, máximo 5)
num_bins = min(5, no_ceros.nunique())

# Calcular los Cuartil solo para valores > 0
cuartiles = pd.qcut(no_ceros, q=num_bins, duplicates="drop")


labels = list(range(1, num_bins + 1))

if len(labels) > num_bins - 1:
    labels = list(range(1, num_bins))


df["Quintil Renencia"] = pd.qcut(df[columna], q=num_bins, labels=labels, duplicates="drop")


df["Quintil Renencia"] = df["Quintil Renencia"].astype("object")


df.loc[df[columna] == 0, "Quintil Renencia"] = 0


with pd.ExcelWriter(archivo_excel, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    df.to_excel(writer, sheet_name=hoja, index=False)

print("Cuartiles agregados al archivo original (0s en grupo separado).")