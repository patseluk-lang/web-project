"""Новий функціонал для гілки development."""


def greet(name: str) -> str:
    """Повертає рядок з привітанням."""
    return f"Привіт, {name}!"


def main() -> None:
    print(greet("Світе"))


if __name__ == "__main__":
    main()
