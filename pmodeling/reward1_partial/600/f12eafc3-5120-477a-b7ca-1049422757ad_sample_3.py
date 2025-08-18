import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = ['Milk Selection', 'Quality Testing', 'Milk Pasteurize', 'Cheese Crafting', 'Controlled Aging', 'Sensory Review', 'Custom Packaging', 'Label Printing', 'Export Licensing', 'Documentation Prep', 'Customs Clearance', 'Cold Shipping', 'Delivery Tracking', 'Feedback Review', 'Market Analysis']

# Create transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Create the POWL model
root = StrictPartialOrder(nodes=transitions.values())

# Define the control flow
root.order.add_edge(transitions['Milk Selection'], transitions['Quality Testing'])
root.order.add_edge(transitions['Quality Testing'], transitions['Milk Pasteurize'])
root.order.add_edge(transitions['Milk Pasteurize'], transitions['Cheese Crafting'])
root.order.add_edge(transitions['Cheese Crafting'], transitions['Controlled Aging'])
root.order.add_edge(transitions['Controlled Aging'], transitions['Sensory Review'])
root.order.add_edge(transitions['Sensory Review'], transitions['Custom Packaging'])
root.order.add_edge(transitions['Custom Packaging'], transitions['Label Printing'])
root.order.add_edge(transitions['Label Printing'], transitions['Export Licensing'])
root.order.add_edge(transitions['Export Licensing'], transitions['Documentation Prep'])
root.order.add_edge(transitions['Documentation Prep'], transitions['Customs Clearance'])
root.order.add_edge(transitions['Customs Clearance'], transitions['Cold Shipping'])
root.order.add_edge(transitions['Cold Shipping'], transitions['Delivery Tracking'])
root.order.add_edge(transitions['Delivery Tracking'], transitions['Feedback Review'])
root.order.add_edge(transitions['Feedback Review'], transitions['Market Analysis'])

# Print the POWL model
print(root)