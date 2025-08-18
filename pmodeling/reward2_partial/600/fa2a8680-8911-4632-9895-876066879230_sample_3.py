import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = ['Client Meet', 'Requirement Gather', 'Module Design', 'Supplier Vetting', 'Component Order', 'Prototype Build', 'Field Testing', 'Test Analysis', 'Software Setup', 'Data Integration', 'Pilot Train', 'Compliance Check', 'Fleet Deploy', 'Remote Monitor', 'Maintenance Plan', 'Performance Tune']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the partial order model
root = StrictPartialOrder(nodes=transitions)

# Define the order dependencies
root.order.add_edge(transitions[0], transitions[1])  # Client Meet -> Requirement Gather
root.order.add_edge(transitions[1], transitions[2])  # Requirement Gather -> Module Design
root.order.add_edge(transitions[2], transitions[3])  # Module Design -> Supplier Vetting
root.order.add_edge(transitions[3], transitions[4])  # Supplier Vetting -> Component Order
root.order.add_edge(transitions[4], transitions[5])  # Component Order -> Prototype Build
root.order.add_edge(transitions[5], transitions[6])  # Prototype Build -> Field Testing
root.order.add_edge(transitions[6], transitions[7])  # Field Testing -> Test Analysis
root.order.add_edge(transitions[7], transitions[8])  # Test Analysis -> Software Setup
root.order.add_edge(transitions[8], transitions[9])  # Software Setup -> Data Integration
root.order.add_edge(transitions[9], transitions[10])  # Data Integration -> Pilot Train
root.order.add_edge(transitions[10], transitions[11])  # Pilot Train -> Compliance Check
root.order.add_edge(transitions[11], transitions[12])  # Compliance Check -> Fleet Deploy
root.order.add_edge(transitions[12], transitions[13])  # Fleet Deploy -> Remote Monitor
root.order.add_edge(transitions[13], transitions[14])  # Remote Monitor -> Maintenance Plan
root.order.add_edge(transitions[14], transitions[15])  # Maintenance Plan -> Performance Tune

# Print the final POWL model
print(root)