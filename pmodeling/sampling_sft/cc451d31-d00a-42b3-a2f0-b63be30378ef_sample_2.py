import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
isoli = Transition(label='Idea Solicitation')
afilt = Transition(label='AI Filtering')
cvote = Transition(label='Community Voting')
erev = Transition(label='Expert Review')
pbuild = Transition(label='Prototype Build')
utest = Transition(label='User Testing')
ifeed = Transition(label='Iterate Feedback')
risk = Transition(label='Risk Assess')
comp = Transition(label='Compliance Check')
plaunch = Transition(label='Pilot Launch')
ptrack = Transition(label='Performance Track')
iimpact = Transition(label='Impact Analyze')
igath = Transition(label='Insight Gather')
cadj = Transition(label='Cycle Adjust')
frep = Transition(label='Final Report')

# Build the prototyping & testing loop: iterate Feedback, then either exit or repeat Risk-Assess->Compliance-Check->Prototype-Build->User-Testing->Iterate Feedback
loop_prot = OperatorPOWL(operator=Operator.LOOP, children=[risk, comp, pbuild, utest, ifeed])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    isoli, afilt, cvote, erev, pbuild, loop_prot, ptrack, iimpact, igath, cadj, frep
])

# Define the control-flow dependencies
root.order.add_edge(isoli, afilt)
root.order.add_edge(afilt, cvote)
root.order.add_edge(afilt, erev)
root.order.add_edge(cvote, pbuild)
root.order.add_edge(erev, pbuild)
root.order.add_edge(pbuild, loop_prot)
root.order.add_edge(loop_prot, ptrack)
root.order.add_edge(utest, ptrack)
root.order.add_edge(ptrack, iimpact)
root.order.add_edge(iimpact, igath)
root.order.add_edge(igath, cadj)
root.order.add_edge(cadj, frep)

# Final edges to exit the loop
root.order.add_edge(afilt, frep)
root.order.add_edge(cvote, frep)
root.order.add_edge(erev, frep)

print(root)