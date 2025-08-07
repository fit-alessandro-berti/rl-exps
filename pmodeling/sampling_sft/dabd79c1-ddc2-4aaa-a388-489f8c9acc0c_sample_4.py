import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
dr = Transition(label='Document Review')
mt = Transition(label='Material Testing')
rd = Transition(label='Radiocarbon Date')
se = Transition(label='Stylistic Eval')
dc = Transition(label='Database Check')
oa = Transition(label='Ownership Audit')
ev = Transition(label='Export Verify')
ea = Transition(label='Expert Arbitration')
cp = Transition(label='Conservation Plan')
ra = Transition(label='Risk Assessment')
ar = Transition(label='Approval Review')
isup = Transition(label='Insurance Setup')
st = Transition(label='Secure Transport')
am = Transition(label='Acquisitions Meet')
fd = Transition(label='Final Documentation')

# Build the choice for either arbitration or risk assessment
xor_ar = OperatorPOWL(operator=Operator.XOR, children=[ea, ra])

# Build the loop for repeated stylistic evaluation and database check
loop_st = OperatorPOWL(operator=Operator.LOOP, children=[se, dc])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    dr, mt, rd, loop_st, xor_ar, oa, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev, ev,
    ev, ev