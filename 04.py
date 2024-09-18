class FaturamentoMensal:
    # O método __init__ é o construtor da classe, que inicializa os atributos
    def __init__(self, estado, valor):
        self.estado = estado
        self.valor = valor



faturamentoSP = FaturamentoMensal("SP", 67836.43)
faturamentoRJ = FaturamentoMensal("RJ", 3678.66)
faturamentoMG = FaturamentoMensal("MG", 29229.88)
faturamentoES = FaturamentoMensal("ES", 27165.48)
faturamentoOutros = FaturamentoMensal("Outros", 19849.53)

faturamentos = [faturamentoSP, faturamentoRJ, faturamentoMG, faturamentoES, faturamentoOutros]

faturamentoTotal = sum(f.valor for f in faturamentos)

for faturamento in faturamentos:
    percentual = (faturamento.valor / faturamentoTotal) * 100
    print(f"{faturamento.estado} representa {percentual:.2f}% do faturamento total.")