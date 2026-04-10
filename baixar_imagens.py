"""
Script para baixar imagens do Google Drive usando sessão do Chrome.
Execute: python baixar_imagens.py
"""
import os, sys, subprocess

# Instalar dependências se necessário
def pip_install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])

try:
    import requests
except ImportError:
    pip_install("requests")
    import requests

try:
    import browser_cookie3
except ImportError:
    pip_install("browser-cookie3")
    import browser_cookie3

ASSETS = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(ASSETS, exist_ok=True)

# Todos os arquivos: {nome_local: file_id}
FILES = {
    # Logos
    "logo-preta.png":   "1RUOJ3f0j0BQq7zYe-VJBU-FREUncaeHU",
    "logo-dourada.png": "1r2W-z6p0mH954CgbVJVZZlcmy46FBEY4",
    "logo-bg-preta.jpg":"1-O_ssiatOdT9Q_YSGBoLe_pLlYiR-E_Q",
    # Produtos (21 fotos)
    "foto-01.png": "1BK0DDs9SVfI3kePqYz3NvwZqnodhE3jv",
    "foto-02.png": "1i_6eJbFtxPEzudIzHJYRetQLgf--nuoS",
    "foto-03.png": "1VYDw3PS4jD1brEc1TdLDsINt3vkuazL1",
    "foto-04.png": "1OB6rcT0mPhw0qpYAj6OTGIxtcfikFv0l",
    "foto-05.png": "1DwVIn5nReD5mUcT2xt2HftgddBWq25fc",
    "foto-06.png": "1VzDrHwTTUdpWsgYTeudcKd8Xes-SuLNL",
    "foto-07.png": "188nPCypncPtDgMfsScAzzUyVcbJfUqe1",
    "foto-08.png": "1Tp-MjdruaG87TS7JQfoAIbF7sK-DWMc9",
    "foto-09.png": "1FnBLxnhibIDZbUNVbNBzNzxeDY1gurnt",
    "foto-10.png": "14l3gMMljl6uTRrwyUVf8oYOp-w1Cd14h",
    "foto-11.png": "12DrAZ_wbtOghLg9kl6v26-AXxePAiDXF",
    "foto-12.png": "1IhVLiTK4csV3RD4Dr39XiuTfdkD89VJX",
    "foto-13.png": "1wbu-OL7qXkAEi9boQ6ugAD0zW1CvFpd9",
    "foto-14.png": "1IxCEH0hcQ7XfXprhQSC9c0PJaQpjpq54",
    "foto-15.png": "1b9pPwn9nMmQqKPrDQis2fK6r3Si-VMxZ",
    "foto-16.png": "1lD3bt3InZ0NuN0Xf0VsjYHvWY1BXIKMU",
    "foto-17.png": "11QV-2qp5T0H9cYi8oNyTfgNeRk5oiItY",
    "foto-18.png": "1UpJS1DeX00asgJQTpA_fBWjWTxk7n-H3",
    "foto-19.png": "1je7TJQtO7XT2vMcUsCSyS6ona4dBqQwQ",
    "foto-20.png": "1tv-f3XGSqdgdBYkqxea1xgYIvVqp2RbY",
    "foto-21.png": "1_TO5XYRKNw-2N-8xzHqkG05X88EY9G5y",
}

print("Carregando cookies do Chrome...")
try:
    cookies = browser_cookie3.chrome(domain_name=".google.com")
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie.name, cookie.value, domain=cookie.domain)
    print("✅ Cookies carregados!")
except Exception as e:
    print(f"⚠️  Não foi possível carregar cookies: {e}")
    print("Tentando sem autenticação...")
    session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})

ok = 0
fail = 0
for nome, fid in FILES.items():
    dest = os.path.join(ASSETS, nome)
    if os.path.exists(dest):
        print(f"  ⏭  {nome} já existe, pulando")
        ok += 1
        continue

    url = f"https://drive.google.com/uc?export=download&id={fid}&confirm=t"
    try:
        r = session.get(url, timeout=30, allow_redirects=True)
        if r.status_code == 200 and len(r.content) > 1000:
            with open(dest, "wb") as f:
                f.write(r.content)
            print(f"  ✅ {nome} ({len(r.content)//1024} KB)")
            ok += 1
        else:
            print(f"  ❌ {nome} — status {r.status_code}, tamanho {len(r.content)} bytes")
            fail += 1
    except Exception as e:
        print(f"  ❌ {nome} — erro: {e}")
        fail += 1

print(f"\n📦 Concluído: {ok} baixados, {fail} falhas")
if fail == 0:
    print("✨ Todas as imagens estão em assets/")
    print("   Atualize os src do index.html para usar assets/ ao invés do Drive.")
