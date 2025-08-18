import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = ['Site Analysis', 'Structure Check', 'Climate Setup', 'Hydroponics Install', 'Nutrient Mix', 'Seed Select', 'Light Schedule', 'Irrigation Plan', 'Health Monitor', 'Pest Control', 'Robotic Harvest', 'Clean Packaging', 'Distribution Plan', 'Data Collection', 'Cycle Feedback']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the process structure
root = StrictPartialOrder(nodes=transitions)

# Define the dependencies between activities
root.order.add_edge(transitions[0], transitions[1])  # Site Analysis -> Structure Check
root.order.add_edge(transitions[1], transitions[2])  # Structure Check -> Climate Setup
root.order.add_edge(transitions[2], transitions[3])  # Climate Setup -> Hydroponics Install
root.order.add_edge(transitions[3], transitions[4])  # Hydroponics Install -> Nutrient Mix
root.order.add_edge(transitions[4], transitions[5])  # Nutrient Mix -> Seed Select
root.order.add_edge(transitions[5], transitions[6])  # Seed Select -> Light Schedule
root.order.add_edge(transitions[6], transitions[7])  # Light Schedule -> Irrigation Plan
root.order.add_edge(transitions[7], transitions[8])  # Irrigation Plan -> Health Monitor
root.order.add_edge(transitions[8], transitions[9])  # Health Monitor -> Pest Control
root.order.add_edge(transitions[9], transitions[10])  # Pest Control -> Robotic Harvest
root.order.add_edge(transitions[10], transitions[11])  # Robotic Harvest -> Clean Packaging
root.order.add_edge(transitions[11], transitions[12])  # Clean Packaging -> Distribution Plan
root.order.add_edge(transitions[12], transitions[13])  # Distribution Plan -> Data Collection
root.order.add_edge(transitions[13], transitions[14])  # Data Collection -> Cycle Feedback

# Print the root to verify
print(root)