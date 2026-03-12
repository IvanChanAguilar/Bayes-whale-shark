import pandas as pd
import glob

# ✅ RUTA ACTUALIZADA (carpeta donde están tus archivos)
ruta = r"C:\carpeta con documentos de peces\peces*.csv"
print("Usando ruta:", ruta)

archivos = glob.glob(ruta)

print("Archivos encontrados:")
for a in archivos:
    print(a)

# ✅ Cargar los archivos CSV encontrados
dfs = []
for a in archivos:
    try:
        print(f"Leyendo archivo: {a}")
        df_temp = pd.read_csv(a, low_memory=False, on_bad_lines='skip')
        dfs.append(df_temp)
    except Exception as e:
        print(f"❌ Error en archivo: {a}")
        print(e)

# ✅ Unirlos en un solo DataFrame
df = pd.concat(dfs, ignore_index=True)
print("Total de registros cargados:", len(df))
# ✅ Guardar el DataFrame completo para uso rápido
df.to_pickle("peces_completo.pkl")
print("✅ DataFrame completo guardado como peces_completo.pkl")

# ✅ A) Tiburón ballena
mask_scientific = df.apply(
    lambda row: row.astype(str).str.contains("Rhincodon", case=False, na=False).any(),
    axis=1
)

mask_common = df.apply(
    lambda row: row.astype(str).str.contains("tibur", case=False, na=False).any(),
    axis=1
)

tiburon = df[mask_scientific | mask_common]
print("✅ Tiburón ballena encontrado. Registros:", len(tiburon))

# ✅ AQUÍ PEGAS EL CÓDIGO NUEVO
print(df.columns)

lat_col = "latitud"
lon_col = "longitud"

print("Columna de latitud detectada:", lat_col)
print("Columna de longitud detectada:", lon_col)

# ✅ Zona marina real del tiburón ballena
lat_min_tb, lat_max_tb = 21.70, 22.20
lon_min_tb, lon_max_tb = -87.50, -87.00

zona_tiburon = df[
    (df[lat_col] >= lat_min_tb) &
    (df[lat_col] <= lat_max_tb) &
    (df[lon_col] >= lon_min_tb) &
    (df[lon_col] <= lon_max_tb)
]

print("Registros en la zona marina del tiburón ballena:", len(zona_tiburon))
# ✅ C) Crear variables categóricas para Bayes

# Variable 1: ¿Es tiburón ballena?
df["es_tiburon"] = df.apply(
    lambda row: "si" if (
        "rhincodon" in str(row).lower() or
        "tibur" in str(row).lower()
    ) else "no",
    axis=1
)

# Variable 2: ¿Está en Holbox?
df["esta_en_holbox"] = df.apply(
    lambda row: "si" if (
        21.45 <= row["latitud"] <= 21.60 and
        -87.40 <= row["longitud"] <= -87.25
    ) else "no",
    axis=1
)

print("✅ Variables categóricas creadas:")
print(df[["es_tiburon", "esta_en_holbox"]].head())
# ✅ B) Filtrar registros dentro de Holbox (zona costera)
lat_min, lat_max = 21.45, 21.60
lon_min, lon_max = -87.40, -87.25

holbox = df[
    (df[lat_col] >= lat_min) &
    (df[lat_col] <= lat_max) &
    (df[lon_col] >= lon_min) &
    (df[lon_col] <= lon_max)
]

print("Registros dentro de Holbox:", len(holbox))


holbox.to_csv("peces_holbox_final.csv", index=False)
print("✅ Archivo final guardado como peces_holbox_final.csv")