import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Client Profiling'),
        Transition(label='Ingredient Sourcing'),
        Transition(label='Quality Check'),
        Transition(label='Blend Experiment'),
        Transition(label='Maturation Cycle'),
        Transition(label='Sensory Panel'),
        Transition(label='Refinement Loop'),
        Transition(label='Stability Test'),
        Transition(label='Packaging Design'),
        Transition(label='Batch Coordination'),
        Transition(label='Compliance Audit'),
        Transition(label='Market Survey'),
        Transition(label='Feedback Review'),
        Transition(label='Order Finalize'),
        Transition(label='Distribution Plan'),
        Transition(label='Inventory Update')
    ]
)

# Define the dependencies
root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[1], root.nodes[2])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[5])
root.order.add_edge(root.nodes[5], root.nodes[6])
root.order.add_edge(root.nodes[6], root.nodes[7])
root.order.add_edge(root.nodes[7], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[12], root.nodes[13])
root.order.add_edge(root.nodes[13], root.nodes[14])

# Print the POWL model
print(root)