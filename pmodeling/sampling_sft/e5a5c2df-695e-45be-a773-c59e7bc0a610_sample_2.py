import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
at = Transition(label='Alert Trigger')
ia = Transition(label='Initial Assess')
sn = Transition(label='Stakeholder Notify')
rc = Transition(label='Resource Check')
ra = Transition(label='Risk Analyze')
cs = Transition(label='Command Setup')
dt = Transition(label='Deploy Teams')
dc = Transition(label='Data Collect')
su = Transition(label='Supply Dispatch')
me = Transition(label='Media Brief')
eu = Transition(label='External Liaison')
suu = Transition(label='Situation Update')
pa = Transition(label='Priority Adjust')
ir = Transition(label='Impact Review')
rp = Transition(label='Recovery Plan')
pa2 = Transition(label='Process Audit')

# Loop for continuous monitoring and decision-making
loop_body = StrictPartialOrder(nodes=[dc, eu, pa, ir, rp])
loop_body.order.add_edge(dc, eu)
loop_body.order.add_edge(eu, pa)
loop_body.order.add_edge(pa, ir)
loop_body.order.add_edge(ir, rp)

# Loop: Situation Update -> Priority Adjust -> Impact Review -> Recovery Plan -> Process Audit
loop = OperatorPOWL(operator=Operator.LOOP, children=[suu, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[at, ia, sn, rc, ra, cs, dt, loop, su, me, pa2])
root.order.add_edge(at, ia)
root.order.add_edge(ia, sn)
root.order.add_edge(ia, rc)
root.order.add_edge(ia, ra)
root.order.add_edge(sn, cs)
root.order.add_edge(rc, dt)
root.order.add_edge(ra, dt)
root.order.add_edge(cs, dt)
root.order.add_edge(dt, su)
root.order.add_edge(dt, me)
root.order.add_edge(dt, loop)
root.order.add_edge(su, pa2)
root.order.add_edge(me, pa2)