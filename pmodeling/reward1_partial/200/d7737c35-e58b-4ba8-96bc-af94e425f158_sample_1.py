from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Supplier Audit'),
    Transition(label='Culture Prep'),
    Transition(label='Milk Testing'),
    Transition(label='Fermentation Start'),
    Transition(label='pH Monitoring'),
    Transition(label='Curd Cutting'),
    Transition(label='Mold Inoculation'),
    Transition(label='Aging Setup'),
    Transition(label='Humidity Control'),
    Transition(label='Texture Check'),
    Transition(label='Flavor Profiling'),
    Transition(label='Batch Labeling'),
    Transition(label='Packaging'),
    Transition(label='Distribution'),
    Transition(label='Feedback Review'),
    Transition(label='Sustainability Audit')
])

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