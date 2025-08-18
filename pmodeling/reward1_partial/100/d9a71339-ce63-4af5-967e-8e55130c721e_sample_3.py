import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Structural Check': Transition(label='Structural Check'),
    'Modular Install': Transition(label='Modular Install'),
    'Hydroponic Setup': Transition(label='Hydroponic Setup'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Sensor Setup': Transition(label='Sensor Setup'),
    'AI Training': Transition(label='AI Training'),
    'Data Capture': Transition(label='Data Capture'),
    'Maintenance Plan': Transition(label='Maintenance Plan'),
    'Pest Scan': Transition(label='Pest Scan'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Harvest Sync': Transition(label='Harvest Sync'),
    'Quality Test': Transition(label='Quality Test'),
    'Package Prep': Transition(label='Package Prep'),
    'Logistics Plan': Transition(label='Logistics Plan')
}

# Define the POWL model structure
root = StrictPartialOrder(nodes=[
    activities['Site Survey'],
    activities['Structural Check'],
    OperatorPOWL(operator=Operator.LOOP, children=[
        OperatorPOWL(operator=Operator.XOR, children=[
            activities['Modular Install'],
            activities['Hydroponic Setup']
        ]),
        activities['Nutrient Mix'],
        activities['Sensor Setup']
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        activities['AI Training'],
        activities['Data Capture']
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        activities['Maintenance Plan'],
        activities['Pest Scan']
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        activities['Growth Monitor'],
        activities['Harvest Sync']
    ]),
    OperatorPOWL(operator=Operator.XOR, children=[
        activities['Quality Test'],
        activities['Package Prep']
    ]),
    activities['Logistics Plan']
])

# Add dependencies between nodes (uncomment and adjust as needed)
# root.order.add_edge(activities['Site Survey'], activities['Structural Check'])
# root.order.add_edge(activities['Structural Check'], activities['Modular Install'])
# root.order.add_edge(activities['Structural Check'], activities['Hydroponic Setup'])
# root.order.add_edge(activities['Modular Install'], activities['Nutrient Mix'])
# root.order.add_edge(activities['Hydroponic Setup'], activities['Nutrient Mix'])
# root.order.add_edge(activities['Modular Install'], activities['Sensor Setup'])
# root.order.add_edge(activities['Hydroponic Setup'], activities['Sensor Setup'])
# root.order.add_edge(activities['Modular Install'], activities['AI Training'])
# root.order.add_edge(activities['Hydroponic Setup'], activities['AI Training'])
# root.order.add_edge(activities['Modular Install'], activities['Data Capture'])
# root.order.add_edge(activities['Hydroponic Setup'], activities['Data Capture'])
# root.order.add_edge(activities['Modular Install'], activities['Maintenance Plan'])
# root.order.add_edge(activities['Hydroponic Setup'], activities['Maintenance Plan'])
# root.order.add_edge(activities['Modular Install'], activities['Pest Scan'])
# root.order.add_edge(activities['Hydroponic Setup'], activities['Pest Scan'])
# root.order.add_edge(activities['Modular Install'], activities['Growth Monitor'])
# root.order.add_edge(activities['Hydroponic Setup'], activities['Growth Monitor'])
# root.order.add_edge(activities['Modular Install'], activities['Harvest Sync'])
# root.order.add_edge(activities['Hydroponic Setup'], activities['Harvest Sync'])
# root.order.add_edge(activities['Modular Install'], activities['Quality Test'])
# root.order.add_edge(activities['Hydroponic Setup'], activities['Quality Test'])
# root.order.add_edge(activities['Modular Install'], activities['Package Prep'])
# root.order.add_edge(activities['Hydroponic Setup'], activities['Package Prep'])
# root.order.add_edge(activities['Modular Install'], activities['Logistics Plan'])
# root.order.add_edge(activities['Hydroponic Setup'], activities['Logistics Plan'])

print(root)