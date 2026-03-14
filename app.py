import streamlit as st
import requests

# Configurazione Pagina
st.set_page_config(page_title="Casa Smart", page_icon="🏠")

# Funzione per attivare Voice Monkey
def trigger_monkey(monkey_name):
    # Recuperiamo le chiavi segrete dai Secrets di Streamlit
    access_key = st.secrets["VM_ACCESS_KEY"]
    secret_key = st.secrets["VM_SECRET_KEY"]
    
    url = "https://api.voicemonkey.io/trigger"
    params = {
        "accessKey": access_key,
        "secretKey": secret_key,
        "monkey": monkey_name
    }
    
    try:
        r = requests.get(url, params=params)
        if r.status_code == 200:
            st.toast(f"✅ Comando '{monkey_name}' inviato!")
        else:
            st.error(f"❌ Errore API: {r.status_code}")
    except Exception as e:
        st.error(f"⚠️ Errore connessione: {e}")

# --- INTERFACCIA ---
st.title("🕹️ Il mio Pannello di Controllo")

# Chiedi il PIN (sarà nei Secrets)
pin = st.sidebar.text_input("Inserisci PIN", type="password")

if pin == st.secrets["MY_PIN"]:
    st.sidebar.success("Accesso Autorizzato")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🛋️ Soggiorno")
        if st.button("Accendi Luce", use_container_width=True):
            trigger_monkey("luce_salotto") # <--- Inserisci qui il nome esatto della Monkey
            
    with col2:
        st.subheader("🌙 Notte")
        if st.button("Spegni Tutto", use_container_width=True):
            trigger_monkey("spegni_casa")
            
else:
    st.info("Digita il PIN a sinistra per attivare i comandi.")
