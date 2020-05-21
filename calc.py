import json
import fileinput
import math

data = ""

totals = {}

def make(id: str,amount_per_second: float,ident: int = 0):
    x = data["recipes"][id]
    num_assemblers = x["time"]*amount_per_second
    machine_name = "basic assembler(s)"
    if "machine" in x:
        num_assemblers /= data["machines"][x["machine"]]["speed"]
        machine_name = data["machines"][x["machine"]]["name"]
    else:
        num_assemblers *= 2
    for i in range(ident):
        print(" ",end="")
    print("{}: {:.2}/s, {} {}".format (id, amount_per_second, math.ceil(num_assemblers), machine_name))
    if id not in totals:
        totals[id] = 0
    totals[id] += amount_per_second
    for y in x:
        if y != "machine" and y != "time" and y in data["recipes"]:
            make(y,amount_per_second*x[y],ident+4)

with open('recipes.json') as recipes:
    data = json.loads(recipes.read())
    print("Input the desired output separated by +. No spaces.")
    print("Example query: red_science*0.8+green_science*0.8+black_science*0.8+blue_science*0.8")
    thing = input("Query:").split("+")
    for item in thing:
        y = item.split("*")
        if y[0] not in data["recipes"]:
            print(y[0], "not found.")
            continue
        make(y[0],float(y[1]))
    print("\nTotals:")
    for id in totals:
        x = data["recipes"][id]
        num_assemblers = x["time"]*totals[id]
        machine_name = "basic assembler(s)"
        if "machine" in x:
            num_assemblers /= data["machines"][x["machine"]]["speed"]
            machine_name = data["machines"][x["machine"]]["name"]
        else:
            num_assemblers *= 2
        print("{}: {:.2}/s, {} {}".format (id, totals[id], math.ceil(num_assemblers), machine_name))

