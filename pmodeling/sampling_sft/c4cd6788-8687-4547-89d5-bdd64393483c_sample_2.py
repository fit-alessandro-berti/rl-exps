import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
SMON = Transition(label='Shipping Monitor')
CB = Transition(label='Community Brief')
AI = Transition(label='Arrival Inspect')
EP = Transition(label='Exhibit Prepare')
PR = Transition(label='Public Release')

# Loop for continuous monitoring after shipping
loop_monitor = OperatorPOWL(
    operator=Operator.LOOP,
    children=[SMON, SilentTransition()]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    AR, OV, SM, LR, DC,
    CR, TP, IS, CC, SP,
    loop_monitor,
    CB, AI,
    EP, PR
])

# Define the control-flow dependencies
root.order.add_edge(AR, OV)
root.order.add_edge(OV, SM)
root.order.add_edge(SM, LR)
root.order.add_edge(LR, DC)
root.order.add_edge(DC, CR)
root.order.add_edge(CR, TP)
root.order.add_edge(TP, IS)
root.order.add_edge(IS, CC)
root.order.add_edge(CC, SP)
root.order.add_edge(SP, loop_monitor)
root.order.add_edge(loop_monitor, CB)
root.order.add_edge(loop_monitor, AI)
root.order.add_edge(CB, EP)
root.order.add_edge(AI, EP)
root.order.add_edge(EP, PR)