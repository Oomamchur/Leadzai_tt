import pytest

from pagination import pagination


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected_result",
    [
        (1, 10, 2, 0, "1 2 ... 9 10"),
        (10, 10, 2, 0, "1 2 ... 9 10"),
        (4, 5, 1, 0, "1 ... 4 5"),
        (4, 10, 2, 2, "1 2 3 4 5 6 ... 9 10"),
        (5, 10, 2, 0, "1 2 ... 5 ... 9 10"),
        (100, 10, 2, 0, "1 2 ... 9 10"),
    ],
)
def test_pagination_different_current_page(
    current_page, total_pages, boundaries, around, expected_result
):
    assert (
        pagination(current_page, total_pages, boundaries, around)
        == expected_result
    )


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected_result",
    [
        (5, 1, 1, 1, "1"),
        (5, 10, 2, 1, "1 2 ... 4 5 6 ... 9 10"),
        (5, 100000, 1, 1, "1 ... 4 5 6 ... 100000"),
    ],
)
def test_pagination_different_total_pages(
    current_page, total_pages, boundaries, around, expected_result
):
    assert (
        pagination(current_page, total_pages, boundaries, around)
        == expected_result
    )


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected_result",
    [
        (1, 10, 0, 1, "1 2 ..."),
        (3, 10, 0, 1, "... 2 3 4 ..."),
        (5, 10, 2, 0, "1 2 ... 5 ... 9 10"),
        (5, 10, 100, 0, "1 2 3 4 5 6 7 8 9 10"),
    ],
)
def test_pagination_different_boundaries(
    current_page, total_pages, boundaries, around, expected_result
):
    assert (
        pagination(current_page, total_pages, boundaries, around)
        == expected_result
    )


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected_result",
    [
        (1, 10, 1, 2, "1 2 3 ... 10"),
        (10, 10, 1, 2, "1 ... 8 9 10"),
        (5, 10, 1, 2, "1 ... 3 4 5 6 7 ... 10"),
        (5, 10, 1, 0, "1 ... 5 ... 10"),
    ],
)
def test_pagination_different_around(
    current_page, total_pages, boundaries, around, expected_result
):
    assert (
        pagination(current_page, total_pages, boundaries, around)
        == expected_result
    )


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected_result",
    [
        (1000000000, 10, 2, 1, "1 2 ... 9 10"),
        (3, 1000000000, 2, 1, "1 2 3 4 ... 999999999 1000000000"),
        (3, 10, 1000000000, 1, "1 2 3 4 5 6 7 8 9 10"),
        (3, 10, 2, 1000000000, "1 2 3 4 5 6 7 8 9 10"),

    ],
)
def test_pagination_big_values(
    current_page, total_pages, boundaries, around, expected_result
):
    assert (
        pagination(current_page, total_pages, boundaries, around)
        == expected_result
    )


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around",
    [
        (0, 10, 2, 1),
        (4, 0, 2, 1),
        (4, 10, -1, 1),
        (4, 10, 2, -1),
    ],
)
def test_pagination_raises_value_error(
    current_page, total_pages, boundaries, around
):
    with pytest.raises(ValueError):
        pagination(current_page, total_pages, boundaries, around)


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around",
    [
        (0.1, 10, 2, 1),
        (4, "0", 2, 1),
        (4, 10, (0, 1), 1),
        (4, 10, 2, [1, 3]),
    ],
)
def test_pagination_not_int_raises_value_error(
    current_page, total_pages, boundaries, around
):
    with pytest.raises(ValueError, match="All values must be integers"):
        pagination(current_page, total_pages, boundaries, around)
