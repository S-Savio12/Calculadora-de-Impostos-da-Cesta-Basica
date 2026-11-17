"""
Semana 2 — O carrinho de compras


from produtos import ALIQUOTA_PADRAO, Produto


class Carrinho:
    """Guarda produtos e suas quantidades."""

    def __init__(self):
        self._itens = {}

    def adicionar(self, produto: Produto, quantidade: int = 1) -> None:
        if not isinstance(produto, Produto):
            raise TypeError("O produto deve ser uma instância de Produto")

        if not isinstance(quantidade, int) or isinstance(quantidade, bool) or quantidade < 1:
            raise ValueError("A quantidade deve ser um inteiro maior ou igual a 1")

        nome = produto.nome

        if nome in self._itens:
            self._itens[nome][1] += quantidade
        else:
            self._itens[nome] = [produto, quantidade]

    def remover(self, nome: str) -> None:
        if nome not in self._itens:
            raise KeyError(nome)

        del self._itens[nome]

    def subtotal(self) -> float:
        return sum(
            produto.preco * quantidade
            for produto, quantidade in self._itens.values()
        )

    def total_impostos(self) -> float:
        return sum(
            produto.imposto() * quantidade
            for produto, quantidade in self._itens.values()
        )

    def total(self) -> float:
        return self.subtotal() + self.total_impostos()

    def economia(self) -> float:
        imposto_padrao = sum(
            round(produto.preco * ALIQUOTA_PADRAO, 2) * quantidade
            for produto, quantidade in self._itens.values()
        )

        return imposto_padrao - self.total_impostos()

    def __len__(self) -> int:
        return sum(
            quantidade
            for produto, quantidade in self._itens.values()
        )

    def __contains__(self, nome: str) -> bool:
        return nome in self._itens


if __name__ == "__main__":
    from produtos import ProdutoCestaBasica, ProdutoPadrao

    c = Carrinho()
    c.adicionar(ProdutoCestaBasica("Feijão 1kg", 8.00), 2)
    c.adicionar(ProdutoPadrao("Chocolate", 10.00))
    print("Total:", c.total())
    print("Economia:", c.economia())
