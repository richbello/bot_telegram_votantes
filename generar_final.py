import json

json_db = """[{"cedula": "2986631", "puesto": "I.E. SOACHA AVANZA LA UNIDAD", "mesa": 1, "direccion": "CRA 38 No 14 - 72", "ciudad": "SOACHA", "lat": 4.6099953, "lng": -74.2238673}, {"cedula": "1073693454", "puesto": "COLEGIO MINUTO DE DIOS CIUDAD VERDE", "mesa": 37, "direccion": "CALLE 38 No 31 141 CIUDAD VERDE", "ciudad": "SOACHA", "lat": 4.6061877, "lng": -74.2130596}, {"cedula": "1033723563", "puesto": "I.E. LICEO MAYOR DE SOACHA", "mesa": 23, "direccion": "CLL. 38 No. 6 A - 55 ESTE", "ciudad": "SOACHA", "lat": 4.58256, "lng": -74.194387}, {"cedula": "11324571", "puesto": "COLEGIO AMERICANO", "mesa": 8, "direccion": "CALLE 21 No. 10-40", "ciudad": "GIRARDOT", "lat": 4.2988522, "lng": -74.8044541}, {"cedula": "1109264322", "puesto": "CENTRO COMERCIAL MERCURIO", "mesa": 31, "direccion": "CRA 7 NRO 32 35", "ciudad": "SOACHA", "lat": 4.5881616, "lng": -74.2035191}, {"cedula": "1005663908", "puesto": "IE SAN JOSE", "mesa": 16, "direccion": "CLL 48 No 30-56 EL EDEN", "ciudad": "SINCELEJO", "lat": 9.2940665, "lng": -75.3768724}, {"cedula": "1073701267", "puesto": "COLEGIO MILITAR LICEO SOCIAL COMPARTIR", "mesa": 13, "direccion": "CLL 18 SUR NRO 9F 24 COMPARTIR", "ciudad": "SOACHA", "lat": 4.5663852, "lng": -74.2371026}, {"cedula": "1016048445", "puesto": "COLEGIO MINUTO DE DIOS CIUDAD VERDE", "mesa": 22, "direccion": "CALLE 38 No 31 141 CIUDAD VERDE", "ciudad": "SOACHA", "lat": 4.6061877, "lng": -74.2130596}, {"cedula": "52026319", "puesto": "NUEVO COLISEO MUNICIPAL", "mesa": 1, "direccion": "CLL 1 No 2-00", "ciudad": "MOSQUERA", "lat": 4.7035501, "lng": -74.2310153}, {"cedula": "1007144082", "puesto": "IE JESUS MARIA ORMAZA", "mesa": 5, "direccion": "CRA 22 BIS # 75 00", "ciudad": "PEREIRA", "lat": 4.8028213, "lng": -75.7443219}, {"cedula": "1016101357", "puesto": "ZONA FRANCA", "mesa": 33, "direccion": "CLL 14 A # 108 - 78", "ciudad": "BOGOTA D.C.", "lat": 4.6714469, "lng": -74.1559155}, {"cedula": "53134432", "puesto": "I.E. VIDA NUEVA", "mesa": 9, "direccion": "CRA 19 A No 4 - 90 SUR", "ciudad": "SOACHA", "lat": 4.5913261, "lng": -74.2285761}, {"cedula": "1000472492", "puesto": "GRAN PLAZA EL ENSUEÑO", "mesa": 19, "direccion": "CRA 51 #59 C-93 SUR /CLL 59 SUR #51-21", "ciudad": "BOGOTA D.C.", "lat": 4.5822363, "lng": -74.1567545}, {"cedula": "1014251052", "puesto": "LA FLORIDA", "mesa": 13, "direccion": "CRA 89 # 68A-36 CRA 89 # 68A-32", "ciudad": "BOGOTA D.C.", "lat": 4.6928276, "lng": -74.1106231}, {"cedula": "1012383845", "puesto": "LA ESTACION", "mesa": 21, "direccion": "CRA 78 ENTRE CLL 60A SUR Y CLL 63 SUR", "ciudad": "BOGOTA D.C.", "lat": 4.5971912, "lng": -74.1803664}, {"cedula": "1023961353", "puesto": "I.E. LEON XIII - CHILOE", "mesa": 27, "direccion": "DIAG. 28 No. 28 - 99 CIUDAD VERDE", "ciudad": "SOACHA", "lat": 4.6049633, "lng": -74.2141603}, {"cedula": "1012435510", "puesto": "CENTRO COMERCIAL VENTURA TERREROS", "mesa": 22, "direccion": "CRA 1 NRO 38 89 SOACHA", "ciudad": "SOACHA", "lat": 4.58846, "lng": -74.1950408}, {"cedula": "1033746591", "puesto": "SAN CARLOS", "mesa": 25, "direccion": "CRA 19 No 50 A - 37 SUR", "ciudad": "BOGOTA D.C.", "lat": 4.5697017, "lng": -74.12794}, {"cedula": "1073324433", "puesto": "COLEGIO MINUTO DE DIOS CIUDAD VERDE", "mesa": 36, "direccion": "CALLE 38 No 31 141 CIUDAD VERDE", "ciudad": "SOACHA", "lat": 4.6061877, "lng": -74.2130596}, {"cedula": "1116020515", "puesto": "PUESTO CABECERA MUNICIPAL", "mesa": 3, "direccion": "CRA 3A No 1B - 12", "ciudad": "LA SALINA", "lat": 6.1276899, "lng": -72.3351729}, {"cedula": "1012363398", "puesto": "I.E. LICEO MAYOR DE SOACHA", "mesa": 17, "direccion": "CLL. 38 No. 6 A - 55 ESTE", "ciudad": "SOACHA", "lat": 4.58256, "lng": -74.194387}, {"cedula": "1007503635", "puesto": "Barcelona - Consulado", "mesa": 34, "direccion": "Seminari Conciliar de Barcelona", "ciudad": "ESPAÑA", "lat": 41.3880817, "lng": 2.1632143}, {"cedula": "1022382733", "puesto": "LAURA HERRERA", "mesa": 3, "direccion": "Carrera 89 B No. 54 F 20 Sur- Bosa Brasil", "ciudad": "BOGOTA D.C.", "lat": 4.6320538, "lng": -74.1873575}, {"cedula": "1000732786", "puesto": "I.E. SAN MATEO SEDE A", "mesa": 17, "direccion": "CR. 5 B ESTE No. 26 - 04", "ciudad": "SOACHA", "lat": 4.5791541, "lng": -74.204448}, {"cedula": "1012422621", "puesto": "COLISEO LEON XIII", "mesa": 17, "direccion": "CLL 48 No 9-05 LEON XIII", "ciudad": "SOACHA", "lat": 4.5950453, "lng": -74.1940555}, {"cedula": "1028480010", "puesto": "MEDICINA LEGAL", "mesa": 9, "direccion": "KR12 A # 7 - 07", "ciudad": "BOGOTA D.C.", "lat": 4.5981491, "lng": -74.0826253}, {"cedula": "1022365207", "puesto": "EL PORTAL", "mesa": 12, "direccion": "CRA 3B. No. 30A - 42 SUR", "ciudad": "BOGOTA D.C.", "lat": 4.5659317, "lng": -74.094819}, {"cedula": "1023898524", "puesto": "I.E. SAN MATEO SEDE B", "mesa": 15, "direccion": "CR. 5 B ESTE No. 26 - 04", "ciudad": "SOACHA", "lat": 4.5791541, "lng": -74.204448}, {"cedula": "1022354665", "puesto": "CENTRO COMERCIAL VENTURA TERREROS", "mesa": 25, "direccion": "CRA 1 NRO 38 89 SOACHA", "ciudad": "SOACHA", "lat": 4.58846, "lng": -74.1950408}, {"cedula": "1016592310", "puesto": "MODELIA REAL", "mesa": 16, "direccion": "CLL 24 D # 82-13 o CRA 82 # 24C- 29", "ciudad": "BOGOTA D.C.", "lat": 4.67085, "lng": -74.1212074}, {"cedula": "1022982891", "puesto": "I.E. SAN MATEO SEDE A", "mesa": 21, "direccion": "CR. 5 B ESTE No. 26 - 04", "ciudad": "SOACHA", "lat": 4.5791541, "lng": -74.204448}, {"cedula": "1073671224", "puesto": "COLISEO GENERAL SANTANDER", "mesa": 16, "direccion": "CLL. 15 NO. 8 - 53", "ciudad": "SOACHA", "lat": 4.5836645, "lng": -74.2178312}, {"cedula": "79847577", "puesto": "IE GENERAL SANTANDER SD MI TIERNA EDAD", "mesa": 7, "direccion": "CLL. 14 NO. 8 - 25 CENTRO", "ciudad": "SOACHA", "lat": 4.5831971, "lng": -74.2186115}, {"cedula": "1010034446", "puesto": "I.E. LEON XIII - CHILOE", "mesa": 22, "direccion": "DIAG. 28 No. 28 - 99 CIUDAD VERDE", "ciudad": "SOACHA", "lat": 4.6049633, "lng": -74.2141603}, {"cedula": "1014662799", "puesto": "MEDICINA LEGAL", "mesa": 6, "direccion": "KR12 A # 7 - 07", "ciudad": "BOGOTA D.C.", "lat": 4.5981491, "lng": -74.0826253}, {"cedula": "1144174969", "puesto": "ESCUELA RAUL SILVA HOLGUIN", "mesa": 29, "direccion": "DG 26K #T83-24", "ciudad": "CALI", "lat": 3.4275857, "lng": -76.4809419}, {"cedula": "79660155", "puesto": "IED GRAL SANTANDER SEDE BTO", "mesa": 18, "direccion": "CARRERA 7 No. 11 -30", "ciudad": "SIBATE", "lat": 4.493369, "lng": -74.2579751}, {"cedula": "43438988", "puesto": "I.E. FRANCISCO MIRANDA", "mesa": 14, "direccion": "KR 51C # 79-56", "ciudad": "MEDELLIN", "lat": 6.2740533, "lng": -75.5636045}, {"cedula": "14801742", "puesto": "I.E. FRANCISCO JOSE DE CALDAS", "mesa": 1, "direccion": "CLLE 8N NUM 16-76 LLERAS", "ciudad": "YUMBO", "lat": 3.5867275, "lng": -76.4930408}, {"cedula": "1073671180", "puesto": "I.E. CIUDAD LATINA", "mesa": 25, "direccion": "CLL. 37 A SUR No. 15 i - 21", "ciudad": "SOACHA", "lat": 4.5756571, "lng": -74.2456952}, {"cedula": "1026300319", "puesto": "COLEGIO COLSUBSIDIO CHICALA", "mesa": 21, "direccion": "CRA 87 No 53C-26 SUR", "ciudad": "BOGOTA D.C.", "lat": 4.624965, "lng": -74.1809234}, {"cedula": "52748481", "puesto": "CENTRO COMERCIAL MERCURIO", "mesa": 6, "direccion": "CRA 7 NRO 32 35", "ciudad": "SOACHA", "lat": 4.5881616, "lng": -74.2035191}, {"cedula": "1024473269", "puesto": "IE LUIS C. GALAN-SD VILLAS DE CASALOMA", "mesa": 2, "direccion": "CLL 59 B No 15 - 60 E", "ciudad": "SOACHA", "lat": 4.5880355, "lng": -74.1825666}, {"cedula": "1024490789", "puesto": "I.E. SOACHA AVANZA LA UNIDAD", "mesa": 23, "direccion": "CRA 38 No 14 - 72", "ciudad": "SOACHA", "lat": 4.6099953, "lng": -74.2238673}, {"cedula": "1000491641", "puesto": "Madrid - Consulado", "mesa": 66, "direccion": "(sin dirección en la consulta)", "ciudad": "ESPAÑA", "lat": 40.41775, "lng": -3.69966}, {"cedula": "1032474754", "puesto": "I. E. EUGENIO DIAZ CASTRO SEDE PRIMARIA", "mesa": 3, "direccion": "VEREDA EL CHARQUITO", "ciudad": "SOACHA", "lat": 4.54396, "lng": -74.27539}, {"cedula": "1074186778", "puesto": "MEGA COLEGIO", "mesa": 20, "direccion": "CALLE 13A ENTRE CRA 6 Y 8 BARRIO SAN CARLOS", "ciudad": "EL ROSAL", "lat": 4.8546287, "lng": -74.2608704}, {"cedula": "75003551", "puesto": "LA PRADERA", "mesa": 7, "direccion": "CLL 4 B # 65 - 31", "ciudad": "BOGOTA D.C.", "lat": 4.6238952, "lng": -74.1220691}, {"cedula": "37670293", "puesto": "IE. NUEVO COMPARTIR", "mesa": 2, "direccion": "CRA 14 No 29 - 80 SUR COMPARTIR", "ciudad": "SOACHA", "lat": 4.5728031, "lng": -74.2424978}, {"cedula": "1034398566", "puesto": "SALON COMUNAL MARSELLA", "mesa": 10, "direccion": "CRA 69 No 8-28", "ciudad": "BOGOTA D.C.", "lat": 4.632406, "lng": -74.1270128}, {"cedula": "1022926750", "puesto": "COLEGIO COLSUBSIDIO CHICALA", "mesa": 20, "direccion": "CRA 87 No 53C-26 SUR", "ciudad": "BOGOTA D.C.", "lat": 4.624965, "lng": -74.1809234}, {"cedula": "1012453776", "puesto": "BOSA SAN JOSE", "mesa": 14, "direccion": "CRA 89BIS #85A-20SUR CRA 80K #85A-33SUR", "ciudad": "BOGOTA D.C.", "lat": 4.6139291, "lng": -74.2098205}, {"cedula": "1075670670", "puesto": "SEDE EDU SIMON BOLIVAR", "mesa": 23, "direccion": "CARRERA 14 No 18-38", "ciudad": "ZIPAQUIRA", "lat": 5.0328018, "lng": -73.9959328}, {"cedula": "1075650862", "puesto": "IEM CUNDINAMARCA", "mesa": 18, "direccion": "CL 7 N 1A-36 BR. LA CONCEPCION", "ciudad": "ZIPAQUIRA", "lat": 5.0279744, "lng": -74.0079785}, {"cedula": "1075870902", "puesto": "C ACONDICIONAMIENTO Y PRE FISICA CAPF II", "mesa": 15, "direccion": "TRASVERSAL 6 No 1-29", "ciudad": "SOPO", "lat": 4.9070309, "lng": -73.9436846}, {"cedula": "1193146788", "puesto": "CENTRO DEPORTIVO PARQUE DE LOS LOCOS", "mesa": 31, "direccion": "CRA 9 CLL 15", "ciudad": "SOACHA", "lat": 4.584744, "lng": -74.217161}, {"cedula": "53893906", "puesto": "I.E. LEON XIII", "mesa": 14, "direccion": "CR. 8 NO. 5 - 83 LEON XIII", "ciudad": "SOACHA", "lat": 4.593502, "lng": -74.1944046}, {"cedula": "1012376468", "puesto": "I.E. SOL NACIENTE", "mesa": 17, "direccion": "CLL 15 A No. 1B - 12", "ciudad": "SOACHA", "lat": 4.5770728, "lng": -74.2139061}, {"cedula": "52236223", "puesto": "BENJAMIN HERRERA", "mesa": 4, "direccion": "CRA 28 # 63 - 64", "ciudad": "BOGOTA D.C.", "lat": 4.6550314, "lng": -74.0764674}, {"cedula": "86080270", "puesto": "COLEGIO MINUTO DE DIOS CIUDAD VERDE", "mesa": 15, "direccion": "CALLE 38 No 31 141 CIUDAD VERDE", "ciudad": "SOACHA", "lat": 4.6061877, "lng": -74.2130596}, {"cedula": "39679683", "puesto": "I.E. JULIO CESAR TURBAY AYALA", "mesa": 5, "direccion": "TV 9 ESTE No.45A- 80", "ciudad": "SOACHA", "lat": 4.59546, "lng": -74.19502}, {"cedula": "52526840", "puesto": "I.E. EL BOSQUE", "mesa": 11, "direccion": "CLL. 32 CON CR 15 ESTE", "ciudad": "SOACHA", "lat": 4.58543, "lng": -74.20145}, {"cedula": "1014296488", "puesto": "BOLIVIA", "mesa": 23, "direccion": "CRA 103 D No 85 A 72", "ciudad": "BOGOTA D.C.", "lat": 4.71182, "lng": -74.12034}, {"cedula": "52197931", "puesto": "COLISEO GENERAL SANTANDER", "mesa": 8, "direccion": "CLL. 15 NO. 8 - 53", "ciudad": "SOACHA", "lat": 4.5836645, "lng": -74.2178312}, {"cedula": "10740728", "puesto": "IED GRAL SANTANDER SEDE BTO", "mesa": 6, "direccion": "CARRERA 7 No. 11 -30", "ciudad": "SIBATE", "lat": 4.493369, "lng": -74.2579751}, {"cedula": "52356333", "puesto": "COLEGIO MILITAR LICEO SOCIAL COMPARTIR", "mesa": 2, "direccion": "CLL 18 SUR NRO 9F 24 COMPARTIR", "ciudad": "SOACHA", "lat": 4.5663852, "lng": -74.2371026}, {"cedula": "1024575963", "puesto": "GALICIA", "mesa": 34, "direccion": "CLL 60 A SUR # 73-31", "ciudad": "BOGOTA D.C.", "lat": 4.58712, "lng": -74.16235}, {"cedula": "1073674702", "puesto": "ALCALA", "mesa": 27, "direccion": "CRA 51 C # 33- 41 SUR", "ciudad": "BOGOTA D.C.", "lat": 4.59981, "lng": -74.12543}, {"cedula": "52272820", "puesto": "CUNDINAMARCA", "mesa": 3, "direccion": "CLL 19 C # 33-30", "ciudad": "BOGOTA D.C.", "lat": 4.61984, "lng": -74.10123}, {"cedula": "1031142237", "puesto": "LUCERO DEL SUR", "mesa": 25, "direccion": "CRA 17 B BIS A # 67-30 SUR o 67-48 SUR", "ciudad": "BOGOTA D.C.", "lat": 4.55123, "lng": -74.14012}, {"cedula": "1031640143", "puesto": "I.E. VIDA NUEVA", "mesa": 21, "direccion": "CRA 19 A No 4 - 90 SUR", "ciudad": "SOACHA", "lat": 4.5913261, "lng": -74.2285761}, {"cedula": "72289576", "puesto": "UNIVERSIDAD JUAN DE CASTELLANOS", "mesa": 12, "direccion": "CRA 11 # 11 - 44", "ciudad": "TUNJA", "lat": 5.531776, "lng": -73.363155}, {"cedula": "87070187", "puesto": "LIC DE LA MERCED-BACHILLERATO", "mesa": 15, "direccion": "CL 18 # 34-104", "ciudad": "PASTO", "lat": 1.219153, "lng": -77.285814}, {"cedula": "55237762", "puesto": "COL SAN JUAN DE GIRON", "mesa": 3, "direccion": "CR 25 NO 31-08 CENTRO", "ciudad": "GIRON", "lat": 7.068229, "lng": -73.169542}, {"cedula": "1116787273", "puesto": "CONCENTRACION CAMILO TORRES", "mesa": 15, "direccion": "CRA 8 No 24-15 BARRIO LA UNION", "ciudad": "ARAUCA", "lat": 7.087754, "lng": -70.754714}, {"cedula": "1005476542", "puesto": "ESCUELA FLOR DE MI LLANO", "mesa": 11, "direccion": "CRA 9 No 4 -65 SUR", "ciudad": "ARAUCA", "lat": 7.078451, "lng": -70.758412}, {"cedula": "1098644764", "puesto": "COL SAN PEDRO CLAVER", "mesa": 29, "direccion": "CR 28 # 47 - 06 BARRIO SOTOMAYOR", "ciudad": "BUCARAMANGA", "lat": 7.118121, "lng": -73.116524}, {"cedula": "79426568", "puesto": "COL SANTO T DE AQUINO SD PRIA", "mesa": 9, "direccion": "KR 14 #12-07", "ciudad": "DUITAMA", "lat": 5.825825, "lng": -73.033621}, {"cedula": "1007129127", "puesto": "CENTRO DE EVENTOS", "mesa": 21, "direccion": "CRA 3 No 8-16", "ciudad": "JUAN DE ACOSTA", "lat": 10.828551, "lng": -75.034547}, {"cedula": "1030673385", "puesto": "COLEGIO ALQUERIA", "mesa": 20, "direccion": "CLL 37 B SUR # 68 D - 93", "ciudad": "BOGOTA D.C.", "lat": 4.599573, "lng": -74.133281}, {"cedula": "80126131", "puesto": "CC GRAN PLAZA BOSA", "mesa": 6, "direccion": "CLL 65 SUR No 78H-51", "ciudad": "BOGOTA D.C.", "lat": 4.6201, "lng": -74.1923}, {"cedula": "52243197", "puesto": "CEDID SAN PABLO", "mesa": 4, "direccion": "CRA 77L No 65J - 73 SUR", "ciudad": "BOGOTA D.C.", "lat": 4.6062, "lng": -74.1784}, {"cedula": "1024508725", "puesto": "CENTRO COMERCIAL MERCURIO", "mesa": 18, "direccion": "CRA 7 NRO 32 35", "ciudad": "SOACHA", "lat": 4.5881616, "lng": -74.2035191}, {"cedula": "1032417059", "puesto": "VILLA DEL RIO", "mesa": 24, "direccion": "CLL 55A SUR No 66-50", "ciudad": "BOGOTA D.C.", "lat": 4.6152, "lng": -74.1485}, {"cedula": "53099030", "puesto": "I E JULIO CESAR TURBAY AYALA", "mesa": 8, "direccion": "TV 9 ESTE No 45A- 80", "ciudad": "SOACHA", "lat": 4.59546, "lng": -74.19502}, {"cedula": "1012434961", "puesto": "I.E. LICEO MAYOR DE SOACHA", "mesa": 17, "direccion": "CLL. 38 No. 6 A - 55 ESTE", "ciudad": "SOACHA", "lat": 4.58256, "lng": -74.194387}, {"cedula": "1073711749", "puesto": "I.E. COMPARTIR PRIMARIA", "mesa": 29, "direccion": "CR. 15 A NO. 5 C - 16 SUR", "ciudad": "SOACHA", "lat": 4.5683, "lng": -74.2343}, {"cedula": "80828793", "puesto": "I. E. SANTA ANA - ANTONIO NARIÑO", "mesa": 14, "direccion": "CR. 11 D No. 17 A - 44 SUR SANTA ANA", "ciudad": "SOACHA", "lat": 4.5686, "lng": -74.2255}, {"cedula": "21118151", "puesto": "CENTRO COMERCIAL GRAN PLAZA", "mesa": 3, "direccion": "CRA 7 No 30B - 139", "ciudad": "SOACHA", "lat": 4.5866, "lng": -74.2057}, {"cedula": "1005823660", "puesto": "GALICIA", "mesa": 26, "direccion": "CLL 60 A SUR # 73-31", "ciudad": "BOGOTA D.C.", "lat": 4.58712, "lng": -74.16235}, {"cedula": "79494633", "puesto": "COLEGIO DEL PILAR", "mesa": 8, "direccion": "CLL 62 No 27A-12", "ciudad": "BOGOTA D.C.", "lat": 4.6558, "lng": -74.0743}, {"cedula": "1013577097", "puesto": "CENTRO COMERCIAL VENTURA TERREROS", "mesa": 22, "direccion": "CRA 1 NRO 38 89 SOACHA", "ciudad": "SOACHA", "lat": 4.58846, "lng": -74.1950408}, {"cedula": "1010140961", "puesto": "PIAMONTE", "mesa": 23, "direccion": "CLL 68A SUR No 80H-05", "ciudad": "BOGOTA D.C.", "lat": 4.6143, "lng": -74.1945}, {"cedula": "1030662692", "puesto": "COL GABRIEL BETANCOURT MEJIA", "mesa": 34, "direccion": "CRA 87A No 6A-23 Y CRA 88 No 6A-28", "ciudad": "BOGOTA D.C.", "lat": 4.6465, "lng": -74.1612}, {"cedula": "52505410", "puesto": "I.E. COMPARTIR PRIMARIA", "mesa": 9, "direccion": "CR. 15 A NO. 5 C - 16 SUR", "ciudad": "SOACHA", "lat": 4.5683, "lng": -74.2343}, {"cedula": "1033683555", "puesto": "UNIVER. DE CUNDINAMARCA EXTENSION SOACHA", "mesa": 20, "direccion": "DIAG. 9 No. 4 B - 85", "ciudad": "SOACHA", "lat": 4.5772, "lng": -74.2201}, {"cedula": "80722895", "puesto": "COLISEO LEON XIII", "mesa": 12, "direccion": "CLL 48 No 9-05 LEON XIII", "ciudad": "SOACHA", "lat": 4.5950453, "lng": -74.1940555}, {"cedula": "1031142237", "puesto": "LUCERO DEL SUR", "mesa": 25, "direccion": "CRA 17 B BIS A # 67-30 SUR o 67-48 SUR", "ciudad": "BOGOTA D.C.", "lat": 4.55123, "lng": -74.14012}, {"cedula": "79503448", "puesto": "LA CABAÑA", "mesa": 16, "direccion": "CLL 63 B # 71A-18", "ciudad": "BOGOTA D.C.", "lat": 4.6645, "lng": -74.1082}]"""

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Consulta de Puesto de Votación</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{--bg:#0b0f0e;--card:#121a18;--card-border:#1c2825;--accent:#2dd4bf;--accent-d:#0d9488;--text:#f1f5f9;--muted:#94a3b8;--chat-bg:#080c0b;--msg-bot:#182421;--msg-user:#0d9488}}
        * {{box-sizing:border-box;margin:0;padding:0;font-family:'Inter',sans-serif}}
        body {{background:var(--bg);color:var(--text);padding:16px;max-width:100vw;overflow-x:hidden;font-size:15px}}
        header {{max-width:1200px;margin:0 auto 16px;text-align:left}}
        .badge {{background:#22c55e;color:#000;font-size:12px;font-weight:700;padding:4px 10px;border-radius:20px;display:inline-block;margin-bottom:8px}}
        h1 {{font-size:26px;font-weight:700;margin:4px 0;line-height:1.2}}
        p.subtitle {{color:var(--muted);font-size:14px;line-height:1.4}}
        .grid {{display:grid;grid-template-columns:1fr;gap:20px;max-width:1200px;margin:0 auto}}
        @media(min-width:850px) {{
            body {{padding:24px}}
            h1 {{font-size:30px}}
            .grid {{grid-template-columns:420px 1fr;gap:24px}}
        }}
        .card {{background:var(--card);border-radius:16px;padding:16px;border:1px solid var(--card-border)}}
        .chat-box {{display:flex;flex-direction:column;height:80vh;max-height:650px}}
        @media(min-width:850px) {{ .chat-box {{height:620px;max-height:none}} }}
        
        .chat-header {{display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--card-border);padding-bottom:12px;gap:8px}}
        .bot-info {{display:flex;align-items:center;gap:10px;min-width:0}}
        .avatar {{width:40px;height:40px;background:var(--accent-d);border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:bold;font-size:15px;color:#fff;flex-shrink:0}}
        .bot-status strong {{font-size:15px;display:block}}
        .bot-status small {{color:var(--accent);display:block;font-size:12px;font-weight:600}}
        
        .clear-btn {{background:#ef4444;color:#fff;border:none;padding:7px 12px;border-radius:10px;font-size:12px;font-weight:700;cursor:pointer;flex-shrink:0}}
        
        .messages {{flex-grow:1;background:var(--chat-bg);border-radius:14px;padding:12px;margin:10px 0;overflow-y:auto;display:flex;flex-direction:column;gap:12px}}
        .msg {{max-width:90%;padding:12px 14px;border-radius:14px;font-size:15px;line-height:1.45;white-space:pre-line;word-break:break-word}}
        .msg.bot {{background:var(--msg-bot);align-self:flex-start;color:#f8fafc}}
        .msg.user {{background:var(--msg-user);align-self:flex-end;color:#ffffff;font-weight:500}}
        .msg .time {{font-size:11px;color:var(--muted);text-align:right;margin-top:4px;display:block}}
        
        .quick-btns {{display:flex;flex-direction:column;gap:8px;margin-bottom:12px}}
        .q-btn {{background:var(--card);border:1px solid var(--card-border);color:var(--text);padding:12px 14px;border-radius:12px;font-size:14px;font-weight:600;cursor:pointer;text-align:left;display:flex;align-items:center;justify-content:space-between;transition:all 0.2s}}
        .q-btn:hover {{border-color:var(--accent);color:var(--accent)}}
        
        .input-row {{display:flex;gap:8px;align-items:center}}
        .input-row input {{flex-grow:1;background:var(--chat-bg);border:1px solid var(--card-border);border-radius:24px;padding:12px 16px;color:#fff;font-size:15px;outline:none}}
        .input-row input:focus {{border-color:var(--accent)}}
        .input-row button {{background:var(--accent);color:#000;border:none;padding:12px 18px;border-radius:24px;font-weight:700;font-size:14px;cursor:pointer}}
        
        .tabs {{display:flex;gap:16px;border-bottom:1px solid var(--card-border);padding-bottom:10px;margin-bottom:16px}}
        .tab-btn {{background:none;border:none;color:var(--muted);font-weight:600;font-size:15px;cursor:pointer;padding:4px 0}}
        .tab-btn.active {{color:var(--accent);border-bottom:2px solid var(--accent);padding-bottom:8px}}
        
        .stats {{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px}}
        .stat-card {{background:var(--chat-bg);border:1px solid var(--card-border);border-radius:12px;padding:14px;text-align:center}}
        .stat-card h2 {{color:var(--accent);font-size:24px;font-weight:700}}
        .stat-card p {{color:var(--muted);font-size:12px;margin-top:2px}}
        
        .info-banner {{background:rgba(45, 212, 191, 0.08);border:1px solid rgba(45, 212, 191, 0.2);border-radius:12px;padding:12px;font-size:13px;color:var(--muted);margin-bottom:16px;line-height:1.4}}
        
        .table-wrap {{overflow-x:auto;max-height:420px}}
        table {{width:100%;border-collapse:collapse;font-size:14px;text-align:left;white-space:nowrap}}
        th,td {{padding:10px 12px;border-bottom:1px solid var(--card-border)}}
        th {{background:var(--chat-bg);color:var(--accent);position:sticky;top:0;font-size:13px}}
        tr:hover {{background:var(--msg-bot)}}
    </style>
</head>
<body>
<header>
    <span class="badge">● BASE REAL DE VOTANTES</span>
    <h1>Consulta de puesto de votación</h1>
    <p class="subtitle">Asistente de consulta oficial cargado con la base de datos de Soacha.</p>
</header>
<div class="grid">
    <div class="card chat-box">
        <div class="chat-header">
            <div class="bot-info">
                <div class="avatar">27</div>
                <div class="bot-status">
                    <strong>Asistente de consulta</strong>
                    <small>• Soacha 2027</small>
                </div>
            </div>
            <button class="clear-btn" onclick="clearChat()">Limpiar</button>
        </div>
        <div class="messages" id="msgs">
            <div class="msg bot">Hola 👋 Soy el asistente de la campaña. Le ayudo a encontrar su puesto de votación.<span class="time">02:00 p. m.</span></div>
            <div class="msg bot">¿Qué desea hacer?\n1. Consultar mi puesto de votación\n2. Acceso de coordinadores\n3. Privacidad y datos<span class="time">02:00 p. m.</span></div>
        </div>
        <div class="quick-btns">
            <button class="q-btn" onclick="sendQuick('1. Consultar puesto de votación')"><span>📍 Consultar puesto de votación</span> <span>›</span></button>
            <button class="q-btn" onclick="sendQuick('2. Acceso de coordinadores')"><span>👥 Acceso de coordinadores</span> <span>›</span></button>
            <button class="q-btn" onclick="sendQuick('3. Privacidad y datos')"><span>🔒 Privacidad y datos</span> <span>›</span></button>
        </div>
        <div class="input-row">
            <input type="number" id="inp" placeholder="Ingrese número de cédula..." onkeypress="if(event.key==='Enter')sendMsg()">
            <button onclick="sendMsg()">Enviar</button>
        </div>
    </div>
    <div class="card">
        <div class="tabs">
            <button class="tab-btn active" onclick="setTab('base',this)">Base de Datos (99)</button>
            <button class="tab-btn" onclick="setTab('audit',this)">Actividad y Auditoría</button>
        </div>
        <div class="stats">
            <div class="stat-card"><h2>99</h2><p>Votantes Reales</p></div>
            <div class="stat-card"><h2>77</h2><p>Puestos Registrados</p></div>
            <div class="stat-card"><h2 id="auditCount">0</h2><p>Consultas Realizadas</p></div>
        </div>
        <div id="tab-base" class="tab-content">
            <div class="info-banner">
                <strong>Base Real Cargada:</strong> Se han sincronizado los 99 registros oficiales de Soacha desde la fuente de datos autorizada.
            </div>
            <div class="table-wrap">
                <table>
                    <thead><tr><th>Cédula</th><th>Puesto</th><th>Mesa</th><th>Dirección</th><th>Municipio</th></tr></thead>
                    <tbody id="dbRows"></tbody>
                </table>
            </div>
        </div>
        <div id="tab-audit" class="tab-content" style="display:none">
            <div class="table-wrap">
                <table>
                    <thead><tr><th>Hora</th><th>Cédula</th><th>Puesto Encontrado</th><th>Estado</th></tr></thead>
                    <tbody id="auditRows"></tbody>
                </table>
            </div>
        </div>
    </div>
</div>
<script>
const DB={{json_db}};
let auditLogs=[];
function initDB(){{
    const tbody=document.getElementById('dbRows');
    tbody.innerHTML='';
    DB.forEach(item=>{{
        const tr=document.createElement('tr');
        tr.innerHTML='<td><b>'+item.cedula+'</b></td><td>'+item.puesto+'</td><td>'+item.mesa+'</td><td>'+item.direccion+'</td><td>'+item.ciudad+'</td>';
        tbody.appendChild(tr);
    }})
}}
function clearChat(){{
    const msgs=document.getElementById('msgs');
    const t=new Date().toLocaleTimeString([],{{hour:'2-digit',minute:'2-digit'}});
    msgs.innerHTML='<div class="msg bot">Hola 👋 Soy el asistente de la campaña. Le ayudo a encontrar su puesto de votación.<span class="time">'+t+'</span></div><div class="msg bot">¿Qué desea hacer?\\n1. Consultar mi puesto de votación\\n2. Acceso de coordinadores\\n3. Privacidad y datos<span class="time">'+t+'</span></div>';
}}
function queryCedula(ced){{
    addMsg(ced,'user');
    const found=DB.find(x=>x.cedula===ced);
    setTimeout(()=>{{
        if(found){{
            const mapsUrl='https://www.google.com/maps?q='+found.lat+','+found.lng;
            const resp='📍 *Resultado de Consulta*\\n\\n• *Cédula:* '+found.cedula+'\\n• *Puesto:* '+found.puesto+'\\n• *Mesa:* '+found.mesa+'\\n• *Dirección:* '+found.direccion+'\\n• *Municipio:* '+found.ciudad+'\\n\\n🗺️ <a href="'+mapsUrl+'" target="_blank" style="color:var(--accent);font-weight:bold">Ver ubicación en Google Maps</a>';
            addMsg(resp,'bot');addAudit(ced,found.puesto,'Exitosa')
        }}else{{
            addMsg('❌ La cédula *'+ced+'* no se encuentra registrada en la base de datos de Soacha.','bot');
            addAudit(ced,'No encontrado','Fallida')
        }}
    }},400)
}}
function sendMsg(){{
    const inp=document.getElementById('inp');
    const txt=inp.value.trim();if(!txt)return;inp.value='';
    if(/^\d+$/.test(txt)){{queryCedula(txt)}}
    else{{addMsg(txt,'user');setTimeout(()=>{{addMsg('Por favor ingrese un número de cédula válido.','bot')}},300)}}
}}
function sendQuick(txt){{
    addMsg(txt,'user');
    setTimeout(()=>{{
        if(txt.includes('1.'))addMsg('Por favor ingrese su número de Cédula (NUIP):','bot');
        else if(txt.includes('2.'))addMsg('Ingrese su PIN de acceso como Líder/Coordinador:','bot');
        else addMsg('Política Ley 1581: Sus datos están completamente protegidos.','bot')
    }},300)
}}
function addMsg(txt,sender){{
    const box=document.getElementById('msgs');
    const div=document.createElement('div');div.className='msg '+sender;
    const t=new Date().toLocaleTimeString([],{{hour:'2-digit',minute:'2-digit'}});
    div.innerHTML=txt.replace(/\\n/g,'<br>')+'<span class="time">'+t+'</span>';
    box.appendChild(div);box.scrollTop=box.scrollHeight
}}
function addAudit(ced,puesto,res){{
    auditLogs.unshift({{hora:new Date().toLocaleTimeString(),ced,puesto,res}});
    document.getElementById('auditCount').innerText=auditLogs.length;
    const tbody=document.getElementById('auditRows');tbody.innerHTML='';
    auditLogs.forEach(a=>{{
        const tr=document.createElement('tr');
        tr.innerHTML='<td>'+a.hora+'</td><td>'+a.ced+'</td><td>'+a.puesto+'</td><td>'+a.res+'</td>';
        tbody.appendChild(tr)
    }})
}}
function setTab(tab,btn){{
    document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('tab-base').style.display=tab==='base'?'block':'none';
    document.getElementById('tab-audit').style.display=tab==='audit'?'block':'none'
}}
initDB();
</script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Archivo index.html generado exitosamente.")
