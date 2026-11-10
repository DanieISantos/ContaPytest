# ContaPoupanca.py
from ContaBancaria import ContaBancaria
class ContaPoupanca():
    """Herda de ContaBancaria e adiciona funcionalidade de rendimento."""

    def render_juros(self, taxa: float) -> float:
        return self._saldo