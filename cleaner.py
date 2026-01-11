
'''
made by https://x.com/didjems_
Ce script m'a permis de scraper le tableau excel suivant : https://docs.google.com/spreadsheets/d/1NRvbp6W9-XPUABU_WHVk3YIE1uHwD6DX5G1WEP2_rSc/htmlview
Je l'ai ensuite rafistolé pour faire correspondre au fichier html.
'''

import json
from urllib.parse import urlparse, parse_qs, unquote

def clean_google_url(google_url):
    """Extrait l'URL de destination d'un lien Google Redirect."""
    parsed = urlparse(google_url)
    # Récupère le paramètre 'q' dans l'URL
    query_params = parse_qs(parsed.query)
    if 'q' in query_params:
        return query_params['q'][0]
    return google_url

def clean_yupoo_url(yupoo_url):
    """Extrait l'URL de destination d'un lien Google Redirect."""
    parsed = urlparse(yupoo_url)
    # Récupère le paramètre 'url' dans l'URL
    query_params = parse_qs(parsed.query)
    if 'url' in query_params:
        return query_params['url'][0]
    return yupoo_url

file_path = 'sellers copy.json'

# 1. Chargement
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_data = []
for item in data:
    # Création du nouvel objet avec les valeurs de base
    new_item = {}
    type_de_vendeur = item.get("type", "")
    if "👕" in type_de_vendeur:
        new_item["type"] = "vêtements"
    elif "👟" in type_de_vendeur:
        new_item["type"] = "chaussures"
    elif "👜" in type_de_vendeur:
        new_item["type"] = "accessoires"
    elif "👠" in type_de_vendeur:
        new_item["type"] = "femmes"
    elif "➕" in type_de_vendeur:
        new_item["type"] = "autres"
    elif "👕👟" in type_de_vendeur:
        new_item["type"] = "vêtements et chaussures"
    elif "👕 👟" in type_de_vendeur:
        new_item["type"] = "vêtements et chaussures"
    elif "👟👕" in type_de_vendeur:
        new_item["type"] = "vêtements et chaussures"
    elif "👜👠" in type_de_vendeur:
        new_item["type"] = "accessoires et femmes"
    elif "👠👜" in type_de_vendeur:
        new_item["type"] = "accessoires et femmes"
    elif "👕👜" in type_de_vendeur:
        new_item["type"] = "vêtements et accessoires"
    elif "👜👕" in type_de_vendeur:
        new_item["type"] = "vêtements et accessoires"
    elif "👟👠" in type_de_vendeur:
        new_item["type"] = "chaussures et femmes"
    elif "👠👟" in type_de_vendeur:
        new_item["type"] = "chaussures et femmes"
    elif "👟👜" in type_de_vendeur:
        new_item["type"] = "chaussures et accessoires"
    elif "👜👟" in type_de_vendeur:
        new_item["type"] = "chaussures et accessoires"
    else:
        new_item["type"] = item.get("type")

    new_item["name"] = item.get("name")

    # Logique pour le catalogue (Priorité Yupoo, puis Kakobuy)
    cata_yupoo = item.get("yupoo", "")
    if "yupoo" in cata_yupoo:
        new_item["catalog_type"] = "yupoo"
        new_item["catalog_url"] = clean_google_url(item["yupoo"])
    elif "weidian" in cata_yupoo:
        new_item["catalog_type"] = "weidian"
        new_item["catalog_url"] = clean_google_url(item["yupoo"])
    elif "taobao" in cata_yupoo:
        new_item["catalog_type"] = "taobao"
        new_item["catalog_url"] = clean_google_url(item["yupoo"])
    elif "1688" in cata_yupoo:
        new_item["catalog_type"] = "1688"
        new_item["catalog_url"] = clean_google_url(item["yupoo"])

    cata_kaka = item.get("kakobuy", "")
    #print(cata_kaka)
    if "kakobuy" in cata_kaka:
        new_item["catalog_type2"] = "kakobuy"
        new_item["catalog_url2"] = clean_google_url(item["kakobuy"])
    if "yupoo" in cata_kaka:
        new_item["catalog_type2"] = "yupoo2"
        new_item["catalog_url2"] = clean_google_url(item["kakobuy"])
    elif "vroum" in cata_kaka:
        new_item["catalog_type2"] = ""
        new_item["catalog_url2"] = ""

    # Champs standards
    new_item["known_for"] = item.get("known_for")
    new_item["quality_rating"] = item.get("quality_rating")
    new_item["price_rating"] = item.get("price_rating")
    new_item["description"] = item.get("description")

    # Logique pour le contact
    contact_url = item.get("contact", "")
    if "discord." in contact_url:
        contact_url = clean_google_url(item.get("contact", ""))
        if "discord" in contact_url:
            new_item["contact_type"] = "discord"
            new_item["contact_value"] = f"<a href='{contact_url}'>discord</a>"
    elif "discord" in contact_url:
        new_item["contact_type"] = "discord"
        new_item["contact_value"] = contact_url
    elif "WeChat" in contact_url :
        new_item["contact_type"] = "wechat"
        new_item["contact_value"] = contact_url
    elif "Wechat" in contact_url :
        new_item["contact_type"] = "wechat"
        new_item["contact_value"] = contact_url
    elif "wechat" in contact_url :
        new_item["contact_type"] = "wechat"
        new_item["contact_value"] = contact_url
    elif "whatsapp.com" in contact_url:
        contact_url = clean_google_url(item.get("contact", ""))
        new_item["contact_type"] = "whatsapp"
        new_item["contact_value"] = f"<a href='{contact_url}'>whatsapp</a>"
    elif "wa.me" in contact_url:
        contact_url = clean_google_url(item.get("contact", ""))
        new_item["contact_type"] = "whatsapp"
        new_item["contact_value"] = f"<a href='{contact_url}'>whatsapp</a>"
    elif "whatsapp" in contact_url :
        new_item["contact_type"] = "whatsapp"
        new_item["contact_value"] = contact_url
    elif "Whatsapp" in contact_url :
        new_item["contact_type"] = "whatsapp"
        new_item["contact_value"] = contact_url
    elif "WHATSAPP" in contact_url :
        new_item["contact_type"] = "whatsapp"
        new_item["contact_value"] = contact_url
    elif "WhatsApp" in contact_url :
        new_item["contact_type"] = "whatsapp"
        new_item["contact_value"] = contact_url
    else:
        new_item["contact_type"] = "autre"
        new_item["contact_value"] = contact_url

    # Logique pour verified
    if item.get("quality_rating", "") == None:
        new_item["verified"] = 'null'
    elif item.get("quality_rating", "") > 80:
        new_item["verified"] = 'true'
    else:
        new_item["verified"] = 'false'

    new_data.append(new_item)

# 3. Écrasement du fichier
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)

print("Transformation terminée avec succès !")