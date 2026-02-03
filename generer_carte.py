import folium
def code_carte(longitude, latitude,nom_cible):
    coords = (latitude,longitude)
    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=15)
    coords = [latitude,longitude]
    folium.Marker(location=coords, popup =nom_cible).add_to(map)
    polygon_coords = [
        [latitude + 0.001, longitude - 0.001],
        [latitude + 0.001, longitude + 0.001],
        [latitude - 0.001, longitude + 0.001],
        [latitude - 0.001, longitude - 0.001],
        [latitude + 0.001, longitude - 0.001]  # fermeture du polygone
    ]
     
    folium.Polygon(
        locations=polygon_coords,
        color='white',       # contour
        fill=True,          # remplissage
        fill_color='blue',  # couleur de remplissage
        fill_opacity=0.3    # transparence
    ).add_to(map)
    

    return  map._repr_html_()