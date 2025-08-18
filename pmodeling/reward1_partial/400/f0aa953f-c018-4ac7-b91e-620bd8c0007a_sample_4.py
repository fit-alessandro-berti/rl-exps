import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Design Layout', 'System Assembly', 'Climate Setup', 'Light Calibration', 'Seed Selection', 'Seedling Prep', 'Nutrient Mix', 'Irrigation Setup', 'Sensor Install', 'Data Integration', 'Waste Routing', 'Energy Audit', 'Regulation Check', 'Operational Test', 'Community Outreach']

# Create transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Create the POWL model
root = StrictPartialOrder(nodes=transitions.values())
root.order.add_edge(transitions['Site Survey'], transitions['Design Layout'])
root.order.add_edge(transitions['Design Layout'], transitions['System Assembly'])
root.order.add_edge(transitions['System Assembly'], transitions['Climate Setup'])
root.order.add_edge(transitions['Climate Setup'], transitions['Light Calibration'])
root.order.add_edge(transitions['Light Calibration'], transitions['Seed Selection'])
root.order.add_edge(transitions['Seed Selection'], transitions['Seedling Prep'])
root.order.add_edge(transitions['Seedling Prep'], transitions['Nutrient Mix'])
root.order.add_edge(transitions['Nutrient Mix'], transitions['Irrigation Setup'])
root.order.add_edge(transitions['Irrigation Setup'], transitions['Sensor Install'])
root.order.add_edge(transitions['Sensor Install'], transitions['Data Integration'])
root.order.add_edge(transitions['Data Integration'], transitions['Waste Routing'])
root.order.add_edge(transitions['Waste Routing'], transitions['Energy Audit'])
root.order.add_edge(transitions['Energy Audit'], transitions['Regulation Check'])
root.order.add_edge(transitions['Regulation Check'], transitions['Operational Test'])
root.order.add_edge(transitions['Operational Test'], transitions['Community Outreach'])

# Print the root model
print(root)