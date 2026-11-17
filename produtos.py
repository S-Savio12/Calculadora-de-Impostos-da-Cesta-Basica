"""
Semana 1 — Modelando produtos


ALIQUOTA_PADRAO = 0.25


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor

    def aliquota(self):
        raise NotImplementedError(
            "A subclasse deve implementar o método aliquota()."
        )

    def imposto(self):
        return round(self.preco * self.aliquota(), 2)

    def preco_final(self):
        return round(self.preco + self.imposto(), 2)

    def __str__(self):
        return (
            f"{self.nome} - R$ {self.preco:.2f} "
            f"(imposto: R$ {self.imposto():.2f})"
        )


class ProdutoCestaBasica(Produto):
    def aliquota(self):
        return 0.0


class ProdutoReduzido(Produto):
    def aliquota(self):
        return ALIQUOTA_PADRAO * 0.40


class ProdutoPadrao(Produto):
    def aliquota(self):
        return ALIQUOTA_PADRAO
