import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
provenance = Transition(label='Provenance Check')
material = Transition(label='Material Testing')
expert = Transition(label='Expert Review')
legal = Transition(label='Legal Verify')
risk = Transition(label='Risk Assess')
insurance = Transition(label='Insurance Quote')
catalog = Transition(label='Catalog Entry')
digital = Transition(label='Digital Scan')
condition = Transition(label='Condition Report')
transport = Transition(label='Transport Plan')
customs = Transition(label='Customs Clear')
certification = Transition(label='Certification')
exhibit = Transition(label='Exhibit Setup')
notify = Transition(label='Owner Notify')
audit = Transition(label='Final Audit')

# Build the loop body for testing, expert review, and legal verify
body = StrictPartialOrder(nodes=[material, expert, legal])
# No edges => all three happen concurrently

# Build the loop: do body, then optionally do risk-assess and insurance-quote, then repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, StrictPartialOrder(nodes=[risk, insurance])])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    provenance,
    loop,
    catalog,
    digital,
    condition,
    transport,
    customs,
    certification,
    exhibit,
    notify,
    audit
])

# Define the control‐flow dependencies
root.order.add_edge(provenance, loop)
root.order.add_edge(loop, catalog)
root.order.add_edge(loop, digital)
root.order.add_edge(loop, condition)
root.order.add_edge(catalog, transport)
root.order.add_edge(digital, customs)
root.order.add_edge(condition, certification)
root.order.add_edge(transport, exhibit)
root.order.add_edge(customs, exhibit)
root.order.add_edge(exhibit, notify)
root.order.add_edge(exhibit, audit)