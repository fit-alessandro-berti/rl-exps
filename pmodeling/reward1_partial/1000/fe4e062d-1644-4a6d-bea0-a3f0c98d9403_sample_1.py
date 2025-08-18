import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Client Profiling': Transition(label='Client Profiling'),
    'Ingredient Sourcing': Transition(label='Ingredient Sourcing'),
    'Quality Check': Transition(label='Quality Check'),
    'Blend Experiment': Transition(label='Blend Experiment'),
    'Maturation Cycle': Transition(label='Maturation Cycle'),
    'Sensory Panel': Transition(label='Sensory Panel'),
    'Refinement Loop': Transition(label='Refinement Loop'),
    'Stability Test': Transition(label='Stability Test'),
    'Packaging Design': Transition(label='Packaging Design'),
    'Batch Coordination': Transition(label='Batch Coordination'),
    'Compliance Audit': Transition(label='Compliance Audit'),
    'Market Survey': Transition(label='Market Survey'),
    'Feedback Review': Transition(label='Feedback Review'),
    'Order Finalize': Transition(label='Order Finalize'),
    'Distribution Plan': Transition(label='Distribution Plan'),
    'Inventory Update': Transition(label='Inventory Update')
}

# Define the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))
root.order.add_edge(activities['Client Profiling'], activities['Ingredient Sourcing'])
root.order.add_edge(activities['Ingredient Sourcing'], activities['Quality Check'])
root.order.add_edge(activities['Quality Check'], activities['Blend Experiment'])
root.order.add_edge(activities['Blend Experiment'], activities['Maturation Cycle'])
root.order.add_edge(activities['Maturation Cycle'], activities['Sensory Panel'])
root.order.add_edge(activities['Sensory Panel'], activities['Refinement Loop'])
root.order.add_edge(activities['Refinement Loop'], activities['Stability Test'])
root.order.add_edge(activities['Stability Test'], activities['Packaging Design'])
root.order.add_edge(activities['Packaging Design'], activities['Batch Coordination'])
root.order.add_edge(activities['Batch Coordination'], activities['Compliance Audit'])
root.order.add_edge(activities['Compliance Audit'], activities['Market Survey'])
root.order.add_edge(activities['Market Survey'], activities['Feedback Review'])
root.order.add_edge(activities['Feedback Review'], activities['Order Finalize'])
root.order.add_edge(activities['Order Finalize'], activities['Distribution Plan'])
root.order.add_edge(activities['Distribution Plan'], activities['Inventory Update'])

print(root)