import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Design Layout', 'Climate Setup', 'Sensor Install', 'Nutrient Mix', 'Automation Code', 'Crop Planning', 'Pest Control', 'Energy Audit', 'Waste Sort', 'Planting Tier', 'Harvest Prep', 'Logistics Plan', 'Community Meet', 'Data Review', 'System Upgrade']
transitions = [Transition(label=activity) for activity in activities]
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(nodes=transitions)

# Define the control flow
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
root.order.add_edge(transitions[14], transitions[15])

# Print the final result
print(root)