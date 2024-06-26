def pagination(
    current_page: int, total_pages: int, boundaries: int, around: int
) -> str:
    for argument in [current_page, total_pages, boundaries, around]:
        if not isinstance(argument, int):
            raise ValueError("All values must be integers")
    if current_page < 1 or total_pages < 1:
        raise ValueError("current_page & total_pages must be greater that 0")
    if around < 0 or boundaries < 0:
        raise ValueError("amount & boundaries must be positive int")

    # Made boundaries
    if boundaries <= total_pages:
        start_boundary = list(range(1, boundaries + 1))
        end_boundary = list(range(total_pages - boundaries + 1, total_pages + 1))
    else:
        start_boundary = end_boundary = list(range(1, total_pages + 1))

    # Add around pages for current page
    start_around = current_page - around
    if current_page - around < 1:
        start_around = 1
    end_around = current_page + around
    if current_page + around > total_pages:
        end_around = total_pages
    current_around = list(range(start_around, end_around + 1))

    # Made array only with visible pages
    visible = sorted(set(start_boundary + current_around + end_boundary))

    result_list = [visible[0]]
    for page in range(1, len(visible)):
        if visible[page] == visible[page - 1] + 1:
            result_list.append(visible[page])
        else:
            result_list.append(f"... {visible[page]}")

    if not boundaries:
        if result_list[0] != 1:
            result_list.insert(0, "...")
        if current_around[-1] != total_pages:
            result_list.append("...")

    result = " ".join(map(str, result_list))

    print(result)
    return result


if __name__ == "__main__":
    pagination(current_page=9, total_pages=10, boundaries=0, around=1)
