FROM python:3.10-slim

WORKDIR /app

COPY . .

# Installation des d�pendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Point d'entr�e de l�application
CMD ["python", "App.py"]