FROM python:3.10-slim

WORKDIR /app

COPY . .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Point d'entrée de l’application
CMD ["python", "App.py"]