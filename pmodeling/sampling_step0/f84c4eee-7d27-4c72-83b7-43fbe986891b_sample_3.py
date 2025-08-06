import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activity_list = ['Component Sourcing', 'Frame Assembly', 'Sensor Mounting', 'Wiring Harness', 'Circuit Testing', 'Firmware Loading', 'Initial Calibration', 'Software Integration', 'Flight Testing', 'Data Logging', 'Performance Tuning', 'Packaging Prep', 'Custom Labeling', 'Documentation Print', 'Quality Review', 'Client Training', 'Remote Monitoring', 'Firmware Update']

# Create the POWL model
root = StrictPartialOrder(nodes=[])
for activity in activity_list:
    root.nodes.append(Transition(label=activity))
root.order = {transition: set() for transition in root.nodes}

# Define the dependencies between activities
# These are just example dependencies, you may need to adjust them based on the actual process
root.order[root.nodes[0]].add(root.nodes[1])  # Component Sourcing -> Frame Assembly
root.order[root.nodes[1]].add(root.nodes[2])  # Frame Assembly -> Sensor Mounting
root.order[root.nodes[2]].add(root.nodes[3])  # Sensor Mounting -> Wiring Harness
root.order[root.nodes[3]].add(root.nodes[4])  # Wiring Harness -> Circuit Testing
root.order[root.nodes[4]].add(root.nodes[5])  # Circuit Testing -> Firmware Loading
root.order[root.nodes[5]].add(root.nodes[6])  # Firmware Loading -> Initial Calibration
root.order[root.nodes[6]].add(root.nodes[7])  # Initial Calibration -> Software Integration
root.order[root.nodes[7]].add(root.nodes[8])  # Software Integration -> Flight Testing
root.order[root.nodes[8]].add(root.nodes[9])  # Flight Testing -> Data Logging
root.order[root.nodes[9]].add(root.nodes[10])  # Data Logging -> Performance Tuning
root.order[root.nodes[10]].add(root.nodes[11])  # Performance Tuning -> Packaging Prep
root.order[root.nodes[11]].add(root.nodes[12])  # Packaging Prep -> Custom Labeling
root.order[root.nodes[12]].add(root.nodes[13])  # Custom Labeling -> Documentation Print
root.order[root.nodes[13]].add(root.nodes[14])  # Documentation Print -> Quality Review
root.order[root.nodes[14]].add(root.nodes[15])  # Quality Review -> Client Training
root.order[root.nodes[15]].add(root.nodes[16])  # Client Training -> Remote Monitoring
root.order[root.nodes[16]].add(root.nodes[17])  # Remote Monitoring -> Firmware Update

# Add loop nodes for quality assurance and post-delivery support
quality_assurance = OperatorPOWL(operator=Operator.LOOP, children=[root.nodes[15], root.nodes[16]])
post_delivery_support = OperatorPOWL(operator=Operator.LOOP, children=[root.nodes[17]])
root.nodes.append(quality_assurance)
root.nodes.append(post_delivery_support)
root.order.add_edge(root.nodes[15], quality_assurance)
root.order.add_edge(root.nodes[16], post_delivery_support)

# Print the final POWL model
print(root)