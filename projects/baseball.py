def calPoints(ops):
    record = []
    
    for op in ops:
        if op.lstrip('-').isdigit():  # Handles positive and negative integers
            record.append(int(op))
        elif op == "C":
            if record:
                record.pop()
        elif op == "D":
            if record:
                record.append(2 * record[-1])
        elif op == "+":
            if len(record) >= 2:
                
                record.append(record[-1] + record[-2])
    
    return sum(record)

# Example usage:
ops1 = input("scores")
print(calPoints(ops1))
#ops1 = ["5", "2", "C", "D", "+"]
#print(calPoints(ops1))  # Output: 30

#ops2 = ["5", "-2", "4", "C", "D", "9"]
#print(calPoints(ops2))  # Output: 27
