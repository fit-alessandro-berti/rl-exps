import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
design     = Transition(label='Drone Design')
reg_check  = Transition(label='Regulatory Check')
nav_sys    = Transition(label='Nav System')
partner    = Transition(label='Partner Setup')
operator   = Transition(label='Operator Training')
test       = Transition(label='Test Flights')
weather    = Transition(label='Weather Review')
optimize   = Transition(label='Route Optimize')
parts      = Transition(label='Parts Logistics')
feedback   = Transition(label='Feedback Loop')
risk       = Transition(label='Risk Assess')
emergency  = Transition(label='Emergency Plan')
compliance = Transition(label='Compliance Audit')
data_sync  = Transition(label='Data Sync')
launch     = Transition(label='Service Launch')

# Define the loop for iterative testing and review
# A = weather review then optimize then parts logistics then feedback then risk assess then emergency plan
A = StrictPartialOrder(nodes=[weather, optimize, parts, feedback, risk, emergency])
A.order.add_edge(weather, optimize)
A.order.add_edge(optimize, parts)
A.order.add_edge(parts, feedback)
A.order.add_edge(feedback, risk)
A.order.add_edge(risk, emergency)

# B = compliance audit
B = compliance

# LOOP(A, B): do A, then either exit or do B then A again
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Build the overall partial order
root = StrictPartialOrder(nodes=[design, reg_check, nav_sys, partner, operator, loop, launch])
root.order.add_edge(design, reg_check)
root.order.add_edge(reg_check, nav_sys)
root.order.add_edge(nav_sys, partner)
root.order.add_edge(partner, operator)
root.order.add_edge(operator, loop)
root.order.add_edge(loop, launch)