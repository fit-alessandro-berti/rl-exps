import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Design Layout', 'Modular Build', 'Install Pumps', 'Setup Sensors', 'Calibrate Lights', 'Nutrient Mix', 'Plant Seeding', 'Water Cycling', 'Energy Audit', 'Pest Control', 'Growth Monitor', 'Data Analysis', 'Yield Forecast', 'Supply Order', 'Waste Recycle', 'System Upgrade']

# Define the transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Define the transitions for the process
# Site Survey -> Design Layout -> Modular Build
# Modular Build -> Install Pumps -> Setup Sensors -> Calibrate Lights
# Modular Build -> Nutrient Mix -> Plant Seeding -> Water Cycling
# Modular Build -> Energy Audit -> Pest Control -> Growth Monitor
# Modular Build -> Data Analysis -> Yield Forecast -> Supply Order
# Modular Build -> Waste Recycle -> System Upgrade

# Create the POWL model
root = StrictPartialOrder(nodes=[transitions[activity] for activity in activities])
root.order.add_edge(transitions['Site Survey'], transitions['Design Layout'])
root.order.add_edge(transitions['Design Layout'], transitions['Modular Build'])
root.order.add_edge(transitions['Modular Build'], transitions['Install Pumps'])
root.order.add_edge(transitions['Modular Build'], transitions['Setup Sensors'])
root.order.add_edge(transitions['Modular Build'], transitions['Calibrate Lights'])
root.order.add_edge(transitions['Modular Build'], transitions['Nutrient Mix'])
root.order.add_edge(transitions['Modular Build'], transitions['Plant Seeding'])
root.order.add_edge(transitions['Modular Build'], transitions['Water Cycling'])
root.order.add_edge(transitions['Modular Build'], transitions['Energy Audit'])
root.order.add_edge(transitions['Modular Build'], transitions['Pest Control'])
root.order.add_edge(transitions['Modular Build'], transitions['Growth Monitor'])
root.order.add_edge(transitions['Modular Build'], transitions['Data Analysis'])
root.order.add_edge(transitions['Modular Build'], transitions['Yield Forecast'])
root.order.add_edge(transitions['Modular Build'], transitions['Supply Order'])
root.order.add_edge(transitions['Modular Build'], transitions['Waste Recycle'])
root.order.add_edge(transitions['Modular Build'], transitions['System Upgrade'])

# Print the POWL model
print(root)