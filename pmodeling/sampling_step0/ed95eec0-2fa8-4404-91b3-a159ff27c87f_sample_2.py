import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activities = ['Trend Scan', 'Idea Harvest', 'Sector Match', 'Brainstorm Hub', 'Concept Filter', 'Prototype Build', 'Hybrid Testing', 'Stakeholder Sync', 'Risk Assess', 'Scenario Map', 'Strategy Align', 'Pilot Launch', 'Data Capture', 'Market Sense', 'Scale Plan']

# Create the workflow structure
root = StrictPartialOrder()

# Add activities as nodes
for activity in activities:
    root.add_node(Transition(label=activity))

# Define operators and edges
root.add_edge(root.nodes[0], root.nodes[1])  # Trend Scan -> Idea Harvest
root.add_edge(root.nodes[1], root.nodes[2])  # Idea Harvest -> Sector Match
root.add_edge(root.nodes[2], root.nodes[3])  # Sector Match -> Brainstorm Hub
root.add_edge(root.nodes[3], root.nodes[4])  # Brainstorm Hub -> Concept Filter
root.add_edge(root.nodes[4], root.nodes[5])  # Concept Filter -> Prototype Build
root.add_edge(root.nodes[5], root.nodes[6])  # Prototype Build -> Hybrid Testing
root.add_edge(root.nodes[6], root.nodes[7])  # Hybrid Testing -> Stakeholder Sync
root.add_edge(root.nodes[7], root.nodes[8])  # Stakeholder Sync -> Risk Assess
root.add_edge(root.nodes[8], root.nodes[9])  # Risk Assess -> Scenario Map
root.add_edge(root.nodes[9], root.nodes[10])  # Scenario Map -> Strategy Align
root.add_edge(root.nodes[10], root.nodes[11])  # Strategy Align -> Pilot Launch
root.add_edge(root.nodes[11], root.nodes[12])  # Pilot Launch -> Data Capture
root.add_edge(root.nodes[12], root.nodes[13])  # Data Capture -> Market Sense
root.add_edge(root.nodes[13], root.nodes[14])  # Market Sense -> Scale Plan

# Print the root node
print(root)