from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
A = Transition(label='Provenance Check')
B = Transition(label='Sample Collection')
C = Transition(label='Spectroscopy Test')
D = Transition(label='Carbon Dating')
E = Transition(label='Expert Review')
F = Transition(label='Legal Clearance')
G = Transition(label='Cultural Assessment')
H = Transition(label='Digital Scan')
I = Transition(label='Report Draft')
J = Transition(label='Stakeholder Meet')
K = Transition(label='Acquisition Vote')
L = Transition(label='Restoration Plan')
M = Transition(label='Condition Report')
N = Transition(label='Archival Entry')
O = Transition(label='Final Approval')
P = SilentTransition()  # For loop

# Construct the POWL model
root = StrictPartialOrder(
    nodes=[
        A,
        B,
        C,
        D,
        E,
        F,
        G,
        H,
        I,
        J,
        K,
        L,
        M,
        N,
        O,
        P
    ],
    order={
        A: {B, C, D, E, F, G, H, I, J, K, L, M, N, O, P},
        B: {P},
        C: {P},
        D: {P},
        E: {P},
        F: {P},
        G: {P},
        H: {P},
        I: {P},
        J: {P},
        K: {P},
        L: {P},
        M: {P},
        N: {P},
        O: {P},
        P: {O}
    }
)

print(root)