import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
activities = ['Site Survey', 'Modular Design', 'System Build', 'Env Control', 'Seed Selection', 'Nutrient Mix', 'Planting Setup', 'Growth Monitor', 'Pest Control', 'Water Cycle', 'Data Capture', 'Yield Forecast', 'Waste Reuse', 'Stakeholder Meet', 'Compliance Check', 'Supply Sync']

# Create transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Define the POWL model
root = StrictPartialOrder(nodes=transitions.values())

# Add edges to the POWL model
root.order.add_edge(transitions['Site Survey'], transitions['Modular Design'])
root.order.add_edge(transitions['Modular Design'], transitions['System Build'])
root.order.add_edge(transitions['System Build'], transitions['Env Control'])
root.order.add_edge(transitions['Env Control'], transitions['Seed Selection'])
root.order.add_edge(transitions['Seed Selection'], transitions['Nutrient Mix'])
root.order.add_edge(transitions['Nutrient Mix'], transitions['Planting Setup'])
root.order.add_edge(transitions['Planting Setup'], transitions['Growth Monitor'])
root.order.add_edge(transitions['Growth Monitor'], transitions['Pest Control'])
root.order.add_edge(transitions['Pest Control'], transitions['Water Cycle'])
root.order.add_edge(transitions['Water Cycle'], transitions['Data Capture'])
root.order.add_edge(transitions['Data Capture'], transitions['Yield Forecast'])
root.order.add_edge(transitions['Yield Forecast'], transitions['Waste Reuse'])
root.order.add_edge(transitions['Waste Reuse'], transitions['Stakeholder Meet'])
root.order.add_edge(transitions['Stakeholder Meet'], transitions['Compliance Check'])
root.order.add_edge(transitions['Compliance Check'], transitions['Supply Sync'])

# Print the POWL model
print(root)