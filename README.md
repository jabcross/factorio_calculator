# factorio_calculator
Simple factory calculator in Python, configured from a JSON file.

Type in a query (or pipe it in).

Example usage:

`echo "red_science*0.8+green_science*0.8+black_science*0.8+blue_science*0.8" | python calc.py`

Example output:

```
red_science: 0.8/s, 1 basic assembler(s)
    copper_plate: 0.8/s, 2 steel furnace(s)
        copper_ore: 0.8/s, 2 miners
    gear: 0.8/s, 1 basic assembler(s)
        iron_plate: 1.6/s, 3 steel furnace(s)
            iron_ore: 1.6/s, 7 miners
green_science: 0.8/s, 14 basic assembler(s)
    belt: 0.8/s, 1 basic assembler(s)
        iron_plate: 0.4/s, 1 steel furnace(s)
            iron_ore: 0.4/s, 2 miners
        gear: 0.4/s, 1 basic assembler(s)
            iron_plate: 0.8/s, 2 steel furnace(s)
                iron_ore: 0.8/s, 4 miners
    inserter: 0.8/s, 4 basic assembler(s)
        iron_plate: 0.8/s, 2 steel furnace(s)
            iron_ore: 0.8/s, 4 miners
        gear: 0.8/s, 1 basic assembler(s)
            iron_plate: 1.6/s, 3 steel furnace(s)
                iron_ore: 1.6/s, 7 miners
        green_circuit: 0.8/s, 2 basic assembler(s)
            iron_plate: 0.8/s, 2 steel furnace(s)
                iron_ore: 0.8/s, 4 miners
            cable: 2.4/s, 2 basic assembler(s)
                copper_plate: 1.2/s, 2 steel furnace(s)
                    copper_ore: 1.2/s, 3 miners
black_science: 0.8/s, 8 basic assembler(s)
    red_ammo: 0.4/s, 3 basic assembler(s)
        copper_plate: 2.0/s, 4 steel furnace(s)
            copper_ore: 2.0/s, 4 miners
        steel: 0.4/s, 4 steel furnace(s)
            iron_plate: 2.0/s, 4 steel furnace(s)
                iron_ore: 2.0/s, 8 miners
        yellow_ammo: 0.4/s, 1 basic assembler(s)
            iron_plate: 1.6/s, 3 steel furnace(s)
                iron_ore: 1.6/s, 7 miners
blue_science: 0.8/s, 20 basic assembler(s)
    sulfur: 0.4/s, 1 chemical plant(s)
        petroleum_gas: 6.0/s, 1 refinery(es)
            crude_oil: 1.3e+01/s, 14 pumpjack(s)
    red_circuit: 1.2/s, 15 basic assembler(s)
        plastic: 2.4/s, 2 chemical plant(s)
            petroleum_gas: 2.4e+01/s, 3 refinery(es)
                crude_oil: 5.3e+01/s, 54 pumpjack(s)
        cable: 4.8/s, 3 basic assembler(s)
            copper_plate: 2.4/s, 4 steel furnace(s)
                copper_ore: 2.4/s, 5 miners
        green_circuit: 2.4/s, 6 basic assembler(s)
            iron_plate: 2.4/s, 4 steel furnace(s)
                iron_ore: 2.4/s, 10 miners
            cable: 7.2/s, 4 basic assembler(s)
                copper_plate: 3.6/s, 6 steel furnace(s)
                    copper_ore: 3.6/s, 8 miners
    engine: 0.8/s, 16 basic assembler(s)
        steel: 0.8/s, 7 steel furnace(s)
            iron_plate: 4.0/s, 7 steel furnace(s)
                iron_ore: 4.0/s, 16 miners
        gear: 0.8/s, 1 basic assembler(s)
            iron_plate: 1.6/s, 3 steel furnace(s)
                iron_ore: 1.6/s, 7 miners
        pipe: 1.6/s, 2 basic assembler(s)
            iron_plate: 1.6/s, 3 steel furnace(s)
                iron_ore: 1.6/s, 7 miners

Totals:
red_science: 0.8/s, 1 basic assembler(s)
copper_plate: 1e+01/s, 16 steel furnace(s)
copper_ore: 1e+01/s, 20 miners
gear: 2.8/s, 3 basic assembler(s)
iron_plate: 1.9e+01/s, 31 steel furnace(s)
iron_ore: 1.9e+01/s, 77 miners
green_science: 0.8/s, 14 basic assembler(s)
belt: 0.8/s, 1 basic assembler(s)
inserter: 0.8/s, 4 basic assembler(s)
green_circuit: 3.2/s, 8 basic assembler(s)
cable: 1.4e+01/s, 8 basic assembler(s)
black_science: 0.8/s, 8 basic assembler(s)
red_ammo: 0.4/s, 3 basic assembler(s)
steel: 1.2/s, 10 steel furnace(s)
yellow_ammo: 0.4/s, 1 basic assembler(s)
blue_science: 0.8/s, 20 basic assembler(s)
sulfur: 0.4/s, 1 chemical plant(s)
petroleum_gas: 3e+01/s, 4 refinery(es)
crude_oil: 6.7e+01/s, 67 pumpjack(s)
red_circuit: 1.2/s, 15 basic assembler(s)
plastic: 2.4/s, 2 chemical plant(s)
engine: 0.8/s, 16 basic assembler(s)
pipe: 1.6/s, 2 basic assembler(s)
```

JSON is incomplete at the moment (I was filling it out as I played).