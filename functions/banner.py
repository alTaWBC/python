def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """Creates a banner where text is centered

    Args:
        text (str, optional): Text to center. Defaults to " ".
        screen_width (int, optional): size of banner. Defaults to 80.

    Raises:
        ValueError: len(text) is larger than width
    """

    if len(text) > screen_width - 4:
        raise ValueError(f"String {text} is larger than \
            specified width {screen_width}")

    if text == "*":
        print("*"*screen_width)
    else:
        output_string = f"**{text.center(screen_width-4)}**"
        print(output_string)


banner_text("*")
banner_text("Hello you there")
banner_text("Hello you")
banner_text("Hello you there manelito")
banner_text("*")
banner_text("*" * 81, 85)
banner_text("*" * 81)
banner_text("Hello you there manelito is bigger", 90)
