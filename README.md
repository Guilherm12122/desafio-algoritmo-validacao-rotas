# Validador de Rotas de Voos ✈️

Este projeto implementa um algoritmo em Python que verifica se **existe uma rota possível entre duas cidades**, dado um conjunto de voos disponíveis.  

A validação é feita de forma **recursiva**, explorando todas as conexões possíveis a partir da cidade de origem até alcançar (ou não) o destino.

---

## 🚀 Como funciona?

1. A lista `VOOS` contém os voos disponíveis, cada um com:
   - `numero`: número do voo  
   - `origem`: cidade de partida  
   - `destino`: cidade de chegada  

2. A função `validate_route(origem, destino)` é responsável por verificar se existe uma rota entre as cidades.  
   - Caso exista: retorna **"É POSSÍVEL"**  
   - Caso não exista: retorna **"NÃO É POSSÍVEL"**  

3. A verificação é feita de forma recursiva pela função `recursive_sequence`, que tenta encontrar caminhos alternativos até atingir o destino.

---

## 📂 Estrutura do código

```
.
├── voos.py        # Código principal
└── README.md      # Documentação do projeto
```

---

## 🖥️ Exemplo de uso

```python
print(validate_route('Portland', 'Orange Country')) # É POSSÍVEL
print(validate_route('Portland', 'Memphis'))        # É POSSÍVEL
print(validate_route('Charlotte', 'Champaign'))     # É POSSÍVEL
print(validate_route('Montgomery', 'Charlotte'))    # NÃO É POSSÍVEL
print(validate_route('Portland', 'Montgomery'))     # É POSSÍVEL
print(validate_route('Memphis', 'Portland'))        # NÃO É POSSÍVEL
print(validate_route('Charlotte', 'Montgomery'))    # É POSSÍVEL
print(validate_route('Portland', 'Los Angeles'))    # É POSSÍVEL
```

### Saída esperada:

```
É POSSÍVEL
É POSSÍVEL
É POSSÍVEL
NÃO É POSSÍVEL
É POSSÍVEL
NÃO É POSSÍVEL
É POSSÍVEL
É POSSÍVEL
```

---

## ⚡ Possíveis melhorias

- [ ] Adicionar tratamento para ciclos infinitos (quando uma cidade pode levar de volta à origem).  
- [ ] Implementar busca de **todas as rotas possíveis**, não apenas validação de existência.  
- [ ] Criar uma versão com **algoritmos de grafos** (ex: DFS ou BFS).  
- [ ] Permitir carregamento de voos a partir de um **arquivo externo (JSON/CSV)**.  
- [ ] Criar testes automatizados com `pytest`.  

---

## 📜 Licença

Este projeto é livre para estudo e modificações.  
