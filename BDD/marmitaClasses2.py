import bottle
import sqlite3

class Recette():
    def __init__(self, Id, nom, image, nbpers, preparation, cuisson, diff, ingredients, etapes, famille):
        self.Id = Id
        self.nom = nom
        self.image = image
        self.nombreDePersonnes = nbpers
        self.preparation = preparation
        self.cuisson = cuisson
        self.difficulte = diff
        self.ingredients = ingredients
        self.etapes = etapes
        self.famille = famille

class Famille():
    def __init__(self, Id, nom, image):
        self.Id = Id
        self.nom = nom
        self.image = image

class Ingredient():
    def __init__(self, Id, nom, quantite, unite=None):
        self.Id = Id
        self.nom = nom
        self.quantite = quantite
        self.unite = unite

class Etape():
    def __init__(self, num, texte):
        self.numero = num
        self.texte = texte

# Route pour les images
@bottle.route('/Images/<filename>')
def server_static(filename):
    return bottle.static_file(filename, root='Images')

@bottle.route('/accueil')
@bottle.view("accueil.tpl")
def accueil():
    conn = sqlite3.connect('Marmita.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Famille")
    ListeFamilles = cursor.fetchall()
    conn.commit()

    cursor.close()
    conn.close()
    LesFamilles=[]
    for i in range(len(ListeFamilles)):
        nv_famille=Famille(ListeFamilles[i][0],ListeFamilles[i][1],ListeFamilles[i][2])
        LesFamilles.append(nv_famille)
    print(LesFamilles)
    return dict(LesFamilles=LesFamilles)

#Pour acceder au fichier css relie au fichier accueil.tpl
@bottle.route('/styleAccueil.css')
@bottle.view('styleAccueil.css')
def style():
    response.content_type="text/css"
    return {}

@bottle.route('/<id_famille:int>')
@bottle.view("famille.tpl")
def famille(id_famille):
    conn = sqlite3.connect('Marmita.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Recettes WHERE ID_Famille=?", (id_famille,))
    ListesRecettes = cursor.fetchall()
    conn.commit()
    cursor.execute("SELECT Nom FROM Famille WHERE ID=?", (id_famille,))
    famille_nom = cursor.fetchone()[0]

    cursor.close()
    conn.close()
    LesRecettes=[]
    for i in range(len(ListesRecettes)):
        nv_recette=Recette(ListesRecettes[i][0],ListesRecettes[i][1],ListesRecettes[i][2],ListesRecettes[i][3],ListesRecettes[i][4],ListesRecettes[i][5],ListesRecettes[i][6],None,None,None)
        LesRecettes.append(nv_recette)
    print(LesRecettes)
    return dict(LesRecettes=LesRecettes, famille_nom=famille_nom)

# Pour acceder au fichier css relie au fichier Familles.tpl
@bottle.route('/styleFamille.css')
@bottle.view('styleFamille.css')
def style():
    response.content_type="text/css"
    return {}

@bottle.route('/recette<id_recette:int>')
@bottle.view("recette.tpl")
def recette(id_recette):
    conn = sqlite3.connect('Marmita.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Recettes WHERE ID=?", (id_recette,))
    ListeRecettes = cursor.fetchall()
    cursor.execute("SELECT nom, Quantite, Unite FROM IngredientsDeRecette INNER JOIN Ingredients ON ID_ingrdients = Ingredients.ID WHERE ID_recettes=?", (id_recette,))
    ListeIngredients = cursor.fetchall()
    cursor.execute("SELECT Numero, Descriptif FROM EtapeDeRecette WHERE ID_recettes=?", (id_recette,))
    ListeEtapes = cursor.fetchall()
    conn.commit()
    cursor.execute("SELECT Nom FROM Recettes WHERE ID=?", (id_recette,))
    recette_nom = cursor.fetchone()[0]

    cursor.close()
    conn.close()
    LesRecettes=[]
    for i in range(len(ListeRecettes)):
        nv_recette=Recette(ListeRecettes[i][0],ListeRecettes[i][1],ListeRecettes[i][2],ListeRecettes[i][3],ListeRecettes[i][4],ListeRecettes[i][5],ListeRecettes[i][6],ListeRecettes[i][7],None,None)
        LesRecettes.append(nv_recette)
    print(LesRecettes)

    LesIngredients=[]
    for i in range(len(ListeIngredients)):
        nv_ingredient=Ingredient(None,ListeIngredients[i][0],ListeIngredients[i][1],ListeIngredients[i][2])
        LesIngredients.append(nv_ingredient)
    print(LesIngredients)

    LesEtapes=[]
    for i in range(len(ListeEtapes)):
        nv_étape=Etape(ListeEtapes[i][0],ListeEtapes[i][1])
        LesEtapes.append(nv_étape)
    print(LesEtapes)
    return dict(LesRecettes=LesRecettes, LesIngredients=LesIngredients, LesEtapes=LesEtapes, recette_nom=recette_nom)

# Pour acceder au fichier css relie au fichier recette.tpl
@bottle.route('/styleRecette.css')
@bottle.view('styleRecette.css')
def style():
    response.content_type="text/css"
    return {}

@bottle.route('/chercherRecette')
@bottle.view("chercheRecette.tpl")
def chercherRecette():
    conn = sqlite3.connect('Marmita.db')
    c = conn.cursor()
    nom_recette = bottle.request.query.nom_recette
    c.execute("SELECT * FROM Recettes WHERE Nom LIKE ?", ('%' + nom_recette + '%',))
    result = c.fetchall()

    c.close()
    conn.close()
    LesRecettes=[]
    for i in range(len(result)):
        nv_recette=Recette(result[i][0],result[i][1],result[i][2],result[i][3],result[i][4],result[i][5],result[i][6],result[i][7],None,None)
        LesRecettes.append(nv_recette)
    print(LesRecettes)
    return dict(LesRecettes=LesRecettes)

# Route pour la page FAQ
@bottle.route('/faq')
@bottle.view('faq.tpl')
def faq():
    pass

# Route pour la page mentions légales
@bottle.route('/mentions-legales')
@bottle.view('MentionsLégales.tpl')
def MentionLégales():
    pass

# Route pour la page mentions légales
@bottle.route('/Conditions-Generales-Utilisation')
@bottle.view('Conditions-Generales-Utilisation.tpl')
def ConditionsGeneralesUtilisation():
    pass

bottle.run(bottle.app(), host='localhost', port=8080, debug=True)