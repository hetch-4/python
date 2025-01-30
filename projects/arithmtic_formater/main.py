def arranger(problems, show_answer = False):
    if len(problems) > 5:
        return "Error: Too many problems"
    fline = []
    sline = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if parts[1] not in ('+', ''):
            return 'Error: Operator muct be "+" or "-".'
        
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Number must only contain digits"
        
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Errror: Numbers cannot be more than four digits."
        
        num1 = int(parts[0])
        num2 = int(parts[2])
        width = max(len(parts[0]), len(parts[2])) + 2

        fline.append(parts[0].rjust(width))
        sline.append(parts[1] + parts[2].rjust(width - 1))
        dashes.append('-' * width)

        if show_answer:
            result = str(num1 + num2 if parts[1] == '+' else num1 - num2)        
            results.append(result.rjust(width))

        arranged_problems ={
            "  ".join(fline) + '\n' +
            "  ".join(sline) + '\n' +
            "  ".join(dashes)
            }
        
        if show_answer:
            arranged_problems += '\n' + ''.join(results)

        return arranged_problems

prob = ['32 + 698', '3301 - 2', '45 + 43', '123 + 49']
print(arranger(prob))