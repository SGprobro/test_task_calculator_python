def main(input: str) -> str:

    try:
        parts = input.strip().split()
        if len(parts) != 3:
            raise ValueError("throws Exception")

        a_str, operation, b_str = parts

        a = int(a_str)
        b = int(b_str)

        if not (1 <= a <= 10) or not (1 <= b <= 10):
            raise ValueError("throws Exception")

        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            result = a // b

        return str(result)

    except ValueError as e:
        return e

expression = input()
print(main(expression))