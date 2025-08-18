import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Design Layout', 'System Assembly', 'Climate Setup', 'Light Calibration', 'Seed Selection', 'Seedling Prep', 'Nutrient Mix', 'Irrigation Setup', 'Sensor Install', 'Data Integration', 'Waste Routing', 'Energy Audit', 'Regulation Check', 'Operational Test', 'Community Outreach']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the partial order
root = StrictPartialOrder(nodes=transitions)

# Define the order (dependencies)
root.order.add_edge(transitions[0], transitions[1])  # Site Survey -> Design Layout
root.order.add_edge(transitions[1], transitions[2])  # Design Layout -> System Assembly
root.order.add_edge(transitions[2], transitions[3])  # System Assembly -> Climate Setup
root.order.add_edge(transitions[3], transitions[4])  # Climate Setup -> Light Calibration
root.order.add_edge(transitions[4], transitions[5])  # Light Calibration -> Seed Selection
root.order.add_edge(transitions[5], transitions[6])  # Seed Selection -> Seedling Prep
root.order.add_edge(transitions[6], transitions[7])  # Seedling Prep -> Nutrient Mix
root.order.add_edge(transitions[7], transitions[8])  # Nutrient Mix -> Irrigation Setup
root.order.add_edge(transitions[8], transitions[9])  # Irrigation Setup -> Sensor Install
root.order.add_edge(transitions[9], transitions[10])  # Sensor Install -> Data Integration
root.order.add_edge(transitions[10], transitions[11])  # Data Integration -> Waste Routing
root.order.add_edge(transitions[11], transitions[12])  # Waste Routing -> Energy Audit
root.order.add_edge(transitions[12], transitions[13])  # Energy Audit -> Regulation Check
root.order.add_edge(transitions[13], transitions[14])  # Regulation Check -> Operational Test
root.order.add_edge(transitions[14], transitions[15])  # Operational Test -> Community Outreach

print(root)