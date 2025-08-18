import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define the POWL model
provenance_check_node = StrictPartialOrder(nodes=[provenance_check])
material_scan_node = StrictPartialOrder(nodes=[material_scan])
style_compare_node = StrictPartialOrder(nodes=[style_compare])
ai_imaging_node = StrictPartialOrder(nodes=[ai_imaging])
chemical_test_node = StrictPartialOrder(nodes=[chemical_test])
aging_verify_node = StrictPartialOrder(nodes=[aging_verify])
record_match_node = StrictPartialOrder(nodes=[record_match])
database_query_node = StrictPartialOrder(nodes=[database_query])
panel_review_node = StrictPartialOrder(nodes=[panel_review])
forger_risk_node = StrictPartialOrder(nodes=[forger_risk])
market_value_node = StrictPartialOrder(nodes=[market_value])
report_draft_node = StrictPartialOrder(nodes=[report_draft])
certification_node = StrictPartialOrder(nodes=[certification])
approval_stage_node = StrictPartialOrder(nodes=[approval_stage])
secure_packing_node = StrictPartialOrder(nodes=[secure_packing])
transport_prep_node = StrictPartialOrder(nodes=[transport_prep])

# Define the partial order
root = StrictPartialOrder(nodes=[
    provenance_check_node,
    material_scan_node,
    style_compare_node,
    ai_imaging_node,
    chemical_test_node,
    aging_verify_node,
    record_match_node,
    database_query_node,
    panel_review_node,
    forger_risk_node,
    market_value_node,
    report_draft_node,
    certification_node,
    approval_stage_node,
    secure_packing_node,
    transport_prep_node
])

# Define dependencies
root.order.add_edge(provenance_check_node, material_scan_node)
root.order.add_edge(material_scan_node, style_compare_node)
root.order.add_edge(style_compare_node, ai_imaging_node)
root.order.add_edge(ai_imaging_node, chemical_test_node)
root.order.add_edge(chemical_test_node, aging_verify_node)
root.order.add_edge(aging_verify_node, record_match_node)
root.order.add_edge(record_match_node, database_query_node)
root.order.add_edge(database_query_node, panel_review_node)
root.order.add_edge(panel_review_node, forger_risk_node)
root.order.add_edge(forger_risk_node, market_value_node)
root.order.add_edge(market_value_node, report_draft_node)
root.order.add_edge(report_draft_node, certification_node)
root.order.add_edge(certification_node, approval_stage_node)
root.order.add_edge(approval_stage_node, secure_packing_node)
root.order.add_edge(secure_packing_node, transport_prep_node)

print(root)