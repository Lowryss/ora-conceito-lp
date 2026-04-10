"""
Baixa imagens novas da pasta Sem fundo e Marca
"""
import os, sys, subprocess

def pip_install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])

try:
    import requests
except ImportError:
    pip_install("requests"); import requests

try:
    import browser_cookie3
except ImportError:
    pip_install("browser-cookie3"); import browser_cookie3

ASSETS = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(ASSETS, exist_ok=True)

# Novas imagens sem fundo + marca
FILES = {
    # Sem fundo - produtos com recorte limpo
    "sf-buffet.png":      "1_X0_9GCVnTuHvGSDHjHiAEX_RiPSvk6j",
    "sf-prod-02.png":     "193Yzxu6CB2H-3rnwbLxzHeroa1LoCXfV",
    "sf-prod-03.png":     "1ZZKclwGWqwlNGD3F1ADnqjNZhftRWY6L",
    "sf-prod-04.png":     "1mmMHN_3NA1_mHEyY7_v1PdDBWRpbBd70",
    "sf-prod-05.png":     "1zCCBOSbFKXlC_BplHTWNaqox57lQ3Vzn",
    "sf-cadeira-f.png":   "1r2FvdmDJelXkswTzEY5oo6EIwmvFuHKE",
    "sf-cadeira-t.png":   "1SDVwhqb2d8uhjashISUHMF_TEFUk_Poa",
    "sf-prod-08.png":     "16KbKtx-aR7NfQllNe14e6cUyKVzFQWAM",
    "sf-estante.png":     "1ys8zLOE1B3tiPnq-5ZdeFCG0NF6JZ4wb",
    # Marca
    "marca-room.PNG":     "1e-ZGuoCWwAjrCpqG4VoQ1F_3b4RhOje0",
}

print("Carregando cookies do Chrome...")
try:
    cookies = browser_cookie3.chrome(domain_name=".google.com")
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie.name, cookie.value, domain=cookie.domain)
    print("Cookies carregados!")
except Exception as e:
    print(f"Sem cookies: {e}")
    session = requests.Session()

session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})

ok = fail = 0
for nome, fid in FILES.items():
    dest = os.path.join(ASSETS, nome)
    if os.path.exists(dest):
        print(f"  JA EXISTE: {nome}")
        ok += 1
        continue
    url = f"https://drive.google.com/uc?export=download&id={fid}&confirm=t"
    try:
        r = session.get(url, timeout=30, allow_redirects=True)
        if r.status_code == 200 and len(r.content) > 1000:
            with open(dest, "wb") as f:
                f.write(r.content)
            print(f"  OK: {nome} ({len(r.content)//1024} KB)")
            ok += 1
        else:
            print(f"  FALHA: {nome} - status {r.status_code}, {len(r.content)} bytes")
            fail += 1
    except Exception as e:
        print(f"  ERRO: {nome} - {e}")
        fail += 1

print(f"\nConcluido: {ok} ok, {fail} falhas")
