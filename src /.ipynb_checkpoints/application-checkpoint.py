import streamlit as st
import joblib
import re
import string

# =============================
# 🔁 Chargement du modèle et du vectorizer
# =============================
model = joblib.load("../model/modele_registre.pkl")
vectorizer = joblib.load("../model/vectorizer_tfidf.pkl")

# =============================
# 🧼 Fonction de nettoyage
# =============================
def nettoyer_texte(texte):
    texte = str(texte).lower()
    texte = re.sub(r"\d+", "", texte)
    texte = texte.translate(str.maketrans("", "", string.punctuation))
    return texte.strip()

# =============================
# 🔍 Fonction de prédiction
# =============================
def predire_registre(phrase):
    phrase_clean = nettoyer_texte(phrase)
    vect = vectorizer.transform([phrase_clean])
    return model.predict(vect)[0]

# =============================
# 🎛️ Interface Streamlit
# =============================
st.set_page_config(page_title="Détecteur de registre", layout="centered")
st.title("📚 Détecteur de registre linguistique")
st.markdown("""
Entrez une phrase en français pour détecter automatiquement son registre :
- **familier**
- **courant**
- **académique**
""")

user_input = st.text_area("✍️ Votre phrase ici :", height=100)

if st.button("🔍 Prédire le registre"):
    if user_input.strip() == "":
        st.warning("Veuillez entrer une phrase.")
    else:
        registre = predire_registre(user_input)
        st.success(f"✅ Registre prédit : **{registre.upper()}**")
