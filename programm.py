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

• Ihre Teilnahme ist freiwillig.
• Ihre Antworten werden ausschließlich zur Auswertung des Bedarfs und zur Entwicklung möglicher, unverbindlicher Lösungen verwendet.

• Wenn Sie nicht möchten, dass ich Sie weiter kontaktiere, schreiben Sie bitte kurz „Kein Kontakt“ in das freie Feld der Umfrage oder antworten Sie mir direkt auf diese E-Mail.

Danke für Ihre Zeit — selbst 2 Minuten helfen enorm, die richtigen Lösungen zu bauen. Wenn Sie möchten, sende ich Ihnen gern eine kurze Zusammenfassung der Ergebnisse und mögliche erste Ideen zurück.

Freundliche Grüße
H. Roony
Hinweis: Bitte antworten Sie einfach auf diese Nachricht, wenn Sie keine weiteren Mails wünschen

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
