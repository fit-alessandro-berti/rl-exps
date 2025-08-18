from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
A = Transition(label='Milk Collection')
B = Transition(label='Quality Testing')
C = Transition(label='Milk Blending')
D = Transition(label='Starter Culture')
E = Transition(label='Fermentation Check')
F = Transition(label='Curd Cutting')
G = Transition(label='Whey Separation')
H = Transition(label='Molding Press')
I = Transition(label='Salting Stage')
J = Transition(label='Aging Control')
K = Transition(label='Packaging Design')
L = Transition(label='Cold Shipping')
M = Transition(label='Compliance Audit')
N = Transition(label='Blockchain Log')
O = Transition(label='Market Pricing')
P = Transition(label='Order Fulfillment')
Q = Transition(label='Feedback Review')

# Define the partial order
root = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q])

# Define the dependencies
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
root.order.add_edge(O, P)
root.order.add_edge(P, Q)

print(root)