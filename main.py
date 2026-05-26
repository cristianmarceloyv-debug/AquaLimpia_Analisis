import utils # Importa el archivo externo que creamos arriba

def main():
    print("1. Cargando datos...")
    ruta_archivo = "dataset_set_A_aguas_residuales.xlsx"
    df = utils.cargar_datos(ruta_archivo)
    
    print("2. Generando reportes para Operaciones y Ambiental...")
    # Llamamos a las funciones modulares
    df_operaciones = utils.generar_reporte_operaciones(df)
    df_ambiental = utils.generar_reporte_ambiental(df)
    
    print("3. Construyendo dashboard exploratorio...")
    # Esta línea es la que dispara la creación de los 4 gráficos
    utils.construir_dashboard(df)
    
    print("Análisis completado. Archivos guardados con éxito.")

if __name__ == "__main__":
    main()