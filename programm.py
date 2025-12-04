import smtplib
from email.mime.text import MIMEText

# ================================
# Funktionen zur Abfrage
# ================================
def Abfragbetreff(x):
    return x

def AbfragName(n):
    return n


# ================================
# TEMPLATES für Mann/Frau
# ================================
template_m = """\
Betreff: {betrefftext}
Guten Tag sehr Geehrter Herr {nameabfr}.
mein Name ist Roony H. — ich arbeite freiberuflich neben dem Studium an praxisnahen Lösungen...

Hinweis: Bitte antworten Sie einfach auf diese Nachricht, wenn Sie keine weiteren Mails wünschen
"""

template_w = """\
Betreff: {betrefftext}
Guten Tag sehr Geehrte Frau {nameabfr}.
mein Name ist Roony H. — ich arbeite freiberuflich neben dem Studium...

Hinweis: Bitte antworten Sie einfach auf diese Nachricht, wenn Sie keine weiteren Mails wünschen
"""


# ========================================
# Funktion, um Gmail per SMTP zu senden
# ========================================
def sende_mail(empfaenger, betreff, text, gmail_user, app_passwort):
    """Senden einer Gmail-Nachricht mit App-Passwort"""

    msg = MIMEText(text)
    msg["Subject"] = betreff
    msg["From"] = gmail_user
    msg["To"] = empfaenger

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, app_passwort)
        server.send_message(msg)

    print("✅ E-Mail erfolgreich gesendet!")


# ================================
# HAUPTPROGRAMM
# ================================

print("🔐 Gmail Login – nichts wird gespeichert!")
gmail_user = input("Ihre Gmail-Adresse: ")
app_passwort = input("Ihr Gmail-App-Passwort: ")

print("\nLogin-Daten übernommen. Sie können jetzt Mails senden.\n")

while True:
    geschlecht = input("Männlich oder Weiblich? (m/w): ")

    # Abfrage für weiblich
    if geschlecht.lower() == "w":
        email = input("Geben Sie die Empfänger-Mail ein: ")
        nameabfr = input("Name der Person (z.B. Müller): ")
        betrefftext = input("Betreff eingeben: ")

        text = template_w.format(
            betrefftext=betrefftext,
            nameabfr=nameabfr
        )

    # Abfrage für männlich
    elif geschlecht.lower() == "m":
        email = input("Geben Sie die Empfänger-Mail ein: ")
        nameabfr = input("Name der Person (z.B. Meier): ")
        betrefftext = input("Betreff eingeben: ")

        text = template_m.format(
            betrefftext=betrefftext,
            nameabfr=nameabfr
        )

    else:
        print("❌ Bitte nur m oder w eingeben!")
        continue


    # ================================
    # Vorschau anzeigen
    # ================================
    print("\n===== VORSCHAU =====")
    print("Empfänger:", email)
    print("Betreff:  ", betrefftext)
    print("Inhalt:\n")
    print(text)
    print("=====================\n")


    # ================================
    # Mail wirklich senden?
    # ================================
    senden = input("Mail jetzt senden? (ja/nein): ")

    if senden.lower() == "ja":
        sende_mail(email, betrefftext, text, gmail_user, app_passwort)

    # Wiederholen?
    nochmal = input("Noch eine Mail senden? (ja/nein): ")
    if nochmal.lower() != "ja":
        print("Programm beendet. Tschüss!")
        break
