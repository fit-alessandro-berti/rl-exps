import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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
partial_order = StrictPartialOrder(
    nodes=[provenance_check, material_scan, style_compare, ai_imaging, chemical_test, aging_verify,
           record_match, database_query, panel_review, forger_risk, market_value, report_draft, certification,
           approval_stage, secure_packing, transport_prep],
    order={})

# Define the partial order graph
partial_order.order.add_edge(provenance_check, material_scan)
partial_order.order.add_edge(material_scan, style_compare)
partial_order.order.add_edge(style_compare, ai_imaging)
partial_order.order.add_edge(ai_imaging, chemical_test)
partial_order.order.add_edge(chemical_test, aging_verify)
partial_order.order.add_edge(aging_verify, record_match)
partial_order.order.add_edge(record_match, database_query)
partial_order.order.add_edge(database_query, panel_review)
partial_order.order.add_edge(panel_review, forger_risk)
partial_order.order.add_edge(forger_risk, market_value)
partial_order.order.add_edge(market_value, report_draft)
partial_order.order.add_edge(report_draft, certification)
partial_order.order.add_edge(certification, approval_stage)
partial_order.order.add_edge(approval_stage, secure_packing)
partial_order.order.add_edge(secure_packing, transport_prep)

# Define the root of the POWL model
root = partial_order

# Return the root of the POWL model
return root