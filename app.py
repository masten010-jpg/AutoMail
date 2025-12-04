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
mein Name ist Roony H. — ich arbeite freiberuflich neben dem Studium an praxisnahen Lösungen, die kleine Büros, Kanzleien und Dienstleister im Alltag digital entlasten. Ich bin derzeit in einer kurzen Erhebungsphase, um reale Probleme zu verstehen, bevor ich automatisierte Tools und Service-Pakete entwerfe.

Dürfte ich Ihnen 2 Minuten Ihrer Zeit bitten?
Ich habe eine sehr kurze Google-Umfrage erstellt (max. 8 Fragen). Die Antworten bleiben anonym (oder: werden nur zur Auswertung genutzt — keine Weitergabe an Dritte). Ziel ist es, echte Prioritäten zu erkennen — nicht, Ihnen etwas aufzudrücken.

Hier ist der Link: https://forms.gle/sQ5mV7GHgThwiKLK9

Kurz zur Transparenz:
• Ich handle derzeit als Privatperson/freiberuflich (kein eingetragener Betrieb).

• Ihre Teilnahme  ist freiwillig.
• Ihre Antworten werden ausschließlich zur Auswertung des Bedarfs und zur Entwicklung möglicher, unverbindlicher Lösungen verwendet.

• Wenn Sie nicht möchten, dass ich Sie weiter kontaktiere, schreiben Sie bitte kurz „Kein Kontakt“ in das freie Feld der Umfrage oder antworten Sie mir direkt auf diese E-Mail.

Danke für Ihre Zeit — selbst 2 Minuten helfen enorm, die richtigen Lösungen zu bauen. Wenn Sie möchten, sende ich Ihnen gern eine kurze Zusammenfassung der Ergebnisse und mögliche erste Ideen zurück.

Freundliche Grüße
H. Roony
Hinweis: Bitte antworten Sie einfach auf diese Nachricht, wenn Sie keine weiteren Mails wünschen
"""

template_w = """\
Betreff: {betrefftext}
Guten Tag sehr Geehrte Frau {nameabfr}.
mein Name ist Roony H. — ich arbeite freiberuflich neben dem Studium an praxisnahen Lösungen, die kleine Büros, Kanzleien und Dienstleister im Alltag digital entlasten. Ich bin derzeit in einer kurzen Erhebungsphase, um reale Probleme zu verstehen, bevor ich automatisierte Tools und Service-Pakete entwerfe.

Dürfte ich Ihnen 2 Minuten Ihrer Zeit bitten?
Ich habe eine sehr kurze Google-Umfrage erstellt (max. 8 Fragen). Die Antworten bleiben anonym (oder: werden nur zur Auswertung genutzt — keine Weitergabe an Dritte). Ziel ist es, echte Prioritäten zu erkennen — nicht, Ihnen etwas aufzudrücken.

Hier ist der Link: https://forms.gle/sQ5mV7GHgThwiKLK9

Kurz zur Transparenz:
• Ich handle derzeit als Privatperson/freiberuflich (kein eingetragener Betrieb).

• Ihre Teilnahme  ist freiwillig.
• Ihre Antworten werden ausschließlich zur Auswertung des Bedarfs und zur Entwicklung möglicher, unverbindlicher Lösungen verwendet.

• Wenn Sie nicht möchten, dass ich Sie weiter kontaktiere, schreiben Sie bitte kurz „Kein Kontakt“ in das freie Feld der Umfrage oder antworten Sie mir direkt auf diese E-Mail.

Danke für Ihre Zeit — selbst 2 Minuten helfen enorm, die richtigen Lösungen zu bauen. Wenn Sie möchten, sende ich Ihnen gern eine kurze Zusammenfassung der Ergebnisse und mögliche erste Ideen zurück.

Freundliche Grüße
H. Roony
Hinweis: Bitte antworten Sie einfach auf diese Nachricht, wenn Sie keine weiteren Mails wünschen
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
