import pytest
from calculator import calculate_commission

class TestCalculateCommission:
    @pytest.mark.parametrize("amount, expected", [
        (100, 50.0),        # минимальная сумма
        (1000, 50.0),       # верхняя граница 1-го диапазона
        (1001, 100.0),      # нижняя граница 2-го диапазона
        (20000, 100.0),     # верхняя граница 2-го диапазона
        (20001, 400.01),    # нижняя граница 3-го диапазона
        (40000, 600.0),     # граница перед новым правилом
        (40001, 500.0),     # новое правило: свыше 40 000 - комиссия 500 руб.
        (50000, 500.0),     # максимальная сумма
    ])
    def test_commission_calculation(self, amount, expected):
        """Проверка корректного расчёта комиссии для всех диапазонов."""
        assert calculate_commission(amount) == pytest.approx(expected)

    @pytest.mark.parametrize("invalid_amount", [99, 50001, -1, 0])
    def test_commission_invalid_amount_raises_value_error(self, invalid_amount):
        """Негативные тесты: сумма вне допустимого диапазона."""
        with pytest.raises(ValueError):
            calculate_commission(invalid_amount)

    @pytest.mark.parametrize("invalid_type", ["abc", 1000.5, None, [1000]])
    def test_commission_invalid_type_raises_type_error(self, invalid_type):
        """Негативные тесты: передача нечислового значения."""
        with pytest.raises(TypeError):
            calculate_commission(invalid_type)

    # # Отдельные тесты для граничных значений )
    # def test_boundary_100(self):
    #     assert calculate_commission(100) == 50.0

    # def test_boundary_1000(self):
    #     assert calculate_commission(1000) == 50.0

    # def test_boundary_1001(self):
    #     assert calculate_commission(1001) == 100.0

    # def test_boundary_20000(self):
    #     assert calculate_commission(20000) == 100.0

    # def test_boundary_20001(self):
    #     assert calculate_commission(20001) == pytest.approx(400.01)

    # def test_boundary_50000(self):
    #     assert calculate_commission(50000) == 500.0