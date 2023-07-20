from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test", methods=["POST"])
def test_connection():
    host = request.form.get("host")
    port = request.form.get("port")
    username = request.form.get("username")
    password = request.form.get("password")

    try:
        # Vérifie que le port est un entier
        port = int(port)

        # Créer l'URL de connexion à la base de données
        db_url = f"postgresql://{username}:{password}@{host}:{port}/"

        try:
            # Tente de se connecter à la base de données
            engine = create_engine(db_url)
            connection = engine.connect()
            connection.close()

            return """
            <html>
            <head>
                <title>Résultat du test de connexion</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 20px;
                        background-color: #f4f4f4;
                    }

                    h1 {
                        text-align: center;
                    }

                    .success {
                        color: #008000;
                        font-weight: bold;
                    }

                    .failure {
                        color: #ff0000;
                        font-weight: bold;
                    }
                </style>
            </head>
            <body>
                <h1>Résultat du test de connexion</h1>
                <p class="success">Connexion réussie à la base de données</p>
                <button onclick="window.history.back()">Retour</button>
            </body>
            </html>
            """
        except OperationalError:
            return """
            <html>
            <head>
                <title>Résultat du test de connexion</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 20px;
                        background-color: #f4f4f4;
                    }

                    h1 {
                        text-align: center;
                    }

                    .success {
                        color: #008000;
                        font-weight: bold;
                    }

                    .failure {
                        color: #ff0000;
                        font-weight: bold;
                    }
                </style>
            </head>
            <body>
                <h1>Résultat du test de connexion</h1>
                <p class="failure">Échec de la connexion à la base de données</p>
                <button onclick="window.history.back()">Retour</button>
            </body>
            </html>
            """
    except ValueError:
        return """
        <html>
        <head>
            <title>Erreur de saisie</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #f4f4f4;
                }

                h1 {
                    text-align: center;
                }

                .error {
                    color: #ff0000;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h1>Erreur de saisie</h1>
            <p class="error">Le port doit être un entier.</p>
            <button onclick="window.history.back()">Retour</button>
        </body>
        </html>
        """

if __name__ == "__main__":
    app.run()
