import os
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from pystyle import Colorate, Colors

def clearterminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_art():
    # Function code:
    asciiart = """
╔═╗╔═╗╔╗╔╗╔╗╔═══╗    ╔═╗ ╔╗╔╗ ╔╗╔═╗╔═╗╔══╗ ╔═══╗╔═══╗
╚╗╚╝╔╝║║║║║║║╔═╗║    ║║╚╗║║║║ ║║║║╚╝║║║╔╗║ ║╔══╝║╔═╗║
 ╚╗╔╝ ║║║║║║║╚══╗    ║╔╗╚╝║║║ ║║║╔╗╔╗║║╚╝╚╗║╚══╗║╚═╝║
 ╔╝╚╗ ║╚╝╚╝║╚══╗║    ║║╚╗║║║║ ║║║║║║║║║╔═╗║║╔══╝║╔╗╔╝
╔╝╔╗╚╗╚╗╔╗╔╝║╚═╝║    ║║ ║║║║╚═╝║║║║║║║║╚═╝║║╚══╗║║║╚╗
╚═╝╚═╝ ╚╝╚╝ ╚═══╝    ╚╝ ╚═╝╚═══╝╚╝╚╝╚╝╚═══╝╚═══╝╚╝╚═╝
                                                          by XWS | NABIL
    """
    colored_ascii_art = Colorate.Horizontal(Colors.purple_to_red, asciiart)
    print(colored_ascii_art)

def main():
    display_ascii_art()

    try:
        while True:
            phone_number = input(Colorate.Horizontal(Colors.purple_to_red, "\nNumero de Telephone -> "))
            print(Colorate.Horizontal(Colors.purple_to_red, "Récupération d'informations..."))

            try:
                parsed_number = phonenumbers.parse(phone_number, None)
                if phonenumbers.is_valid_number(parsed_number):
                    if phone_number.startswith("+"):
                        country_code = "+" + phone_number[1:3]
                    else:
                        country_code = "None"
                    operator = carrier.name_for_number(parsed_number, "fr")
                    type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
                    timezones = timezone.time_zones_for_number(parsed_number)
                    timezone_info = timezones[0] if timezones else "None"
                    country = phonenumbers.region_code_for_number(parsed_number)
                    region = geocoder.description_for_number(parsed_number, "fr")
                    status = "Valid"

                    print(Colorate.Horizontal(Colors.purple_to_red, f"""
[+] Phone        : {phone_number}
[+] Country Code : {country_code}
[+] Country      : {country}
[+] Region       : {region}
[+] Timezone     : {timezone_info}
[+] Operator     : {operator}
[+] Type Number  : {type_number}
[+] Telegram -> https://t.me/{phone_number}
[+] Whatsapp -> https://wa.me/{phone_number}
[+] Viber -> https://viber.click/{phone_number}"""))

                else:
                    print(Colorate.Horizontal(Colors.purple_to_red, " Format invalide ! [Ex: +442012345678 or +33623456789]"))

            except Exception as e:
                print(Colorate.Horizontal(Colors.purple_to_red, f" Il y a une exception: {e}"))

            choice = input(Colorate.Horizontal(Colors.purple_to_red, "Veux tu continuer ? (y/n): ")).strip().lower()
            if choice != 'y':
                break
            else:
                clearterminal()
                display_ascii_art()

    except Exception as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    main()