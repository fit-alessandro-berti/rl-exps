from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activities = ['Site Survey', 'Permit Review', 'Design Layout', 'System Assembly', 'Climate Setup', 'Nutrient Prep', 'Irrigation Test', 'Lighting Config', 'Energy Install', 'Sensor Setup', 'Automation Deploy', 'Crop Seeding', 'Waste Plan', 'Staff Training', 'Community Outreach', 'Yield Monitor', 'Maintenance Check']
transitions = [Transition(label=activity) for activity in activities]

# Define workflow
root = StrictPartialOrder(nodes=transitions)
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
root.order.add_edge(transitions[15], transitions[16])
root.order.add_edge(transitions[16], transitions[17])