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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop_panel = OperatorPOWL(operator=Operator.LOOP, children=[panel_review, forger_risk])
xor_approval = OperatorPOWL(operator=Operator.XOR, children=[approval_stage, skip])
xor_transport = OperatorPOWL(operator=Operator.XOR, children=[secure_packing, skip])
xor_certification = OperatorPOWL(operator=Operator.XOR, children=[certification, skip])

# Construct the root node with the defined activities and loops
root = StrictPartialOrder(
    nodes=[provenance_check, material_scan, style_compare, ai_imaging, chemical_test, aging_verify, record_match,
           database_query, panel_review, forger_risk, market_value, report_draft, approval_stage, secure_packing,
           transport_prep],
    order={
        (provenance_check, material_scan): 1,
        (material_scan, style_compare): 1,
        (style_compare, ai_imaging): 1,
        (ai_imaging, chemical_test): 1,
        (chemical_test, aging_verify): 1,
        (aging_verify, record_match): 1,
        (record_match, database_query): 1,
        (database_query, panel_review): 1,
        (panel_review, forger_risk): 1,
        (forger_risk, market_value): 1,
        (market_value, report_draft): 1,
        (report_draft, approval_stage): 1,
        (approval_stage, secure_packing): 1,
        (secure_packing, transport_prep): 1,
        (transport_prep, loop_panel): 1,
        (loop_panel, xor_approval): 1,
        (xor_approval, xor_certification): 1,
        (xor_certification, xor_transport): 1
    }
)

# Add edges to the root node
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
root.order.add_edge(report_draft, approval_stage)
root.order.add_edge(approval_stage, secure_packing)
root.order.add_edge(secure_packing, transport_prep)
root.order.add_edge(transport_prep, loop_panel)
root.order.add_edge(loop_panel, xor_approval)
root.order.add_edge(xor_approval, xor_certification)
root.order.add_edge(xor_certification, xor_transport)