from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configuration de l'API Shopify
SHOP_NAME = "My Store"
API_KEY = "08e473cd8092e1c5cd2cdcfeea9be8f5"
PASSWORD = "2e30b62e45440c1578f242f1a46dd2ca"
API_VERSION = "2024-04"

# Endpoint pour envoyer la requête avec ExecuteThreeD = FALSE
@app.route('/execute_payment', methods=['POST'])
def execute_payment():
    # URL de l'API Shopify
    url = f"https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/{API_VERSION}/payments.json"

    # Exemple de données avec le paramètre ExecuteThreeD = FALSE
    data = {
        "transaction": {
            "amount": "100.00",
            "currency": "USD",
            "kind": "authorization",
            "ExecuteThreeD": False
        }
    }

    # Requête POST vers Shopify
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=data, headers=headers)

    # Retourne la réponse
    if response.status_code == 201:
        return jsonify({"status": "success", "response": response.json()})
    else:
        return jsonify({"status": "error", "message": response.text}), response.status_code

# Point de départ de l'application
if __name__ == "__main__":
    app.run(port=5000, debug=True)
