from rotas import obter_rota_acessivel

# Exemplo de uso
origem = "rua joão luis vives 42, São Paulo"
destino = "Av. da Liberdade 532, São Paulo"

rota_acessivel = obter_rota_acessivel(origem, destino)
if rota_acessivel:
    print("Rota acessível:")
    for step in rota_acessivel["legs"][0]["steps"]:
        print(step["html_instructions"])
else:
    print("Não foi possível obter a rota acessível.")
   
