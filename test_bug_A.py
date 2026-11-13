import pytest
from bug3_logic import find_max


@pytest.mark.parametrize(
    "scores, expected",
    [
        ([95, 85, 70, 60], 95),  # 최댓값이 처음
        ([70, 95, 85, 60], 95),  # 최댓값이 중간
        ([70, 85, 60, 95], 95),  # 최댓값이 마지막
        ([10, 20, 30], 30),      # 오름차순
        ([7], 7),                # 원소 하나
    ],
)
def test_find_max(scores, expected):
    assert find_max(scores) == expected