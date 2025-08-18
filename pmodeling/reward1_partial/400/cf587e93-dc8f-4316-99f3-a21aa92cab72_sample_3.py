import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their respective labels
activities = {
    'Seed Select': Transition(label='Seed Select'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Sensor Setup': Transition(label='Sensor Setup'),
    'Env Monitor': Transition(label='Env Monitor'),
    'Growth Scan': Transition(label='Growth Scan'),
    'Pest Control': Transition(label='Pest Control'),
    'Water Cycle': Transition(label='Water Cycle'),
    'Harvest Robo': Transition(label='Harvest Robo'),
    'Yield Assess': Transition(label='Yield Assess'),
    'Waste Process': Transition(label='Waste Process'),
    'Energy Sync': Transition(label='Energy Sync'),
    'Pack Biodeg': Transition(label='Pack Biodeg'),
    'Market Track': Transition(label='Market Track'),
    'Order Align': Transition(label='Order Align'),
    'Logistics Plan': Transition(label='Logistics Plan'),
    'Feedback Loop': Transition(label='Feedback Loop')
}

# Define the control flow
root = StrictPartialOrder(nodes=activities.values())
root.order.add_edge(activities['Seed Select'], activities['Nutrient Mix'])
root.order.add_edge(activities['Seed Select'], activities['Sensor Setup'])
root.order.add_edge(activities['Sensor Setup'], activities['Env Monitor'])
root.order.add_edge(activities['Env Monitor'], activities['Growth Scan'])
root.order.add_edge(activities['Growth Scan'], activities['Pest Control'])
root.order.add_edge(activities['Growth Scan'], activities['Water Cycle'])
root.order.add_edge(activities['Pest Control'], activities['Harvest Robo'])
root.order.add_edge(activities['Water Cycle'], activities['Harvest Robo'])
root.order.add_edge(activities['Harvest Robo'], activities['Yield Assess'])
root.order.add_edge(activities['Yield Assess'], activities['Waste Process'])
root.order.add_edge(activities['Waste Process'], activities['Energy Sync'])
root.order.add_edge(activities['Energy Sync'], activities['Pack Biodeg'])
root.order.add_edge(activities['Pack Biodeg'], activities['Market Track'])
root.order.add_edge(activities['Market Track'], activities['Order Align'])
root.order.add_edge(activities['Order Align'], activities['Logistics Plan'])
root.order.add_edge(activities['Logistics Plan'], activities['Feedback Loop'])