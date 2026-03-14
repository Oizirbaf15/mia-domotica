import streamlit as st
import requests

# 1. Configurazione della pagina (Titolo e Icona nella scheda del browser)
st.set_page_config(page_title="La mia Casa Smart", page_icon="🏠", layout="centered")

# 2. Funzione per inviare il comando
def invia_comando(url_segreto):
    try:
        # Esegue la chiamata all'URL salvato nei Secrets
        risposta = requests.get(url_segreto)
        
        if risposta.status_code == 200:
            st.toast("✅ Comando eseguito!", icon="🎉")
        else:
            st.error(f"❌ Errore API {risposta.status_code}: {risposta.text}")
    except Exception as e:
        st.error(f"⚠️ Errore di connessione: {e}")

# 3. Interfaccia Grafica
st.title("🏠 Pannello di Controllo")
st.markdown("---")

# Barra laterale per la sicurezza
st.sidebar.header("Sicurezza")
pin_inserito = st.sidebar.text_input("Inserisci PIN di accesso", type="password")

# Controllo del PIN (deve corrispondere a quello nei Secrets)
if pin_inserito == st.secrets["MY_PIN"]:
    st.sidebar.success("Accesso Autorizzato")
    
    st.subheader("💡 Illuminazione")
    
    # Creiamo due colonne per rendere i pulsanti più belli
    col1, col2 = st.columns(2)
    
    with col1:
        # Pulsante per l'Abatjour
        if st.button("🛋️ Accendi Abatjour", use_container_width=True):
            invia_comando(st.secrets["URL_ABATJOUR"])
            
    with col2:
        # Esempio per un secondo dispositivo (che potrai aggiungere in futuro)
        if st.button("📺 Spegni Tutto", use_container_width=True):
            # Assicurati di avere URL_SPEGNI_TUTTO nei Secrets se usi questo
            # invia_comando(st.secrets["URL_SPEGNI_TUTTO"])
            st.info("Pulsante da configurare")

else:
    # Messaggio mostrato quando il PIN non è inserito o è sbagliato
    st.warning("Inserisci il PIN corretto nella barra laterale per visualizzare i comandi.")
    st.image("https://img.icons8.com/illustrations/lexaloffle/100/lock.png")

# Piè di pagina
st.markdown("---")
st.caption("Creato con Streamlit • Protetto da crittografia Secrets")
