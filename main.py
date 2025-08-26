VOOS = [
    {
        "numero": 3141,
        "origem": "Portland",
        "destino": "Orange Country"
    },
    {
        "numero": 2173,
        "origem": "Portland",
        "destino": "Charlotte"
    },
    {
        "numero": 623,
        "origem": "Portland",
        "destino": "Daytona Beach"
    },
    {
        "numero": 5440,
        "origem": "Orange Country",
        "destino": "Montgomery"
    },
    {
        "numero": 5440,
        "origem": "Orange Country",
        "destino": "Los Angeles"
    },
    {
        "numero": 221,
        "origem": "Charlotte",
        "destino": "Memphis"
    },
    {
        "numero": 32,
        "origem": "Memphis",
        "destino": "Champaign"
    },
    {
        "numero": 981,
        "origem": "Montgomery",
        "destino": "Memphis"
    }
]



################## ALGORITMO DE VALIDAÇÃO DE ROTA #############################
def validate_route(origem, destino):
    
    voos_origem = [voo for voo in VOOS if voo['origem'] == origem]

    if len(voos_origem) == 0:
        return 'Não existe viagem a partir dessa origem'
    
    resultado = recursive_sequence(voos_origem, destino)

    if resultado:
        return 'É POSSÍVEL'

    return 'NÃO É POSSÍVEL'

def recursive_sequence(voos_origem, destino):

    for voo_origem in voos_origem:

        if voo_origem['destino'] == destino:
            return True
        else:
            resultado = recursive_sequence([dic for dic in VOOS if dic['origem'] == voo_origem['destino']], destino)

            if resultado:
                return True
            else:
                continue

    return False
                
################################################################################

################################# TESTES ############################################
        

print(validate_route('Portland', 'Orange Country')) # É POSSÍVEL
print(validate_route('Portland', 'Memphis')) # É POSSÍVEL
print(validate_route('Charlotte', 'Champaign')) # É POSSÍVEL
print(validate_route('Montgomery', 'Charlotte')) # NÃO É POSSÍVEL
print(validate_route('Portland', 'Montgomery')) # É POSSÍVEL
print(validate_route('Memphis', 'Portland')) # NÃO É POSSÍVEL
print(validate_route('Charlotte', 'Montgomery')) # É POSSÍVEL
print(validate_route('Portland', 'Los Angeles')) # É POSSÍVEL


