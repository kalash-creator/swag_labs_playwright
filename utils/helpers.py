def parse_price(price_str: str) -> float:
    return float(price_str.replace("$", ""))


def format_price(price_float: float) -> str:
    return f"${price_float:.2f}"