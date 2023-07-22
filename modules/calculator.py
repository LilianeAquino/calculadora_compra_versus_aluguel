# calcula o aluguel de acordo com o reajuste anual
def calcular_valor_total_aluguel(valor_mensal_aluguel: float, taxa_aumento_aluguel: float, anos: int = 20) -> float:
  """
    Método responsável por calcular o valor do aluguel para determinado período
  """
  valor_total_aluguel = 0
  valor_mensal_aluguel_atual = valor_mensal_aluguel

  for _ in range(anos):
    valor_total_aluguel += 12 * valor_mensal_aluguel_atual
    valor_mensal_aluguel_atual *= (1 + taxa_aumento_aluguel/100)

  return round(valor_total_aluguel, 2)


# usa a fórmula de juros compostos para calcular o valor futuro do investimento
def calcular_valor_total_investimento(valor_investimento: float, taxa: float, anos: int = 20) -> float:
  """
      Método responsável por calcular o valor total de um investimento para determinado período
  """
  tempo_em_meses = anos*12
  taxa_mensal = 1 + taxa/100

  valor_total_investimento = valor_investimento * taxa_mensal ** tempo_em_meses

  return round(valor_total_investimento, 2)


# usa a fórmula de juros compostos para calcular o valor futuro do imóvel
def calcular_valorizacao_imovel(valor_imovel: float, taxa_valorizacao: float, anos: int = 20) -> float:
  """
    Método responsável por calcular a valorização do imóvel para determinado período
  """
  taxa_mensal = 1 + taxa_valorizacao/100
  tempo_em_meses = anos*12

  valor_imovel = valor_imovel * taxa_mensal ** tempo_em_meses
  return round(valor_imovel, 2)


# a ideia seria: alugo e invisto o dinheiro ou compro o imóvel? Se meus gastos com aluguel for maior do que meus rendimentos, devo comprar
# porque comprar vai sair mais barato do que alugar.
# aluguel é gasto e investimento é rendimento
def decisao_comprar_ou_alugar(valor_total_aluguel: float, valor_total_investido: float) -> str:
    if valor_total_aluguel > valor_total_investido:
        return "Comprar"
    elif valor_total_aluguel < valor_total_investido:
        return "Alugar"
    else:
        return "Ambas as opções são vantajosas"
