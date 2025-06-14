from flask import Flask, render_template, request
import pandas as pd
from predict import predict
import os
from werkzeug.utils import secure_filename



app = Flask(__name__, static_url_path='/static')

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    predictions = []
    if request.method == 'POST':
        # Cas 1 : fichiers séparés
        if 'transaction-file' in request.files and 'identity-file' in request.files:
            trans_file = request.files['transaction-file']
            id_file = request.files['identity-file']

            trans_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(trans_file.filename))
            id_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(id_file.filename))

            trans_file.save(trans_path)
            id_file.save(id_path)

            df_trans = pd.read_csv(trans_path)
            df_id = pd.read_csv(id_path)

            df = pd.merge(df_trans, df_id, on='TransactionID', how='left')

        # Cas 2 : fichier mergé
        elif 'merged-file' in request.files:
            merged_file = request.files['merged-file']
            merged_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(merged_file.filename))
            merged_file.save(merged_path)

            df = pd.read_csv(merged_path)

        # Sauvegarde pour que le dashboard puisse l'utiliser
        df.to_csv(os.path.join(app.config['UPLOAD_FOLDER'], 'last_uploaded.csv'), index=False)

        # prédiction pour la page d'accueil
        preds = predict(df)
        predictions = list(zip(preds['TransactionID'], preds['Predictions']))

    return render_template('index.html', predictions=predictions, page='index', title="Accueil", page_class="index")

@app.route('/dashboard')
def dashboard():
    try:
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'last_uploaded.csv')
        df = pd.read_csv(path)
        pred = predict(df)
        scores = pred['Predictions'].tolist()

        total = len(scores)
        fraud_count = sum(1 for s in scores if s >= 0.5)

        return render_template('dashboard.html',
                               total_transactions=total,
                               fraud_count=fraud_count,
                               scores=scores,
                               page='dashboard',
                               title="Dashboard",
                               page_class="dashboard")
    except Exception as e:
        return f"Erreur de chargement : {e}", 500


    return render_template('dashboard.html', stats=stats, title="Dashboard", page="dashboard", page_class="dashboard")

@app.route('/stats')
def stats():
    # Ici tu peux ajouter des stats plus détaillées avec fichiers ou calculs
    return render_template('stats.html', title="Statistiques", page="stats", page_class="stats")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
