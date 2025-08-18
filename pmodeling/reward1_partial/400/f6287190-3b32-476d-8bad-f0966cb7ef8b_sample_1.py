import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities with their labels
activities = {
    'Seed Select': Transition(label='Seed Select'),
    'Climate Map': Transition(label='Climate Map'),
    'IoT Setup': Transition(label='IoT Setup'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Sensor Check': Transition(label='Sensor Check'),
    'Light Adjust': Transition(label='Light Adjust'),
    'Water Cycle': Transition(label='Water Cycle'),
    'Pest Scan': Transition(label='Pest Scan'),
    'Growth Audit': Transition(label='Growth Audit'),
    'Harvest Plan': Transition(label='Harvest Plan'),
    'Demand Sync': Transition(label='Demand Sync'),
    'Quality Grade': Transition(label='Quality Grade'),
    'Pack Items': Transition(label='Pack Items'),
    'Waste Compost': Transition(label='Waste Compost'),
    'Data Review': Transition(label='Data Review'),
    'Cycle Reset': Transition(label='Cycle Reset')
}

# Define the workflow model
root = StrictPartialOrder()

# Define the relationships between activities
root.order.add_edge(activities['Seed Select'], activities['Climate Map'])
root.order.add_edge(activities['Climate Map'], activities['IoT Setup'])
root.order.add_edge(activities['IoT Setup'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Sensor Check'])
root.order.add_edge(activities['Sensor Check'], activities['Light Adjust'])
root.order.add_edge(activities['Light Adjust'], activities['Water Cycle'])
root.order.add_edge(activities['Water Cycle'], activities['Pest Scan'])
root.order.add_edge(activities['Pest Scan'], activities['Growth Audit'])
root.order.add_edge(activities['Growth Audit'], activities['Harvest Plan'])
root.order.add_edge(activities['Harvest Plan'], activities['Demand Sync'])
root.order.add_edge(activities['Demand Sync'], activities['Quality Grade'])
root.order.add_edge(activities['Quality Grade'], activities['Pack Items'])
root.order.add_edge(activities['Pack Items'], activities['Waste Compost'])
root.order.add_edge(activities['Waste Compost'], activities['Data Review'])
root.order.add_edge(activities['Data Review'], activities['Cycle Reset'])
root.order.add_edge(activities['Cycle Reset'], activities['Seed Select'])

print(root)