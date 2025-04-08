from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Base de données simulée (JSON-like)
etudiants = [
    {"id": 1, "nom": "Maxim", "prenom": "Alice", "email": "alice.maxim@example.com"},
    {"id": 2, "nom": "Elodie", "prenom": "Bob", "email": "bob.elodie@example.com"}
]

@app.route('/api/etudiants', methods=['GET'])
def get_etudiants():
    """Liste tous les étudiants
    ---
    responses:
      200:
        description: Liste des étudiants
    """
    return jsonify(etudiants)

@app.route('/api/etudiants', methods=['POST'])
def ajouter_etudiant():
    """Ajouter un étudiant
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: Etudiant
          required:
            - nom
            - prenom
            - email
          properties:
            nom:
              type: string
            prenom:
              type: string
            email:
              type: string
    responses:
      201:
        description: Étudiant ajouté
    """
    data = request.get_json()
    new_id = max(e["id"] for e in etudiants) + 1 if etudiants else 1
    new_etudiant = {"id": new_id, **data}
    etudiants.append(new_etudiant)
    return jsonify(new_etudiant), 201

@app.route('/api/etudiants/<int:id>', methods=['DELETE'])
def supprimer_etudiant(id):
    """Supprimer un étudiant par ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Étudiant supprimé
    """
    global etudiants
    etudiants = [e for e in etudiants if e["id"] != id]
    return jsonify({"message": f"Étudiant {id} supprimé"}), 200

@app.route('/api/etudiants/<int:id>', methods=['PUT'])
def modifier_etudiant(id):
    """Mettre à jour un étudiant
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          id: Etudiant
          properties:
            nom:
              type: string
            prenom:
              type: string
            email:
              type: string
    responses:
      200:
        description: Étudiant mis à jour
    """
    data = request.get_json()
    for etudiant in etudiants:
        if etudiant["id"] == id:
            etudiant.update(data)
            return jsonify(etudiant), 200
    return jsonify({"message": "Étudiant non trouvé"}), 404

@app.route('/')
def accueil():
    return "<h1>Bienvenue sur l'API Étudiants</h1><p>Voir <a href='/apidocs'>la documentation Swagger</a></p>"

if __name__ == '__main__':
    app.run(debug=True)
