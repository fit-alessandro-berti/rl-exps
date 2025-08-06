import pm4py

# Define the transitions (activities)
A = pm4py.objects.powl.obj.Transition(label='Order Validate')
B = pm4py.objects.powl.obj.Transition(label='Route Optimize')
C = pm4py.objects.powl.obj.Transition(label='Drone Assign')
D = pm4py.objects.powl.obj.Transition(label='Preflight Check')
E = pm4py.objects.powl.obj.Transition(label='Load Package')
F = pm4py.objects.powl.obj.Transition(label='Flight Launch')
G = pm4py.objects.powl.obj.Transition(label='Traffic Monitor')
H = pm4py.objects.powl.obj.Transition(label='Weather Assess')
I = pm4py.objects.powl.obj.Transition(label='Obstacle Avoid')
J = pm4py.objects.powl.obj.Transition(label='Battery Check')
K = pm4py.objects.powl.obj.Transition(label='Delivery Verify')
L = pm4py.objects.powl.obj.Transition(label='Biometric Scan')
M = pm4py.objects.powl.obj.Transition(label='Package Release')
N = pm4py.objects.powl.obj.Transition(label='Return Flight')
O = pm4py.objects.powl.obj.Transition(label='Post Flight')
P = pm4py.objects.powl.obj.Transition(label='Data Analyze')
Q = pm4py.objects.powl.obj.Transition(label='Feedback Collect')
Skip = pm4py.objects.powl.obj.SilentTransition()

# Define the partial order
root = pm4py.objects.powl.obj.StrictPartialOrder()

# Add the transitions to the root
root.nodes.append(A)
root.nodes.append(B)
root.nodes.append(C)
root.nodes.append(D)
root.nodes.append(E)
root.nodes.append(F)
root.nodes.append(G)
root.nodes.append(H)
root.nodes.append(I)
root.nodes.append(J)
root.nodes.append(K)
root.nodes.append(L)
root.nodes.append(M)
root.nodes.append(N)
root.nodes.append(O)
root.nodes.append(P)
root.nodes.append(Q)

# Define the exclusive choices
root.nodes.append(Skip)

# Define the exclusive choice for A and B
xor_A_B = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[A, B])
root.nodes.append(xor_A_B)

# Define the exclusive choice for C and Skip
xor_C_Skip = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[C, Skip])
root.nodes.append(xor_C_Skip)

# Define the exclusive choice for D and E
xor_D_E = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[D, E])
root.nodes.append(xor_D_E)

# Define the exclusive choice for F and G
xor_F_G = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[F, G])
root.nodes.append(xor_F_G)

# Define the exclusive choice for H and I
xor_H_I = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[H, I])
root.nodes.append(xor_H_I)

# Define the exclusive choice for J and K
xor_J_K = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[J, K])
root.nodes.append(xor_J_K)

# Define the exclusive choice for L and M
xor_L_M = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[L, M])
root.nodes.append(xor_L_M)

# Define the exclusive choice for N and O
xor_N_O = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[N, O])
root.nodes.append(xor_N_O)

# Define the exclusive choice for P and Q
xor_P_Q = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[P, Q])
root.nodes.append(xor_P_Q)

# Define the loop for F and G
loop_F_G = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.LOOP, children=[F, G])
root.nodes.append(loop_F_G)

# Define the loop for H and I
loop_H_I = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.LOOP, children=[H, I])
root.nodes.append(loop_H_I)

# Define the loop for J and K
loop_J_K = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.LOOP, children=[J, K])
root.nodes.append(loop_J_K)

# Define the loop for L and M
loop_L_M = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.LOOP, children=[L, M])
root.nodes.append(loop_L_M)

# Define the loop for N and O
loop_N_O = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.LOOP, children=[N, O])
root.nodes.append(loop_N_O)

# Define the loop for P and Q
loop_P_Q = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.LOOP, children=[P, Q])
root.nodes.append(loop_P_Q)

# Add edges between nodes
root.order.add_edge(A, xor_A_B)
root.order.add_edge(B, xor_A_B)
root.order.add_edge(xor_A_B, xor_C_Skip)
root.order.add_edge(C, xor_C_Skip)
root.order.add_edge(Skip, xor_C_Skip)
root.order.add_edge(xor_C_Skip, xor_D_E)
root.order.add_edge(D, xor_D_E)
root.order.add_edge(E, xor_D_E)
root.order.add_edge(xor_D_E, xor_F_G)
root.order.add_edge(F, xor_F_G)
root.order.add_edge(G, xor_F_G)
root.order.add_edge(xor_F_G, xor_H_I)
root.order.add_edge(H, xor_H_I)
root.order.add_edge(I, xor_H_I)
root.order.add_edge(xor_H_I, xor_J_K)
root.order.add_edge(J, xor_J_K)
root.order.add_edge(K, xor_J_K)
root.order.add_edge(xor_J_K, xor_L_M)
root.order.add_edge(L, xor_L_M)
root.order.add_edge(M, xor_L_M)
root.order.add_edge(xor_L_M, xor_N_O)
root.order.add_edge(N, xor_N_O)
root.order.add_edge(O, xor_N_O)
root.order.add_edge(xor_N_O, xor_P_Q)
root.order.add_edge(P, xor_P_Q)
root.order.add_edge(Q, xor_P_Q)
root.order.add_edge(xor_P_Q, loop_F_G)
root.order.add_edge(loop_F_G, xor_P_Q)
root.order.add_edge(xor_P_Q, loop_H_I)
root.order.add_edge(loop_H_I, xor_P_Q)
root.order.add_edge(xor_P_Q, loop_J_K)
root.order.add_edge(loop_J_K, xor_P_Q)
root.order.add_edge(xor_P_Q, loop_L_M)
root.order.add_edge(loop_L_M, xor_P_Q)
root.order.add_edge(xor_P_Q, loop_N_O)
root.order.add_edge(loop_N_O, xor_P_Q)
root.order.add_edge(xor_P_Q, loop_P_Q)
root.order.add_edge(loop_P_Q, xor_P_Q)

# Print the root for verification
print(root)