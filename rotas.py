import os
import requests
from dotenv import load_dotenv

url = "https://maps.googleapis.com/maps/api/directions/json"

load_dotenv()

def obter_rota_acessivel(origem, destino):
  api_key = os.getenv('GOOGLE_API_KEY')
  params = {
      "origin": origem,
      "destination": destino,
      "mode": "transit",  # Define o modo de transporte para transporte público
      "transit_mode": "subway",  # Define o modo de transporte público como ônibus e metro
      "key": api_key
  }

  response = requests.get(url, params=params)
  data = response.json()

  if data["status"] == "OK":
      # Extrai a primeira rota da resposta
      rota = data["routes"][0]
      return rota
  else:
      print("Erro ao obter a rota:", data["status"])
      return None