from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    provenance_check, material_scan, style_compare, ai_imaging, chemical_test,
    aging_verify, record_match, database_query, panel_review, forger_risk,
    market_value, report_draft, certification, approval_stage, secure_packing,
    transport_prep
])

# Define the dependencies between activities
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, style_compare)
root.order.add_edge(style_compare, ai_imaging)
root.order.add_edge(ai_imaging, chemical_test)
root.order.add_edge(chemical_test, aging_verify)
root.order.add_edge(aging_verify, record_match)
root.order.add_edge(record_match, database_query)
root.order.add_edge(database_query, panel_review)
root.order.add_edge(panel_review, forger_risk)
root.order.add_edge(forger_risk, market_value)
root.order.add_edge(market_value, report_draft)
root.order.add_edge(report_draft, certification)
root.order.add_edge(certification, approval_stage)
root.order.add_edge(approval_stage, secure_packing)
root.order.add_edge(secure_packing, transport_prep)

print(root)