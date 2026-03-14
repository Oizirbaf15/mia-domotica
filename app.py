import streamlit as st
import requests

st.set_page_config(page_title="Casa Smart", page_icon="🏠")

def trigger_monkey(monkey_name):
    # Usiamo il nuovo sistema a Token (V2)
    token = st.secrets["VM_TOKEN"]
    
    # URL aggiornato per la V2
    url = f"https://api.voicemonkey.io/trigger?token={token}&monkey={monkey_name}"
    
    try:
        r = requests.get(url)
        if r.status_code == 200:
            st.toast(f"✅ Comando '{monkey_name}' inviato!")
        else:
            st.error(f"❌ Errore API: {r.status_code}")
    except Exception as e:
        st.error(f"⚠️ Errore: {e}")

st.title("🕹️ Dashboard Domotica")
pin = st.sidebar.text_input("Inserisci PIN", type="password")

if pin == st.secrets["MY_PIN"]:
    st.sidebar.success("Accesso Autorizzato")
    if st.button("🛋️ Accendi Salotto", use_container_width=True):
        trigger_monkey("luce_salotto") # <--- Scrivi qui il nome esatto del tuo Trigger
else:
    st.info("Inserisci il PIN per sbloccare i comandi.")
