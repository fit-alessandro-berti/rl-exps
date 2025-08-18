from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities with their exact names
activities = ['Client Brief', 'Spec Analysis', 'Material Sourcing', 'Component Vetting', 'Frame Assembly', 'Sensor Install', 'Propulsion Setup', 'Calibration', 'Software Load', 'Flight Test', 'AI Training', 'QA Review', 'Mission Pack', 'Client Training', 'Deployment Support']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the partial order structure
root = StrictPartialOrder(nodes=transitions)

# Define the partial order dependencies
root.order.add_edge(transitions[0], transitions[1])
root.order.add_edge(transitions[1], transitions[2])
root.order.add_edge(transitions[2], transitions[3])
root.order.add_edge(transitions[3], transitions[4])
root.order.add_edge(transitions[4], transitions[5])
root.order.add_edge(transitions[5], transitions[6])
root.order.add_edge(transitions[6], transitions[7])
root.order.add_edge(transitions[7], transitions[8])
root.order.add_edge(transitions[8], transitions[9])
root.order.add_edge(transitions[9], transitions[10])
root.order.add_edge(transitions[10], transitions[11])
root.order.add_edge(transitions[11], transitions[12])
root.order.add_edge(transitions[12], transitions[13])

print(root)