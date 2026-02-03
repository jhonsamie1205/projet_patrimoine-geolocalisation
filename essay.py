from flask import Flask, render_template, request, redirect, url_for,flash;
from insertion_bd import insert_patrimoine, insert_typep, insert_ville, recuperer_patrimoine,recuperer_type
import folium
from generer_carte import code_carte;
app = Flask(__name__)
app.secret_key = "cle_secrete_pour_flash"

@app.route('/')
def index():
    return render_template("acceuil.html")

@app.route('/patrimoine')
def patrimoine():
    return render_template ("patrimoine.html")

@app.route('/traitement', methods=['POST'])
def traitement():
    try:
        donnee= request.form
        nom_patrimoine= donnee['nom_patrimoine']
        type_patrimoine= donnee['type_patrimoine']
        description_patrimoine= donnee['description_patrimoine']
        longitude_patrimoine =float( donnee['longitude_patrimoine'])
        latitude_patrimoine = float(donnee['latitude_patrimoine'])
        nom_ville = donnee['nom_ville']
        
    
   


        id_ville = insert_ville(
        nom_ville
        )

        id_type = insert_typep(
            type_patrimoine
        )

        insert_patrimoine(
            nom_patrimoine,
            description_patrimoine,
            latitude_patrimoine,
            longitude_patrimoine,
            id_ville,
            id_type
        )

    
        print(nom_patrimoine, type_patrimoine, nom_ville, description_patrimoine, longitude_patrimoine,  latitude_patrimoine )
        flash("Patrimoine enregistré avec succès", "success")
    except Exception as e:
        flash("erreur lors de l'enregistrement", "erreur")

    

    return redirect(url_for('patrimoine'))

@app.route('/liste_patrimoine')
def liste_patrimoine():
   liste_patrimoine = recuperer_patrimoine()
   liste_type=recuperer_type()
    
   return render_template('afficher_patrimoine.html', liste_patrimoine=liste_patrimoine, liste_type=liste_type)

@app.route('/afficher_carte')
def afficher_carte():
    longitude = request.args.get('Lo', type=float)
    latitude = request.args.get('La', type=float)
    nom_patrimoine = request.args.get('No_p')
   
    return render_template("carte.html",carte=code_carte(longitude,latitude,nom_patrimoine))
if __name__ == "__main__":
    app.run(debug=True)
