from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Milk Collection'),
    Transition(label='Quality Testing'),
    Transition(label='Milk Blending'),
    Transition(label='Starter Culture'),
    Transition(label='Fermentation Check'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Separation'),
    Transition(label='Molding Press'),
    Transition(label='Salting Stage'),
    Transition(label='Aging Control'),
    Transition(label='Packaging Design'),
    Transition(label='Cold Shipping'),
    Transition(label='Compliance Audit'),
    Transition(label='Blockchain Log'),
    Transition(label='Market Pricing'),
    Transition(label='Order Fulfillment'),
    Transition(label='Feedback Review')
])

# Define the partial order
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

print(root)