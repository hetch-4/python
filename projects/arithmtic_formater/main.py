def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if parts[1] not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        num1 = int(parts[0])
        num2 = int(parts[2])
        width = max(len(parts[0]), len(parts[2])) + 2

        first_line.append(parts[0].rjust(width))
        second_line.append(parts[1] + parts[2].rjust(width - 1))
        dashes.append('-' * width)
        
        if show_answers:
            result = str(num1 + num2 if parts[1] == '+' else num1 - num2)
            results.append(result.rjust(width))

    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dashes)
    )

    if show_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems


# Example usage
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems, True))
