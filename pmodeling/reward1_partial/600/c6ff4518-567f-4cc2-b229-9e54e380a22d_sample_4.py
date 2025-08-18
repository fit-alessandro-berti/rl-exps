from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Culture Prep'),
    Transition(label='Milk Pasteurize'),
    Transition(label='Coagulation'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Draining'),
    Transition(label='Hand Molding'),
    Transition(label='Pressing'),
    Transition(label='Salting'),
    Transition(label='Rind Treatment'),
    Transition(label='Aging Setup'),
    Transition(label='Microclimate Control'),
    Transition(label='Flavor Profiling'),
    Transition(label='Quality Check'),
    Transition(label='Sensory Review'),
    Transition(label='Texture Inspect'),
    Transition(label='Eco Packaging'),
    Transition(label='Batch Labeling'),
    Transition(label='Blockchain Log'),
    Transition(label='Niche Shipping')
])

# Define the partial order dependencies
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
root.order.add_edge(root.nodes[14], root.nodes[15])
root.order.add_edge(root.nodes[15], root.nodes[16])

print(root)