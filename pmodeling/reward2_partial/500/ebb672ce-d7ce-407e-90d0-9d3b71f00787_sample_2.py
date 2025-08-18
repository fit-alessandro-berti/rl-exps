import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
activities = {
    'Site Survey': Transition(label='Site Survey'),
    'Design Layout': Transition(label='Design Layout'),
    'Modular Build': Transition(label='Modular Build'),
    'Install Pumps': Transition(label='Install Pumps'),
    'Setup Sensors': Transition(label='Setup Sensors'),
    'Calibrate Lights': Transition(label='Calibrate Lights'),
    'Nutrient Mix': Transition(label='Nutrient Mix'),
    'Plant Seeding': Transition(label='Plant Seeding'),
    'Water Cycling': Transition(label='Water Cycling'),
    'Energy Audit': Transition(label='Energy Audit'),
    'Pest Control': Transition(label='Pest Control'),
    'Growth Monitor': Transition(label='Growth Monitor'),
    'Data Analysis': Transition(label='Data Analysis'),
    'Yield Forecast': Transition(label='Yield Forecast'),
    'Supply Order': Transition(label='Supply Order'),
    'Waste Recycle': Transition(label='Waste Recycle'),
    'System Upgrade': Transition(label='System Upgrade')
}

# Create the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the dependencies between activities
root.order.add_edge(activities['Site Survey'], activities['Design Layout'])
root.order.add_edge(activities['Design Layout'], activities['Modular Build'])
root.order.add_edge(activities['Modular Build'], activities['Install Pumps'])
root.order.add_edge(activities['Install Pumps'], activities['Setup Sensors'])
root.order.add_edge(activities['Setup Sensors'], activities['Calibrate Lights'])
root.order.add_edge(activities['Calibrate Lights'], activities['Nutrient Mix'])
root.order.add_edge(activities['Nutrient Mix'], activities['Plant Seeding'])
root.order.add_edge(activities['Plant Seeding'], activities['Water Cycling'])
root.order.add_edge(activities['Water Cycling'], activities['Energy Audit'])
root.order.add_edge(activities['Energy Audit'], activities['Pest Control'])
root.order.add_edge(activities['Pest Control'], activities['Growth Monitor'])
root.order.add_edge(activities['Growth Monitor'], activities['Data Analysis'])
root.order.add_edge(activities['Data Analysis'], activities['Yield Forecast'])
root.order.add_edge(activities['Yield Forecast'], activities['Supply Order'])
root.order.add_edge(activities['Supply Order'], activities['Waste Recycle'])
root.order.add_edge(activities['Waste Recycle'], activities['System Upgrade'])

# Print the root of the POWL model
print(root)