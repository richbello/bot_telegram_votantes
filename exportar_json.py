import pandas as pd
import json

def convertir_excel_a_json(archivo_excel):
    xls = pd.ExcelFile(archivo_excel)
    df = pd.read_excel(xls, sheet_name='Votantes')
    
    votantes_dict = {}
    for _, row in df.iterrows():
        cedula = str(row['NUIP']).strip()
        votantes_dict[cedula] = {
            "puesto": str(row['Puesto']),
            "mesa": int(row['Mesa']),
            "direccion": str(row['Dirección']),
            "municipio": str(row['Municipio']),
            "departamento": str(row['Departamento']),
            "latitud": float(row['Latitud']),
            "longitud": float(row['Longitud']),
            "estado": str(row['Estado'])
        }
        
    with open("votantes_data.json", "w", encoding="utf-8") as f:
        json.dump(votantes_dict, f, ensure_ascii=False, indent=2)
        
    print(f"🌐 'votantes_data.json' generado con {len(votantes_dict)} registros.")

if __name__ == '__main__':
    convertir_excel_a_json('puestos_votacion_prueba.xlsx')
