from abc import ABC, abstractmethod

from taxable.taxable_handler import TaxableHandler


class Taxable(ABC):
    # static attribute | class attribute
    VAT_PERCENTAGE = TaxableHandler.get_param_value('VAT_PCT') # 20

    # abstract method : get_tax
    @abstractmethod
    def get_tax(self, amount):
        pass
