import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Impact Study', 'Structure Check', 'Soil Testing', 'System Design', 'Seed Selection', 'Irrigation Setup', 'Lighting Install', 'Pest Control', 'Community Meet', 'Regulation Review', 'Waste Plan', 'Crop Monitor', 'Harvest Prep', 'Market Launch']

# Create the POWL model
root = StrictPartialOrder()

# Define the activities as transitions
transitions = {activity: Transition(label=activity) for activity in activities}

# Add transitions to the root model
for activity in activities:
    root.add_transition(transitions[activity])

# Define the process structure
root.add_transition(transitions['Site Survey'])
root.add_transition(transitions['Impact Study'])
root.add_transition(transitions['Structure Check'])
root.add_transition(transitions['Soil Testing'])
root.add_transition(transitions['System Design'])
root.add_transition(transitions['Seed Selection'])
root.add_transition(transitions['Irrigation Setup'])
root.add_transition(transitions['Lighting Install'])
root.add_transition(transitions['Pest Control'])
root.add_transition(transitions['Community Meet'])
root.add_transition(transitions['Regulation Review'])
root.add_transition(transitions['Waste Plan'])
root.add_transition(transitions['Crop Monitor'])
root.add_transition(transitions['Harvest Prep'])
root.add_transition(transitions['Market Launch'])

# Define the dependencies
root.add_edge(transitions['Site Survey'], transitions['Impact Study'])
root.add_edge(transitions['Impact Study'], transitions['Structure Check'])
root.add_edge(transitions['Structure Check'], transitions['Soil Testing'])
root.add_edge(transitions['Soil Testing'], transitions['System Design'])
root.add_edge(transitions['System Design'], transitions['Seed Selection'])
root.add_edge(transitions['Seed Selection'], transitions['Irrigation Setup'])
root.add_edge(transitions['Irrigation Setup'], transitions['Lighting Install'])
root.add_edge(transitions['Lighting Install'], transitions['Pest Control'])
root.add_edge(transitions['Pest Control'], transitions['Community Meet'])
root.add_edge(transitions['Community Meet'], transitions['Regulation Review'])
root.add_edge(transitions['Regulation Review'], transitions['Waste Plan'])
root.add_edge(transitions['Waste Plan'], transitions['Crop Monitor'])
root.add_edge(transitions['Crop Monitor'], transitions['Harvest Prep'])
root.add_edge(transitions['Harvest Prep'], transitions['Market Launch'])

# Print the root model
print(root)