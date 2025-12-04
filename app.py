import streamlit as st
import smtplib
from email.mime.text import MIMEText

# ======================================================
# Streamlit Layout
# ======================================================
st.set_page_config(page_title="Mail-System", page_icon="📧")
st.title("📧 Automatisches Mail-System (Version 2)")

st.write("Dieses Tool basiert auf deinem Python-Programm, läuft aber als Streamlit-Web-App.")

# ======================================================
# Gmail Zugangsdaten
# ======================================================
with st.expander("🔐 Gmail Zugangsdaten eingeben (werden nicht gespeichert)"):
    gmail_user = st.text_input("Deine Gmail-Adresse:", placeholder="z.B. name@gmail.com")
    app_passwort = st.text_input("Gmail App-Passwort:", type="password")

# Wenn keine Zugangsdaten → abbrechen
if not gmail_user or not app_passwort:
    st.warning("Bitte Gmail-Adresse + App-Passwort eingeben.")
    st.stop()

# ======================================================
# Templates (identisch wie im Programm)
# ======================================================
template_m = """\
Betreff: {betrefftext}
Guten Tag sehr Geehrter Herr {nameabfr}.

mein Name ist Roony H. — ich arbeite freiberuflich neben dem Studium an praxisnahen Lösungen...

(gekürzt für Übersicht)
"""

template_w = """\
Betreff: {betrefftext}
Guten Tag sehr Geehrte Frau {nameabfr}.

mein Name ist Roony H. — ich arbeite freiberuflich neben dem Studium...

(gekürzt für Übersicht)
"""

# ======================================================
# Formular wie Programm 1
# ======================================================
st.header("📨 Mail-Daten eingeben")

geschlecht = st.radio("Geschlecht auswählen:", ["m", "w"])
empfaenger = st.text_input("Empfänger-Mail:")
nameabfr = st.text_input("Name der Person (z.B. Müller):")
betrefftext = st.text_input("Betreff der E-Mail:")

# ======================================================
# Template auswählen + generieren
# ======================================================
if geschlecht == "m":
    mail_text = template_m.format(betrefftext=betrefftext, nameabfr=nameabfr)
else:
    mail_text = template_w.format(betrefftext=betrefftext, nameabfr=nameabfr)

# ======================================================
# Vorschau
# ======================================================
st.subheader("📄 Vorschau der E-Mail")
st.code(mail_text)

# ======================================================
# Funktionen zum Senden 
# ======================================================
def sende_mail(empfaenger, betreff, text):
    msg = MIMEText(text)
    msg["Subject"] = betreff
    msg["From"] = gmail_user
    msg["To"] = empfaenger

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, app_passwort)
        server.send_message(msg)

# ======================================================
# Senden-Button
# ======================================================
if st.button("📧 E-Mail jetzt senden!"):
    if not empfaenger or not betrefftext or not nameabfr:
        st.error("Bitte alle Felder ausfüllen!")
    else:
        try:
            sende_mail(empfaenger, betrefftext, mail_text)
            st.success("✔ E-Mail erfolgreich gesendet!")
        except Exception as e:
            st.error(f"Fehler beim Senden: {e}")
