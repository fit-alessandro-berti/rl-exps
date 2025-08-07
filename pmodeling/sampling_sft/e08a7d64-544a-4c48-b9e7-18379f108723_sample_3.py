import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
provenance_check    = Transition(label='Provenance Check')
material_testing    = Transition(label='Material Testing')
expert_review       = Transition(label='Expert Review')
legal_verify        = Transition(label='Legal Verify')
risk_assess         = Transition(label='Risk Assess')
insurance_quote     = Transition(label='Insurance Quote')
catalog_entry       = Transition(label='Catalog Entry')
digital_scan        = Transition(label='Digital Scan')
condition_report    = Transition(label='Condition Report')
transport_plan      = Transition(label='Transport Plan')
customs_clear       = Transition(label='Customs Clear')
certification       = Transition(label='Certification')
exhibit_setup       = Transition(label='Exhibit Setup')
owner_notify        = Transition(label='Owner Notify')
final_audit         = Transition(label='Final Audit')

# Build the loop body (testing, review, verification, risk, insurance, catalog, digital, condition)
loop_body = StrictPartialOrder(nodes=[
    material_testing,
    expert_review,
    legal_verify,
    risk_assess,
    insurance_quote,
    catalog_entry,
    digital_scan,
    condition_report
])
# no edges => all tasks concurrent

# Loop operator: do testing, then choose to exit or do the whole body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, loop_body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    loop,
    transport_plan,
    customs_clear,
    certification,
    exhibit_setup,
    owner_notify,
    final_audit
])
# Initial provenance check is the start
root.order.add_edge(provenance_check, loop)
# After the loop, do transport, customs, certification, setup, notify, final audit in sequence
root.order.add_edge(loop, transport_plan)
root.order.add_edge(transport_plan, customs_clear)
root.order.add_edge(customs_clear, certification)
root.order.add_edge(certification, exhibit_setup)
root.order.add_edge(exhibit_setup, owner_notify)
root.order.add_edge(owner_notify, final_audit)