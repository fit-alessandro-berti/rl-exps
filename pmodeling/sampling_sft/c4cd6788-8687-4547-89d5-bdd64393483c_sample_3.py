import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
AR = Transition(label='Artifact Research')
OV = Transition(label='Ownership Verify')
SM = Transition(label='Stakeholder Meet')
LR = Transition(label='Legal Review')
DC = Transition(label='Diplomatic Contact')
CR = Transition(label='Condition Report')
TP = Transition(label='Transport Plan')
IS = Transition(label='Insurance Setup')
CC = Transition(label='Customs Clear')
SP = Transition(label='Secure Packaging')
SM2 = Transition(label='Shipping Monitor')
CB = Transition(label='Community Brief')
AI = Transition(label='Arrival Inspect')
EP = Transition(label='Exhibit Prepare')
PR = Transition(label='Public Release')

# Loop for repeated condition assessment and packaging
condition_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[CR, SP]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    AR, OV, SM, LR, DC,
    condition_loop, TP, IS, CC,
    SM2, CB, AI, EP, PR
])

# Define the control-flow dependencies
root.order.add_edge(AR, OV)
root.order.add_edge(OV, SM)
root.order.add_edge(SM, LR)
root.order.add_edge(LR, DC)
root.order.add_edge(DC, condition_loop)
root.order.add_edge(condition_loop, TP)
root.order.add_edge(TP, IS)
root.order.add_edge(IS, CC)
root.order.add_edge(CC, SM2)
root.order.add_edge(SM2, CB)
root.order.add_edge(CB, AI)
root.order.add_edge(AI, EP)
root.order.add_edge(EP, PR)