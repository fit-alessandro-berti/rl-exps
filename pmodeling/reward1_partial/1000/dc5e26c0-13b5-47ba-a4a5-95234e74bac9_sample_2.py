import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities (labels)
activities = ['Site Survey', 'Design Layout', 'Climate Setup', 'Sensor Install', 'Nutrient Mix', 'Automation Code', 'Crop Planning', 'Pest Control', 'Energy Audit', 'Waste Sort', 'Planting Tier', 'Harvest Prep', 'Logistics Plan', 'Community Meet', 'Data Review', 'System Upgrade']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the workflow model
root = StrictPartialOrder(nodes=transitions)

# Define the dependencies between activities
root.order.add_edge(transitions[0], transitions[1])  # Site Survey -> Design Layout
root.order.add_edge(transitions[1], transitions[2])  # Design Layout -> Climate Setup
root.order.add_edge(transitions[2], transitions[3])  # Climate Setup -> Sensor Install
root.order.add_edge(transitions[3], transitions[4])  # Sensor Install -> Nutrient Mix
root.order.add_edge(transitions[4], transitions[5])  # Nutrient Mix -> Automation Code
root.order.add_edge(transitions[5], transitions[6])  # Automation Code -> Crop Planning
root.order.add_edge(transitions[6], transitions[7])  # Crop Planning -> Pest Control
root.order.add_edge(transitions[7], transitions[8])  # Pest Control -> Energy Audit
root.order.add_edge(transitions[8], transitions[9])  # Energy Audit -> Waste Sort
root.order.add_edge(transitions[9], transitions[10])  # Waste Sort -> Planting Tier
root.order.add_edge(transitions[10], transitions[11])  # Planting Tier -> Harvest Prep
root.order.add_edge(transitions[11], transitions[12])  # Harvest Prep -> Logistics Plan
root.order.add_edge(transitions[12], transitions[13])  # Logistics Plan -> Community Meet
root.order.add_edge(transitions[13], transitions[14])  # Community Meet -> Data Review
root.order.add_edge(transitions[14], transitions[15])  # Data Review -> System Upgrade

print(root)