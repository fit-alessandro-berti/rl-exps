import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = ['Site Analysis', 'Zoning Approval', 'Structural Check', 'Building Retrofit', 'Hydroponic Setup', 'Climate Control', 'Nutrient Design', 'Staff Hiring', 'Staff Training', 'Software Install', 'System Testing', 'Crop Planting', 'Growth Monitor', 'Pest Control', 'Harvest Plan']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the partial order structure
root = StrictPartialOrder(nodes=transitions)

# Add dependencies between activities
root.order.add_edge(transitions[0], transitions[1])  # Site Analysis -> Zoning Approval
root.order.add_edge(transitions[1], transitions[2])  # Zoning Approval -> Structural Check
root.order.add_edge(transitions[2], transitions[3])  # Structural Check -> Building Retrofit
root.order.add_edge(transitions[3], transitions[4])  # Building Retrofit -> Hydroponic Setup
root.order.add_edge(transitions[4], transitions[5])  # Hydroponic Setup -> Climate Control
root.order.add_edge(transitions[5], transitions[6])  # Climate Control -> Nutrient Design
root.order.add_edge(transitions[6], transitions[7])  # Nutrient Design -> Staff Hiring
root.order.add_edge(transitions[7], transitions[8])  # Staff Hiring -> Staff Training
root.order.add_edge(transitions[8], transitions[9])  # Staff Training -> Software Install
root.order.add_edge(transitions[9], transitions[10])  # Software Install -> System Testing
root.order.add_edge(transitions[10], transitions[11])  # System Testing -> Crop Planting
root.order.add_edge(transitions[11], transitions[12])  # Crop Planting -> Growth Monitor
root.order.add_edge(transitions[12], transitions[13])  # Growth Monitor -> Pest Control
root.order.add_edge(transitions[13], transitions[14])  # Pest Control -> Harvest Plan

# Print the final POWL model
print(root)