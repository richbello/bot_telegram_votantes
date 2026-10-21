import pandas as pd
import json

xls = pd.ExcelFile('puestos_votacion_prueba.xlsx')
df = pd.read_excel(xls, 'Votantes')

db = [{
    'cedula': str(r['NUIP']).strip(),
    'puesto': str(r['Puesto']).strip(),
    'mesa': int(r['Mesa']),
    'direccion': str(r['Dirección']).strip(),
    'ciudad': str(r['Municipio']).strip(),
    'lat': float(r['Latitud']),
    'lng': float(r['Longitud'])
} for _, r in df.iterrows()]

json_db = json.dumps(db, ensure_ascii=False)
total_db = len(db)
total_puestos = len(set(x['puesto'] for x in db))

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bot Consulta Puesto de Votacion</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{--bg:#0f1715;--card:#16221f;--accent:#2dd4bf;--accent-d:#0d9488;--text:#e2e8f0;--muted:#94a3b8;--border:#243531;--chat:#0b1110;--msg:#1c2a27}}
        * {{box-sizing:border-box;margin:0;padding:0;font-family:'Inter',sans-serif}}
        body {{background:var(--bg);color:var(--text);padding:20px}}
        header {{max-width:1200px;margin:0 auto 20px}}
        .badge {{background:#d97706;color:#fff;font-size:11px;font-weight:700;padding:3px 8px;border-radius:4px}}
        h1 {{font-size:26px;font-weight:700;margin:8px 0}}
        p.subtitle {{color:var(--muted);font-size:14px}}
        .grid {{display:grid;grid-template-columns:360px 1fr;gap:20px;max-width:1200px;margin:0 auto}}
        .card {{background:var(--card);border-radius:16px;padding:20px;border:1px solid var(--border)}}
        .chat-box {{display:flex;flex-direction:column;height:580px}}
        .chat-header {{display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border);padding-bottom:12px}}
        .avatar {{width:36px;height:36px;background:var(--accent-d);border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:bold}}
        .bot-status small {{color:var(--accent);display:block;font-size:11px}}
        .messages {{flex-grow:1;background:var(--chat);border-radius:12px;padding:12px;margin:12px 0;overflow-y:auto;display:flex;flex-direction:column;gap:8px}}
        .msg {{max-width:85%;padding:8px 12px;border-radius:10px;font-size:13px;line-height:1.4;white-space:pre-line}}
        .msg.bot {{background:var(--msg);align-self:flex-start}}
        .msg.user {{background:var(--accent-d);align-self:flex-end;color:#fff}}
        .msg .time {{font-size:10px;color:var(--muted);text-align:right;margin-top:3px;display:block}}
        .quick-btns {{display:flex;gap:6px;margin-bottom:10px;flex-wrap:wrap}}
        .q-btn {{background:var(--msg);border:1px solid var(--accent);color:var(--accent);padding:5px 10px;border-radius:12px;font-size:12px;cursor:pointer}}
        .input-row {{display:flex;gap:8px}}
        .input-row input {{flex-grow:1;background:var(--chat);border:1px solid var(--border);border-radius:18px;padding:8px 14px;color:#fff;font-size:13px;outline:none}}
        .input-row button {{background:var(--accent);color:#000;border:none;padding:8px 16px;border-radius:18px;font-weight:600;cursor:pointer}}
        .tabs {{display:flex;gap:15px;border-bottom:1px solid var(--border);padding-bottom:10px;margin-bottom:15px}}
        .tab-btn {{background:none;border:none;color:var(--muted);font-weight:600;font-size:14px;cursor:pointer}}
        .tab-btn.active {{color:var(--accent);border-bottom:2px solid var(--accent);padding-bottom:8px}}
        .stats {{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:15px}}
        .stat-card {{background:var(--chat);border:1px solid var(--border);border-radius:10px;padding:12px;text-align:center}}
        .stat-card h2 {{color:var(--accent);font-size:22px}}
        .stat-card p {{color:var(--muted);font-size:11px;margin-top:2px}}
        .table-wrap {{overflow-x:auto;max-height:400px}}
        table {{width:100%;border-collapse:collapse;font-size:12px;text-align:left}}
        th,td {{padding:8px 10px;border-bottom:1px solid var(--border)}}
        th {{background:var(--chat);color:var(--accent);position:sticky;top:0}}
        tr:hover {{background:var(--msg)}}
        .chip {{background:var(--msg);border:1px solid var(--accent);color:var(--accent);padding:2px 6px;border-radius:4px;cursor:pointer;display:inline-block;margin:2px}}
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
            <div style="display:flex;align-items:center">
                <div class="avatar">27</div>
                <div class="bot-status" style="margin-left:10px">
                    <strong>Campaña Soacha 2027</strong>
                    <small>bot • en línea</small>
                </div>
            </div>
            <span style="font-size:11px;background:#134e4a;color:var(--accent);padding:2px 8px;border-radius:10px">Ciudadano</span>
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
            <input type="text" id="inp" placeholder="Escriba cédula..." onkeypress="if(event.key==='Enter')sendMsg()">
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
            <div class="stat-card"><h2>{total_db}</h2><p>Simpatizantes Reales</p></div>
            <div class="stat-card"><h2>{total_puestos}</h2><p>Puestos de Votación</p></div>
            <div class="stat-card"><h2 id="auditCount">0</h2><p>Consultas Registradas</p></div>
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
            <p style="font-size:12px;color:var(--muted);margin-bottom:10px">Toque cualquier cédula para consultar en el chat:</p>
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
function queryCedula(ced){{
    addMsg(ced,'user');
    const found=DB.find(x=>x.cedula===ced);
    setTimeout(()=>{{
        if(found){{
            const mapsUrl='https://www.google.com/maps?q='+found.lat+','+found.lng;
            const resp='📍 *Puesto Encontrado*\\n• Cédula: '+found.cedula+'\\n• Puesto: '+found.puesto+'\\n• Mesa: '+found.mesa+'\\n• Dirección: '+found.direccion+'\\n• Municipio: '+found.ciudad+'\\n\\n🗺️ <a href="'+mapsUrl+'" target="_blank" style="color:var(--accent)">Ver en Google Maps</a>';
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

print("✅ 'index.html' generado exitosamente con los 80 registros.")
