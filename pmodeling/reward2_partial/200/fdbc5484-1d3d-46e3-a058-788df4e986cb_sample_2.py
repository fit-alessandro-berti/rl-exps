from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = ['Asset ID', 'Value Assess', 'Risk Scan', 'Market Review', 'Initial Offer', 'Counter Offer', 'Negotiation', 'Contract Draft', 'Legal Review', 'Digital Sign', 'Royalty Setup', 'Transfer Record', 'Compliance Check', 'Audit Schedule', 'Market Feedback', 'Strategy Update']

# Create transitions for each activity
transitions = {activity: Transition(label=activity) for activity in activities}

# Define the partial order graph
root = StrictPartialOrder(nodes=transitions.values())

# Define the dependencies between activities
root.order.add_edge(transitions['Asset ID'], transitions['Value Assess'])
root.order.add_edge(transitions['Value Assess'], transitions['Risk Scan'])
root.order.add_edge(transitions['Risk Scan'], transitions['Market Review'])
root.order.add_edge(transitions['Market Review'], transitions['Initial Offer'])
root.order.add_edge(transitions['Initial Offer'], transitions['Counter Offer'])
root.order.add_edge(transitions['Counter Offer'], transitions['Negotiation'])
root.order.add_edge(transitions['Negotiation'], transitions['Contract Draft'])
root.order.add_edge(transitions['Contract Draft'], transitions['Legal Review'])
root.order.add_edge(transitions['Legal Review'], transitions['Digital Sign'])
root.order.add_edge(transitions['Digital Sign'], transitions['Royalty Setup'])
root.order.add_edge(transitions['Royalty Setup'], transitions['Transfer Record'])
root.order.add_edge(transitions['Transfer Record'], transitions['Compliance Check'])
root.order.add_edge(transitions['Compliance Check'], transitions['Audit Schedule'])
root.order.add_edge(transitions['Audit Schedule'], transitions['Market Feedback'])
root.order.add_edge(transitions['Market Feedback'], transitions['Strategy Update'])

# Print the root to verify the model
print(root)