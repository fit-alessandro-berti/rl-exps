import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ci = Transition(label='Client Intake')
na = Transition(label='Needs Analysis')
dm = Transition(label='Developer Match')
ev = Transition(label='Expert Vetting')
pb = Transition(label='Prototype Build')
fl = Transition(label='Feedback Loop')
mr = Transition(label='Model Refinement')
ld = Transition(label='License Draft')
inpn = Transition(label='IP Negotiation')
cs = Transition(label='Contract Sign')
dp = Transition(label='Deployment Prep')
gl = Transition(label='Go Live')
mm = Transition(label='Monitor Model')
oa = Transition(label='Optimize AI')
sh = Transition(label='Support Handoff')
cc = Transition(label='Compliance Check')
fr = Transition(label='Final Review')

# Build the refinement loop: Feedback Loop -> Model Refinement
refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[fl, mr])

# Build the licensing and deployment sequence: License Draft -> IP Negotiation -> Contract Sign -> Deployment Prep -> Go Live
licensing = StrictPartialOrder(nodes=[ld, inpn, cs, dp, gl])
licensing.order.add_edge(ld, inpn)
licensing.order.add_edge(inpn, cs)
licensing.order.add_edge(cs, dp)
licensing.order.add_edge(dp, gl)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    ci, na, dm, ev, pb, refinement_loop, licensing, mm, oa, sh, cc, fr
])

# Define the control‐flow dependencies
root.order.add_edge(ci, na)
root.order.add_edge(na, dm)
root.order.add_edge(dm, ev)
root.order.add_edge(ev, pb)
root.order.add_edge(pb, refinement_loop)
root.order.add_edge(refinement_loop, licensing)
root.order.add_edge(licensing, mm)
root.order.add_edge(mm, oa)
root.order.add_edge(oa, sh)
root.order.add_edge(sh, cc)
root.order.add_edge(cc, fr)

print(root)