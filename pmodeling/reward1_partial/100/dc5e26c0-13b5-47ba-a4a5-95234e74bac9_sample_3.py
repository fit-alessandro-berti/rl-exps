import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'Climate Setup': Transition(label='Climate Setup'),
    'Sensor Install': Transition(label='Sensor Install'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Automation Code': Transition(label='Automation Code'),
    'Crop Planning': Transition(label='Crop Planning'),
    'Pest Control': Transition(label='Pest Control'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Waste Sort': Transition(label='Waste Sort'),
    'Planting Tier': Transition(label='Planting Tier'),
    'Harvest Prep': Transition(label='Harvest Prep'),
    'Logistics Plan': Transition(label='Logistics Plan'),
    'Community Meet': Transition(label='Community Meet'),
    'Data Review': Transition(label='Data Review'),
    'System Upgrade': Transition(label='System Upgrade')
}

# Define the partial order model
root = StrictPartialOrder(nodes=[
    activities['Site Survey'],
    activities['Design Layout'],
    activities['Climate Setup'],
    activities['Sensor Install'],
    activities['Nutrient Mix'],
    activities['Automation Code'],
    activities['Crop Planning'],
    activities['Pest Control'],
    activities['Energy Audit'],
    activities['Waste Sort'],
    activities['Planting Tier'],
    activities['Harvest Prep'],
    activities['Logistics Plan'],
    activities['Community Meet'],
    activities['Data Review'],
    activities['System Upgrade']
])

# Define dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['Climate Setup'])
root.order.add_edge(activities['Climate Setup'], activities['Sensor Install'])
root.order.add_edge(activities['Sensor Install'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Automation Code'])
root.order.add_edge(activities['Automation Code'], activities['Crop Planning'])
root.order.add_edge(activities['Crop Planning'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Energy Audit'])
root.order.add_edge(activities['Energy Audit'], activities['Waste Sort'])
root.order.add_edge(activities['Waste Sort'], activities['Planting Tier'])
root.order.add_edge(activities['Planting Tier'], activities['Harvest Prep'])
root.order.add_edge(activities['Harvest Prep'], activities['Logistics Plan'])
root.order.add_edge(activities['Logistics Plan'], activities['Community Meet'])
root.order.add_edge(activities['Community Meet'], activities['Data Review'])
root.order.add_edge(activities['Data Review'], activities['System Upgrade'])

# Print the final result
print(root)