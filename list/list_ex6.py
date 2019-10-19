t = list()

while True:
    inp = input("Enter a number:")
    if inp == 'done':
        break
    t.append(float(inp))

print("Maximum: %f" % max(t))
print("Minimum: %f" % min(t))
print("Average: %f\n" % (sum(t)/len(t)))