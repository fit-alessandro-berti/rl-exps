import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = ['Data Ingestion', 'Quantum Setup', 'Route Optimize', 'Demand Forecast', 'Scenario Simulate', 'Risk Assess', 'Anomaly Detect', 'Supplier Sync', 'Quantum Communicate', 'Inventory Adjust', 'Procurement Plan', 'Performance Track', 'Feedback Loop', 'Decision Automate', 'Cost Analyze', 'Network Adapt']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the partial order graph
root = StrictPartialOrder(nodes=transitions)

# Define dependencies between activities
root.order.add_edge(transitions[0], transitions[1])  # Data Ingestion -> Quantum Setup
root.order.add_edge(transitions[1], transitions[2])  # Quantum Setup -> Route Optimize
root.order.add_edge(transitions[1], transitions[3])  # Quantum Setup -> Demand Forecast
root.order.add_edge(transitions[2], transitions[4])  # Route Optimize -> Scenario Simulate
root.order.add_edge(transitions[3], transitions[4])  # Demand Forecast -> Scenario Simulate
root.order.add_edge(transitions[4], transitions[5])  # Scenario Simulate -> Risk Assess
root.order.add_edge(transitions[4], transitions[6])  # Scenario Simulate -> Anomaly Detect
root.order.add_edge(transitions[5], transitions[7])  # Risk Assess -> Supplier Sync
root.order.add_edge(transitions[6], transitions[7])  # Anomaly Detect -> Supplier Sync
root.order.add_edge(transitions[7], transitions[8])  # Supplier Sync -> Quantum Communicate
root.order.add_edge(transitions[8], transitions[9])  # Quantum Communicate -> Inventory Adjust
root.order.add_edge(transitions[8], transitions[10])  # Quantum Communicate -> Procurement Plan
root.order.add_edge(transitions[9], transitions[11])  # Inventory Adjust -> Performance Track
root.order.add_edge(transitions[10], transitions[11])  # Procurement Plan -> Performance Track
root.order.add_edge(transitions[11], transitions[12])  # Performance Track -> Feedback Loop
root.order.add_edge(transitions[12], transitions[13])  # Feedback Loop -> Decision Automate
root.order.add_edge(transitions[13], transitions[14])  # Decision Automate -> Cost Analyze
root.order.add_edge(transitions[13], transitions[15])  # Decision Automate -> Network Adapt

print(root)