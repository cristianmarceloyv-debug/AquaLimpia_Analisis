import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cargar_datos(ruta):
    # Lee el archivo Excel correctamente
    return pd.read_excel(ruta) 

def generar_reporte_operaciones(df):
    cols = ['fecha_registro', 'planta', 'caudal_entrada_m3_d', 'DBO_entrada_mg_L', 
            'DBO_salida_mg_L', 'energia_aeracion_kWh', 'lodos_generados_kg_d']
    df_ops = df[cols].copy()
    df_ops.to_csv('reporte_operaciones.csv', index=False)
    return df_ops

def generar_reporte_ambiental(df):
    cols = ['fecha_registro', 'planta', 'DBO_salida_mg_L', 'cumplimiento_norma']
    df_amb = df[cols].copy()
    df_amb.to_csv('reporte_ambiental.csv', index=False)
    return df_amb

def construir_dashboard(df):
    # Aquí están los 4 gráficos encapsulados en una función modular
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    sns.boxplot(data=df, x='planta', y='DBO_salida_mg_L', ax=axes[0,0], palette="Set2")
    axes[0,0].set_title('Distribución de DBO de Salida por Planta')
    
    sns.scatterplot(data=df, x='caudal_entrada_m3_d', y='DBO_salida_mg_L', hue='planta', ax=axes[0,1])
    axes[0,1].set_title('Caudal de Entrada vs DBO Salida')
    
    sns.countplot(data=df, x='planta', hue='cumplimiento_norma', ax=axes[1,0], palette="viridis")
    axes[1,0].set_title('Cumplimiento Normativo (0=No, 1=Sí)')
    
    df['fecha_dt'] = pd.to_datetime(df['fecha_registro'])
    sns.lineplot(data=df.sort_values('fecha_dt'), x='fecha_registro', y='energia_aeracion_kWh', hue='planta', ax=axes[1,1])
    axes[1,1].set_title('Consumo de Energía a lo largo del tiempo')
    axes[1,1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('dashboard_exploratorio.png')