def pagination(
    current_page: int, total_pages: int, boundaries: int, around: int
) -> str:
    if not all(
        isinstance(variable, int)
        for variable in [current_page, total_pages, boundaries, around]
    ):
        raise ValueError("All values must be integers")
    if current_page < 1 or total_pages < 1:
        raise ValueError(
            "current_page & total_pages must be int, greater that 0"
        )
    if around < 0 or boundaries < 0:
        raise ValueError("amount & boundaries must be positive int")

    # Made boundaries
    if boundaries <= total_pages:
        start_boundary = [page for page in range(1, boundaries + 1)]
        end_boundary = [
            total_pages - page for page in range(boundaries - 1, -1, -1)
        ]
    else:
        start_boundary = end_boundary = [page for page in range(1, total_pages + 1)]

    # Add around pages for current page
    start_around = 1 if (current_page - around) < 1 else current_page - around
    end_around = (
        total_pages
        if current_page + around > total_pages
        else current_page + around
    )

    current_around = [page for page in range(start_around, end_around + 1)]

    # Made array only with visible pages
    visible = sorted(set(start_boundary + current_around + end_boundary))

    result_list = [
        visible[page]
        if visible[page] == visible[page - 1] + 1
        else f"... {visible[page]}"
        for page in range(1, len(visible))
    ]
    result_list.insert(0, visible[0])
    if not boundaries:
        result_list.append("...")
        if result_list[0] != 1:
            result_list.insert(0, "...")

    result = " ".join(map(str, result_list))

    print(result)
    return result


if __name__ == "__main__":
    # pagination(current_page=5, total_pages=300000000, boundaries=0, around=3)

    pagination(current_page=4, total_pages=10, boundaries=2, around=1)
