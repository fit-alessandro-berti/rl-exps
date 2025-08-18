import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
A = Transition(label='Material Sourcing')
B = Transition(label='Supplier Vetting')
C = Transition(label='Design Review')
D = Transition(label='Prototype Build')
E = Transition(label='Quality Audit')
F = Transition(label='Batch Scheduling')
G = Transition(label='Handcrafting')
H = Transition(label='Packaging Design')
I = Transition(label='Custom Labeling')
J = Transition(label='Sustainability Check')
K = Transition(label='Inventory Sync')
L = Transition(label='Market Analysis')
M = Transition(label='Order Aggregation')
N = Transition(label='Distribution Plan')
O = Transition(label='Customer Feedback')

# Define the partial order
root = StrictPartialOrder(nodes=[
    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O
])

# Define the order relationships
root.order.add_edge(A, B)
root.order.add_edge(B, C)
root.order.add_edge(C, D)
root.order.add_edge(D, E)
root.order.add_edge(E, F)
root.order.add_edge(F, G)
root.order.add_edge(G, H)
root.order.add_edge(H, I)
root.order.add_edge(I, J)
root.order.add_edge(J, K)
root.order.add_edge(K, L)
root.order.add_edge(L, M)
root.order.add_edge(M, N)
root.order.add_edge(N, O)

# Print the root model
print(root)