import os
import pandas as pd
import json
import glob

excel_file = 'puestos_votacion_prueba_3.xlsx'
if not os.path.exists(excel_file):
    excel_files = glob.glob('*.xlsx')
    excel_file = excel_files[0] if excel_files else 'puestos_votacion_prueba.xlsx'

print(f"Leyendo datos desde: {excel_file}")

xls = pd.ExcelFile(excel_file)
sheet_name = 'Votantes' if 'Votantes' in xls.sheet_names else xls.sheet_names[0]
df = pd.read_excel(xls, sheet_name)

db = []
for _, r in df.iterrows():
    try:
        db.append({
            'cedula': str(r['NUIP']).strip(),
            'puesto': str(r['Puesto']).strip(),
            'mesa': int(r['Mesa']) if pd.notnull(r['Mesa']) else 0,
            'direccion': str(r['Dirección']).strip() if pd.notnull(r['Dirección']) else '',
            'ciudad': str(r['Municipio']).strip() if pd.notnull(r['Municipio']) else '',
            'lat': float(r['Latitud']) if pd.notnull(r['Latitud']) else 0.0,
            'lng': float(r['Longitud']) if pd.notnull(r['Longitud']) else 0.0
        })
    except Exception as e:
        pass

json_db = json.dumps(db, ensure_ascii=False)
total_db = len(db)
total_puestos = len(set(x['puesto'] for x in db))

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Bot Consulta Puesto de Votacion</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{--bg:#0f1715;--card:#16221f;--accent:#2dd4bf;--accent-d:#0d9488;--text:#f1f5f9;--muted:#cbd5e1;--border:#243531;--chat:#0b1110;--msg:#1c2a27}}
        * {{box-sizing:border-box;margin:0;padding:0;font-family:'Inter',sans-serif}}
        body {{background:var(--bg);color:var(--text);padding:10px;max-width:100vw;overflow-x:hidden;font-size:16px}}
        header {{max-width:1200px;margin:0 auto 12px;text-align:left}}
        .badge {{background:#d97706;color:#fff;font-size:13px;font-weight:700;padding:6px 12px;border-radius:6px;display:inline-block;margin-bottom:6px}}
        h1 {{font-size:22px;font-weight:700;margin:4px 0;line-height:1.2}}
        p.subtitle {{color:var(--muted);font-size:14px;line-height:1.3}}
        .grid {{display:grid;grid-template-columns:1fr;gap:16px;max-width:1200px;margin:0 auto}}
        @media(min-width: 850px) {{
            body {{padding:20px}}
            h1 {{font-size:28px}}
            p.subtitle {{font-size:15px}}
            .grid {{grid-template-columns:420px 1fr;gap:24px}}
        }}
        .card {{background:var(--card);border-radius:16px;padding:14px;border:1px solid var(--border)}}
        .chat-box {{display:flex;flex-direction:column;height:82vh;max-height:680px}}
        @media(min-width: 850px) {{ .chat-box {{height:640px;max-height:none}} }}
        
        .chat-header {{display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border);padding-bottom:12px;gap:8px}}
        .bot-info {{display:flex;align-items:center;gap:10px;min-width:0}}
        .avatar {{width:42px;height:42px;background:var(--accent-d);border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:bold;font-size:16px;flex-shrink:0}}
        .bot-status {{min-width:0}}
        .bot-status strong {{font-size:16px;display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
        .bot-status small {{color:var(--accent);display:block;font-size:13px;font-weight:600}}
        
        .clear-btn {{background:#ef4444;color:#fff;border:none;padding:8px 12px;border-radius:10px;font-size:13px;font-weight:700;cursor:pointer;flex-shrink:0;display:flex;align-items:center;gap:4px}}
        .clear-btn:active {{opacity:0.8}}
        
        .messages {{flex-grow:1;background:var(--chat);border-radius:14px;padding:12px;margin:10px 0;overflow-y:auto;display:flex;flex-direction:column;gap:12px}}
        .msg {{max-width:92%;padding:12px 14px;border-radius:14px;font-size:16px;line-height:1.45;white-space:pre-line;word-break:break-word;font-weight:400}}
        .msg.bot {{background:var(--msg);align-self:flex-start;color:#f8fafc}}
        .msg.user {{background:var(--accent-d);align-self:flex-end;color:#ffffff;font-weight:500}}
        .msg .time {{font-size:12px;color:var(--muted);text-align:right;margin-top:6px;display:block}}
        
        .quick-btns {{display:flex;gap:8px;margin-bottom:10px;overflow-x:auto;padding-bottom:6px;-webkit-overflow-scrolling:touch}}
        .q-btn {{background:var(--msg);border:1.5px solid var(--accent);color:var(--accent);padding:10px 14px;border-radius:16px;font-size:14px;font-weight:700;cursor:pointer;white-space:nowrap;flex-shrink:0}}
        
        .input-row {{display:flex;gap:8px;align-items:center}}
        .input-row input {{flex-grow:1;background:var(--chat);border:1.5px solid var(--border);border-radius:24px;padding:12px 16px;color:#fff;font-size:16px;outline:none;min-width:0}}
        .input-row input:focus {{border-color:var(--accent)}}
        .input-row button {{background:var(--accent);color:#000;border:none;padding:12px 18px;border-radius:24px;font-weight:700;font-size:15px;cursor:pointer;flex-shrink:0}}
        
        .tabs {{display:flex;gap:12px;border-bottom:1px solid var(--border);padding-bottom:10px;margin-bottom:12px;overflow-x:auto;-webkit-overflow-scrolling:touch}}
        .tab-btn {{background:none;border:none;color:var(--muted);font-weight:600;font-size:15px;cursor:pointer;white-space:nowrap;padding:4px 0}}
        .tab-btn.active {{color:var(--accent);border-bottom:3px solid var(--accent);padding-bottom:6px}}
        
        .stats {{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:12px}}
        .stat-card {{background:var(--chat);border:1px solid var(--border);border-radius:10px;padding:10px;text-align:center}}
        .stat-card h2 {{color:var(--accent);font-size:22px}}
        .stat-card p {{color:var(--muted);font-size:12px;margin-top:2px}}
        
        .table-wrap {{overflow-x:auto;max-height:360px;-webkit-overflow-scrolling:touch}}
        table {{width:100%;border-collapse:collapse;font-size:15px;text-align:left;white-space:nowrap}}
        th,td {{padding:12px;border-bottom:1px solid var(--border)}}
        th {{background:var(--chat);color:var(--accent);position:sticky;top:0;font-size:14px}}
        tr:hover {{background:var(--msg)}}
        
        .chip {{background:var(--msg);border:1.5px solid var(--accent);color:var(--accent);padding:8px 14px;border-radius:10px;cursor:pointer;display:inline-block;margin:4px;font-size:15px;font-weight:600}}
    </style>
</head>
<body>
<header>
    <span class="badge">BASE REAL • SOACHA DE {total_db} VOTANTES</span>
    <h1>Bot de consulta de puesto de votación</h1>
    <p class="subtitle">Simulación de la base de datos real con {total_db} simpatizantes en Soacha.</p>
</header>
<div class="grid">
    <div class="card chat-box">
        <div class="chat-header">
            <div class="bot-info">
                <div class="avatar">27</div>
                <div class="bot-status">
                    <strong>Soacha 2027</strong>
                    <small>• en línea</small>
                </div>
            </div>
            <button class="clear-btn" onclick="clearChat()">🗑️ Limpiar</button>
        </div>
        <div class="messages" id="msgs">
            <div class="msg bot">Hola 👋 Soy el asistente de la campaña. Le ayudo a encontrar su puesto de votación.<span class="time">02:00 p. m.</span></div>
            <div class="msg bot">¿Qué desea hacer?<br>1. Consultar mi puesto de votación<br>2. Soy líder o coordinador<br>3. Política de datos<span class="time">02:00 p. m.</span></div>
        </div>
        <div class="quick-btns">
            <button class="q-btn" onclick="sendQuick('1. Mi puesto')">1. Mi puesto</button>
            <button class="q-btn" onclick="sendQuick('2. Soy líder')">2. Soy líder</button>
            <button class="q-btn" onclick="sendQuick('3. Política de datos')">3. Política de datos</button>
        </div>
        <div class="input-row">
            <input type="number" id="inp" placeholder="Escriba cédula..." onkeypress="if(event.key==='Enter')sendMsg()">
            <button onclick="sendMsg()">Enviar</button>
        </div>
    </div>
    <div class="card">
        <div class="tabs">
            <button class="tab-btn active" onclick="setTab('base',this)">Base de datos ({total_db})</button>
            <button class="tab-btn" onclick="setTab('probar',this)">Cédulas de prueba</button>
            <button class="tab-btn" onclick="setTab('audit',this)">Auditoría</button>
        </div>
        <div class="stats">
            <div class="stat-card"><h2>{total_db}</h2><p>Simpatizantes</p></div>
            <div class="stat-card"><h2>{total_puestos}</h2><p>Puestos</p></div>
            <div class="stat-card"><h2 id="auditCount">0</h2><p>Consultas</p></div>
        </div>
        <div id="tab-base" class="tab-content">
            <div class="table-wrap">
                <table>
                    <thead><tr><th>Cédula</th><th>Puesto</th><th>Mesa</th><th>Dirección</th><th>Municipio</th></tr></thead>
                    <tbody id="dbRows"></tbody>
                </table>
            </div>
        </div>
        <div id="tab-probar" class="tab-content" style="display:none">
            <p style="font-size:14px;color:var(--muted);margin-bottom:12px">Toque cualquier cédula para consultar en el chat:</p>
            <div id="chipsWrap"></div>
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
const DB={json_db};
let auditLogs=[];
function initDB(){{
    const tbody=document.getElementById('dbRows');
    const chips=document.getElementById('chipsWrap');
    tbody.innerHTML='';chips.innerHTML='';
    DB.forEach(item=>{{
        const tr=document.createElement('tr');
        tr.innerHTML='<td><b>'+item.cedula+'</b></td><td>'+item.puesto+'</td><td>'+item.mesa+'</td><td>'+item.direccion+'</td><td>'+item.ciudad+'</td>';
        tbody.appendChild(tr);
        const chip=document.createElement('span');
        chip.className='chip';chip.innerText=item.cedula;
        chip.onclick=()=>{{queryCedula(item.cedula)}};
        chips.appendChild(chip)
    }})
}}
function clearChat(){{
    const msgs=document.getElementById('msgs');
    const t=new Date().toLocaleTimeString([],{{hour:'2-digit',minute:'2-digit'}});
    msgs.innerHTML='<div class="msg bot">Hola 👋 Soy el asistente de la campaña. Le ayudo a encontrar su puesto de votación.<span class="time">'+t+'</span></div><div class="msg bot">¿Qué desea hacer?<br>1. Consultar mi puesto de votación<br>2. Soy líder o coordinador<br>3. Política de datos<span class="time">'+t+'</span></div>';
}}
function queryCedula(ced){{
    addMsg(ced,'user');
    const found=DB.find(x=>x.cedula===ced);
    setTimeout(()=>{{
        if(found){{
            const mapsUrl='https://www.google.com/maps?q='+found.lat+','+found.lng;
            const resp='📍 *Puesto Encontrado*\\n• Cédula: '+found.cedula+'\\n• Puesto: '+found.puesto+'\\n• Mesa: '+found.mesa+'\\n• Dirección: '+found.direccion+'\\n• Municipio: '+found.ciudad+'\\n\\n🗺️ <a href="'+mapsUrl+'" target="_blank" style="color:var(--accent);font-weight:bold">Ver en Google Maps</a>';
            addMsg(resp,'bot');addAudit(ced,found.puesto,'Exitosa')
        }}else{{
            addMsg('❌ La cédula *'+ced+'* no se encuentra registrada en la base de datos.','bot');
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
        if(txt.includes('1.'))addMsg('Por favor escriba su número de Cédula (NUIP):','bot');
        else if(txt.includes('2.'))addMsg('Ingrese su PIN de acceso como Líder/Coordinador:','bot');
        else addMsg('Política Ley 1581: Sus datos están protegidos.','bot')
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
    document.getElementById('tab-probar').style.display=tab==='probar'?'block':'none';
    document.getElementById('tab-audit').style.display=tab==='audit'?'block':'none'
}}
initDB();
</script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ 'index.html' optimizado para móvil.")
