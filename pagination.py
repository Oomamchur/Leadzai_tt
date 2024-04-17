def pagination(
    current_page: int, total_pages: int, boundaries: int, around: int
) -> str:
    """I assumed that boundary can't be less 1.
    Because usually pagination always show the first and the last pages"""
    if current_page < 1 or total_pages < 1 or boundaries < 1:
        raise ValueError("current_page, total_pages, boundaries must be greater that 0")
    if around < 0:
        raise ValueError("amount must be positive int")

    pages = list(range(1, total_pages + 1))
    # Made boundaries
    start_boundary = pages[:boundaries]
    end_boundary = pages[-boundaries:]
    # Add around pages for current page
    start_around = 0 if (current_page - 1 - around) < 1 else current_page - 1 - around
    end_around = (
        total_pages if current_page + around > total_pages else current_page + around
    )
    current_around = pages[start_around:end_around]
    # Made array only with visible pages
    visible = sorted(set(start_boundary + current_around + end_boundary))

    result_list = [
        visible[i] if visible[i] == visible[i - 1] + 1 else f"... {visible[i]}"
        for i in range(1, len(visible))
    ]
    result_list.insert(0, visible[0])
    result = " ".join(map(str, result_list))
    print(result)
    return result


if __name__ == "__main__":
    pagination(current_page=5, total_pages=10, boundaries=1, around=1)
