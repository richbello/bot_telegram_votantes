import pandas as pd
from sqlalchemy import create_engine, text

ENGINE_URL = "postgresql://postgres:tu_contraseña@localhost:5432/campana_db"
engine = create_engine(ENGINE_URL)

def cargar_base_datos(archivo_excel):
    xls = pd.ExcelFile(archivo_excel)
    
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

    with engine.begin() as conn:
        df_votantes.to_sql('votantes', conn, if_exists='replace', index=False)
        conn.execute(text("ALTER TABLE votantes ADD PRIMARY KEY (cedula);"))
        conn.execute(text("CREATE INDEX idx_votantes_cedula ON votantes(cedula);"))

    print("? Base de datos importada exitosamente en PostgreSQL.")

if __name__ == '__main__':
    cargar_base_datos('puestos_votacion_prueba.xlsx')
