from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Survey'),
        Transition(label='Structural Audit'),
        Transition(label='Layout Design'),
        Transition(label='System Install'),
        Transition(label='Climate Setup'),
        Transition(label='Water Testing'),
        Transition(label='Nutrient Mix'),
        Transition(label='Seed Selection'),
        Transition(label='Planting Prep'),
        Transition(label='Growth Monitor'),
        Transition(label='Pest Inspect'),
        Transition(label='Harvest Plan'),
        Transition(label='Packaging Prep'),
        Transition(label='Distribution'),
        Transition(label='Sustainability')
    ]
)

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[1], root.nodes[3])
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