# 4. Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и
# снятия средств в список.



from decimal import Decimal


class ATM:
    class Display:
        _GREETING = '''
         WELCOME! DIY ATM greets You.
         Sum multiplicity is 50.0 units.
         TAXES:
         1.5% of sum but not lesser than 30 and not greater than 600 units.
         3% of refinancing after 3 operations performed.
         10% after each operation if account amount is greater than 5e6 units.
         '''
        _menu: tuple

        def __init__(self, actions: tuple) -> None:
            self._menu = actions
            print(self._GREETING)

        def print_menu(self):
            print("Main menu:")
            print('\n'.join([f'{i:10}{label:>30}' for i, label in enumerate(self._menu, start=1)]))

        def print_text(self, text) -> None:
            print(text)

        def choose(self) -> str:
            return self._menu[self.get_menu_punct()]

        def get_menu_punct(self) -> int:
            pointer = -1
            while True:
                try:
                    pointer = int(input("Input your choice: ")) - 1
                except (TypeError, ValueError):
                    print("Wrong input")
                if 0 <= pointer < len(self._menu):
                    return pointer
                else:
                    print("Wrong input")

        def get_amount(self) -> Decimal:
            money_amt = -1
            while True:
                try:
                    money_amt = Decimal(input("Input amount of money: "))
                except TypeError:
                    print("Wrong input")
                if not money_amt % 50:
                    print(f'You entered:{round(money_amt, 2):.30}')
                    return money_amt
                else:
                    print('Amount is not multiple of 50.00 units')

    _ACTIONS: tuple = ('TAKE', 'PUT', 'CHECK', 'EXIT')
    _account_sum: Decimal = 0
    TAX_STANDARD: Decimal = Decimal(0.015)
    REFINANCE_RATE: Decimal = Decimal(0.03)
    TAX_WEALTH: Decimal = Decimal(0.1)
    CEILING_SUM: Decimal = Decimal(5e6)
    TAX_UPPER_LIM: Decimal = Decimal(600)
    TAX_LOWER_LIM: Decimal = Decimal(600)
    DIVISOR: Decimal = Decimal(50)

    def __init__(self) -> None:
        self.operation_count = 0
        self.display = self.Display(self._ACTIONS)
        # self.work()

    def get_money_rest(self) -> Decimal:
        return self._account_sum

    def put(self) -> None:
        self.display.print_text('Input amount of money to put: ')
        sum_to_put = self.display.get_amount()
        self._account_sum += sum_to_put
        self.operation_count += 1
        if self.TAX_LOWER_LIM < self._account_sum < self.TAX_UPPER_LIM:
            self._account_sum -= self._account_sum * self.TAX_STANDARD
        if self.operation_count > 3:
            self._account_sum += self._account_sum * self.REFINANCE_RATE
            self.operation_count = 0
        self.check()

    def take(self) -> None:
        self.display.print_text('Input amount of money to take: ')
        sum_to_take = self.display.get_amount()
        if self.get_money_rest() < sum_to_take:
            self.display.print_text('Not enough money!')
        else:
            self._account_sum -= sum_to_take
            self.operation_count += 1
            if self.TAX_LOWER_LIM < self._account_sum < self.TAX_UPPER_LIM:
                self._account_sum -= self._account_sum * self.TAX_STANDARD
            if self.operation_count > 3:
                self._account_sum += self._account_sum * self.REFINANCE_RATE
                self.operation_count = 0
        self.check()

    def check(self) -> None:
        self.display.print_text('Rest money on account:')
        self.display.print_text(self.get_money_rest())

    def check_operation(self) -> None:
        self.check()
        if self.TAX_LOWER_LIM < self._account_sum < self.TAX_UPPER_LIM:
            self._account_sum -= self._account_sum * self.TAX_STANDARD

    def work(self) -> None:
        while True:
            self.display.print_menu()
            match self.display.choose():
                case 'TAKE':
                    self.take()
                case 'PUT':
                    self.put()
                case 'CHECK':
                    self.check()
                case 'EXIT':
                    self.display.print_text("Good-bye! Exiting...")
                    raise SystemExit(0)
                case _:
                    self.display.print_text("ERROR! Internal error")


def main():
    atm = ATM()
    atm.work()


if __name__ == '__main__':
    main()
