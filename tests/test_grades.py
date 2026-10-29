import pytest
from grades import calculate_average, get_highest_score, check_pass_status, get_grade_letter


# 1. @pytest.mark.parametrize + pytest.approx для дробових чисел
@pytest.mark.parametrize("scores, expected_avg", [
    ([80, 90, 100], 90.0),
    ([75.5, 82.3, 91.1], 82.96666666666667),
    ([100], 100.0),
])
def test_calculate_average_valid(scores, expected_avg):
    result = calculate_average(scores)
    assert result == pytest.approx(expected_avg, abs=1e-4)


# 2. Перевірка пошуку максимального балу
@pytest.mark.parametrize("scores, expected_max", [
    ([60, 75, 95, 80], 95),
    ([88.5, 88.4, 88.5], 88.5),
    ([0, 50, 100], 100),
])
def test_get_highest_score(scores, expected_max):
    assert get_highest_score(scores) == expected_max


# 3. Перевірка статусу «склав / не склав»
# Тестуються значення явно вище та явно нижче за 60.0
@pytest.mark.parametrize("scores, threshold, expected_status", [
    ([70, 80, 90], 60.0, True),    # Середній 80.0 > 60.0 -> True
    ([50, 40, 30], 60.0, False),   # Середній 40.0 < 60.0 -> False
    ([90, 95], 85.0, True),        # Середній 92.5 > 85.0 -> True
])
def test_check_pass_status(scores, threshold, expected_status):
    assert check_pass_status(scores, threshold) == expected_status


# 4. Перевірка конвертації в літерну оцінку
@pytest.mark.parametrize("score, expected_letter", [
    (95, 'A'),
    (82, 'B'),
    (74, 'C'),
    (63, 'D'),
    (45, 'F'),
])
def test_get_grade_letter(score, expected_letter):
    assert get_grade_letter(score) == expected_letter


# 5. Перевірка відмови на некоректні дані через pytest.raises(ValueError)
@pytest.mark.parametrize("invalid_scores", [
    [],                 # Порожній список
    [-10, 80, 90],      # Оцінка менше 0
    [70, 105, 80],      # Оцінка більше 100
])
def test_calculate_average_raises_value_error(invalid_scores):
    with pytest.raises(ValueError):
        calculate_average(invalid_scores)


def test_invalid_threshold_raises_value_error():
    with pytest.raises(ValueError):
        check_pass_status([70, 80], passing_threshold=150.0)