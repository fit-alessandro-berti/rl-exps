import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
style_compare = Transition(label='Style Compare')
ai_imaging = Transition(label='AI Imaging')
chemical_test = Transition(label='Chemical Test')
aging_verify = Transition(label='Aging Verify')
record_match = Transition(label='Record Match')
database_query = Transition(label='Database Query')
panel_review = Transition(label='Panel Review')
forger_risk = Transition(label='Forgery Risk')
market_value = Transition(label='Market Value')
report_draft = Transition(label='Report Draft')
certification = Transition(label='Certification')
approval_stage = Transition(label='Approval Stage')
secure_packing = Transition(label='Secure Packing')
transport_prep = Transition(label='Transport Prep')

# Define the root node as a strict partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    material_scan,
    style_compare,
    ai_imaging,
    chemical_test,
    aging_verify,
    record_match,
    database_query,
    panel_review,
    forger_risk,
    market_value,
    report_draft,
    certification,
    approval_stage,
    secure_packing,
    transport_prep
])

# Define the dependencies (order) between activities
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(provenance_check, style_compare)
root.order.add_edge(provenance_check, ai_imaging)
root.order.add_edge(provenance_check, chemical_test)
root.order.add_edge(provenance_check, aging_verify)
root.order.add_edge(provenance_check, record_match)
root.order.add_edge(provenance_check, database_query)
root.order.add_edge(provenance_check, panel_review)
root.order.add_edge(provenance_check, forger_risk)
root.order.add_edge(provenance_check, market_value)
root.order.add_edge(provenance_check, report_draft)
root.order.add_edge(provenance_check, certification)
root.order.add_edge(provenance_check, approval_stage)
root.order.add_edge(provenance_check, secure_packing)
root.order.add_edge(provenance_check, transport_prep)

# Now 'root' contains the POWL model for the authentication process