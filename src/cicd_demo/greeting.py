def greet(name: str) -> str:
    if not name or not name.strip():
        raise ValueError("name must be a non-empty string")
    return f"Hello, {name.strip()}!"
