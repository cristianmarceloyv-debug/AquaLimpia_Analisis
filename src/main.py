import utils # Importa el archivo externo 

def main():
    print("1. Cargando datos...")
    ruta_archivo = "dataset_set_A_aguas_residuales.xlsx"
    df = utils.cargar_datos(ruta_archivo)
    
    print("2. Generando reportes para Operaciones y Ambiental...")
    # funciones modulares
    df_operaciones = utils.generar_reporte_operaciones(df)
    df_ambiental = utils.generar_reporte_ambiental(df)
    
    print("3. Construyendo dashboard exploratorio...")
    # creación de los 4 gráficos
    utils.construir_dashboard(df)
    
    print("Análisis completado. Archivos guardados con éxito.")

if __name__ == "__main__":
    main()