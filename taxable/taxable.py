from abc import ABC, abstractmethod


class Taxable(ABC):
    # static attribute | class attribute
    VAT_PERCENTAGE = 14

    # abstract method : get_tax
    @abstractmethod
    def get_tax(self, amount):
        pass
