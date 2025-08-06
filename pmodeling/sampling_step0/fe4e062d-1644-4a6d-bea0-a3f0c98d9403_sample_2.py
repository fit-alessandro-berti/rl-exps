import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Client Profiling', 'Ingredient Sourcing', 'Quality Check', 'Blend Experiment', 'Maturation Cycle', 'Sensory Panel', 'Refinement Loop', 'Stability Test', 'Packaging Design', 'Batch Coordination', 'Compliance Audit', 'Market Survey', 'Feedback Review', 'Order Finalize', 'Distribution Plan', 'Inventory Update']

# Define the transitions
transitions = {activity: Transition(label=activity) for activity in activities}

# Define the POWL model
root = StrictPartialOrder()

# Define the edges in the POWL model
root.order.add_edge(transitions['Client Profiling'], transitions['Ingredient Sourcing'])
root.order.add_edge(transitions['Ingredient Sourcing'], transitions['Quality Check'])
root.order.add_edge(transitions['Quality Check'], transitions['Blend Experiment'])
root.order.add_edge(transitions['Blend Experiment'], transitions['Maturation Cycle'])
root.order.add_edge(transitions['Maturation Cycle'], transitions['Sensory Panel'])
root.order.add_edge(transitions['Sensory Panel'], transitions['Refinement Loop'])
root.order.add_edge(transitions['Refinement Loop'], transitions['Stability Test'])
root.order.add_edge(transitions['Stability Test'], transitions['Packaging Design'])
root.order.add_edge(transitions['Packaging Design'], transitions['Batch Coordination'])
root.order.add_edge(transitions['Batch Coordination'], transitions['Compliance Audit'])
root.order.add_edge(transitions['Compliance Audit'], transitions['Market Survey'])
root.order.add_edge(transitions['Market Survey'], transitions['Feedback Review'])
root.order.add_edge(transitions['Feedback Review'], transitions['Order Finalize'])
root.order.add_edge(transitions['Order Finalize'], transitions['Distribution Plan'])
root.order.add_edge(transitions['Distribution Plan'], transitions['Inventory Update'])

# Return the root of the POWL model
return root