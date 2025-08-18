root = StrictPartialOrder(nodes=[
    Transition(label='Site Survey'),
    Transition(label='Design Layout'),
    Transition(label='Procure Modules'),
    Transition(label='Install Framework'),
    Transition(label='Setup Sensors'),
    Transition(label='Calibrate Nutrients'),
    Transition(label='Configure IoT'),
    Transition(label='Plant Seeding'),
    Transition(label='Monitor Growth'),
    Transition(label='Manage Lighting'),
    Transition(label='Pest Control'),
    Transition(label='Recycle Waste'),
    Transition(label='Analyze Data'),
    Transition(label='Adjust Environment'),
    Transition(label='Harvest Crops'),
    Transition(label='Distribute Produce')
])

root.order.add_edge(Transition(label='Site Survey'), Transition(label='Design Layout'))
root.order.add_edge(Transition(label='Design Layout'), Transition(label='Procure Modules'))
root.order.add_edge(Transition(label='Procure Modules'), Transition(label='Install Framework'))
root.order.add_edge(Transition(label='Install Framework'), Transition(label='Setup Sensors'))
root.order.add_edge(Transition(label='Setup Sensors'), Transition(label='Calibrate Nutrients'))
root.order.add_edge(Transition(label='Calibrate Nutrients'), Transition(label='Configure IoT'))
root.order.add_edge(Transition(label='Configure IoT'), Transition(label='Plant Seeding'))
root.order.add_edge(Transition(label='Plant Seeding'), Transition(label='Monitor Growth'))
root.order.add_edge(Transition(label='Monitor Growth'), Transition(label='Manage Lighting'))
root.order.add_edge(Transition(label='Manage Lighting'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Recycle Waste'))
root.order.add_edge(Transition(label='Recycle Waste'), Transition(label='Analyze Data'))
root.order.add_edge(Transition(label='Analyze Data'), Transition(label='Adjust Environment'))
root.order.add_edge(Transition(label='Adjust Environment'), Transition(label='Harvest Crops'))
root.order.add_edge(Transition(label='Harvest Crops'), Transition(label='Distribute Produce'))