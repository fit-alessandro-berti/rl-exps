import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with exact names
activities = ['Site Review', 'Impact Study', 'Design Plan', 'Structure Mod', 'Hydroponics Setup', 'Crop Select', 'Nutrient Mix', 'Pest Control', 'Sensor Install', 'Staff Train', 'Compliance Audit', 'Packaging Dev', 'Logistics Plan', 'Community Engage', 'Sustainability Check']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Create the partial order
root = StrictPartialOrder(nodes=transitions)

# Add the edges based on the process description
root.order.add_edge(transitions[0], transitions[1])
root.order.add_edge(transitions[1], transitions[2])
root.order.add_edge(transitions[2], transitions[3])
root.order.add_edge(transitions[3], transitions[4])
root.order.add_edge(transitions[4], transitions[5])
root.order.add_edge(transitions[5], transitions[6])
root.order.add_edge(transitions[6], transitions[7])
root.order.add_edge(transitions[7], transitions[8])
root.order.add_edge(transitions[8], transitions[9])
root.order.add_edge(transitions[9], transitions[10])
root.order.add_edge(transitions[10], transitions[11])
root.order.add_edge(transitions[11], transitions[12])
root.order.add_edge(transitions[12], transitions[13])
root.order.add_edge(transitions[13], transitions[14])

# Print the root POWL model
print(root)