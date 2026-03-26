"""간단한 파이썬 예제 코드."""


def greet(name: str) -> str:
    """이름을 받아 인사말을 반환합니다."""
    return f"안녕하세요, {name}님!"


if __name__ == "__main__":
    print(greet("코덱스"))
