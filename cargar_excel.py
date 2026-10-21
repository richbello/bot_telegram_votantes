import pandas as pd
from sqlalchemy import create_engine, text
import os

# Configuración de base de datos (SQLite por defecto para desarrollo o PostgreSQL para producción)
DB_PATH = "sqlite:///campana_votantes.db"
engine = create_engine(DB_PATH)

def procesar_y_cargar_excel(archivo_excel):
    if not os.path.exists(archivo_excel):
        print(f"❌ El archivo {archivo_excel} no existe en esta carpeta.")
        return

    print(f"📂 Procesando archivo: {archivo_excel}...")
    xls = pd.ExcelFile(archivo_excel)

    # 1. Cargar y procesar la hoja 'Puestos'
    if 'Puestos' in xls.sheet_names:
        df_puestos = pd.read_excel(xls, sheet_name='Puestos')
        df_puestos = df_puestos.rename(columns={
            'ID puesto': 'id_puesto',
            'Puesto': 'puesto_nombre',
            'Dirección': 'direccion',
            'Municipio': 'municipio',
            'Departamento': 'departamento',
            'Latitud': 'latitud',
            'Longitud': 'longitud',
            'Personas': 'total_personas',
            'Mesas distintas': 'total_mesas'
        })
        df_puestos = df_puestos[['id_puesto', 'puesto_nombre', 'direccion', 'municipio', 'departamento', 'latitud', 'longitud', 'total_personas', 'total_mesas']]
        
        with engine.begin() as conn:
            df_puestos.to_sql('puestos_votacion', conn, if_exists='replace', index=False)
        print("✅ Tabla 'puestos_votacion' sincronizada.")

    # 2. Cargar y procesar la hoja 'Votantes'
    if 'Votantes' in xls.sheet_names:
        df_votantes = pd.read_excel(xls, sheet_name='Votantes')
        df_votantes = df_votantes.rename(columns={
            'NUIP': 'cedula',
            'Departamento': 'departamento',
            'Municipio': 'municipio',
            'Puesto': 'puesto_nombre',
            'Dirección': 'direccion',
            'Mesa': 'mesa',
            'Latitud': 'latitud',
            'Longitud': 'longitud',
            'Estado': 'estado',
            'ID puesto': 'id_puesto'
        })
        
        # Limpieza de datos
        df_votantes['cedula'] = df_votantes['cedula'].astype(str).str.strip()
        df_votantes = df_votantes.drop_duplicates(subset=['cedula'], keep='last')

        with engine.begin() as conn:
            # Reemplaza o inserta registros
            df_votantes.to_sql('votantes', conn, if_exists='replace', index=False)
            
            # Crear índice para búsquedas ultra rápidas por cédula
            conn.execute(text("CREATE UNIQUE INDEX IF NOT EXISTS idx_votantes_cedula ON votantes(cedula);"))
            
        print(f"✅ Se cargaron {len(df_votantes)} votantes exitosamente.")

if __name__ == '__main__':
    archivo = 'puestos_votacion_prueba.xlsx'
    procesar_y_cargar_excel(archivo)
