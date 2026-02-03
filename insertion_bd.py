from acces_bd import get_connection
from datetime import date

def insert_ville(nom):
    connexion = get_connection()
    cursor = connexion.cursor()

    cursor.execute("SELECT Id_Villes FROM villes WHERE Nom_Ville=%s", (nom,))
    ville = cursor.fetchone()

    if ville:
        id_ville = ville[0]
    else:
        cursor.execute(
            "INSERT INTO villes (Nom_Ville) VALUES (%s)",
            (nom,)
        )
        id_ville = cursor.lastrowid
        connexion.commit()

    cursor.close()
    connexion.close()
    return id_ville


def insert_typep(libelle):
    connexion = get_connection()
    cursor = connexion.cursor()

    cursor.execute(
        "SELECT Id_Types_Patrimoines FROM types_patrimoines WHERE Libelle=%s",
        (libelle,)
    )
    type_patrimoine = cursor.fetchone()
    if type_patrimoine:
        id_type = type_patrimoine[0]
    else:
        cursor.execute(
            "INSERT INTO types_patrimoines (Libelle) VALUES (%s)",
            (libelle,)
        )
        id_type = cursor.lastrowid
        connexion.commit()

    cursor.close()
    connexion.close()
    return id_type

def insert_patrimoine(nom, desc, lat, lon, id_ville, id_type, id_user=None):
    connexion = get_connection()
    cursor = connexion.cursor()

    cursor.execute("""
    SELECT Id_Patrimoines  FROM patrimoines
    WHERE Nom_Patrimoine = %s AND Id_Villes = %s
    """, (nom, id_ville))

    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO patrimoines
            (Nom_Patrimoine, Description_Patrimoine, Latitude_Patrimoine, Longitude_Patrimoine,
            Date_Creation, Id_Utilisateurs, Id_Villes, Id_Types_Patrimoines)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            nom,
            desc,
            lat,
            lon,
            date.today(),
            id_user,
            id_ville,
            id_type
        ))

        connexion.commit()
        cursor.close()
        connexion.close()

        


def recuperer_patrimoine():
    connexion= get_connection()
    cursor= connexion.cursor(dictionary=True)
    cursor.execute(""" 
       select p.Nom_Patrimoine ,p.Description_Patrimoine ,p.Latitude_Patrimoine, p.Longitude_Patrimoine,t.Libelle,v.Nom_Ville, p.Date_Creation 
       from patrimoines p, villes v, types_patrimoines t
       where p.Id_Villes=v.Id_Villes and p.Id_Types_Patrimoines=t.Id_Types_Patrimoines

    """)

    liste_patrimoine= cursor.fetchall()
    return liste_patrimoine

def recuperer_type():
    connexion= get_connection()
    cursor= connexion.cursor(dictionary=True)
    cursor.execute(""" 
       select distinct Libelle 
       from types_patrimoines 
    """)
    liste_type= cursor.fetchall()
    return liste_type




print(recuperer_patrimoine())
print(recuperer_type())

