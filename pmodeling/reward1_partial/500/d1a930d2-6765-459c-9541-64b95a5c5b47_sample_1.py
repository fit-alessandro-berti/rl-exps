import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forger_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define parallel activities
document_review_and_forger_scan = OperatorPOWL(operator=Operator.OR, children=[document_review, forger_scan])
provenance_check_and_historical_research = OperatorPOWL(operator=Operator.OR, children=[provenance_check, historical_research])

# Define sequential activities
artifact_intake_to_condition_check = StrictPartialOrder(nodes=[artifact_intake, condition_check])
condition_check_to_material_test = StrictPartialOrder(nodes=[condition_check, material_test])
material_test_to_style_compare = StrictPartialOrder(nodes=[material_test, style_compare])
style_compare_to_carbon_dating = StrictPartialOrder(nodes=[style_compare, carbon_dating])
carbon_dating_to_document_review_and_forger_scan = StrictPartialOrder(nodes=[carbon_dating, document_review_and_forger_scan])
document_review_and_forger_scan_to_panel_review = StrictPartialOrder(nodes=[document_review_and_forger_scan, panel_review])
panel_review_to_report_draft = StrictPartialOrder(nodes=[panel_review, report_draft])
report_draft_to_final_approval = StrictPartialOrder(nodes=[report_draft, final_approval])
final_approval_to_catalog_entry = StrictPartialOrder(nodes=[final_approval, catalog_entry])

# Define partial order dependencies
root = StrictPartialOrder(nodes=[artifact_intake_to_condition_check, condition_check_to_material_test, material_test_to_style_compare, style_compare_to_carbon_dating, carbon_dating_to_document_review_and_forger_scan, document_review_and_forger_scan_to_panel_review, panel_review_to_report_draft, report_draft_to_final_approval, final_approval_to_catalog_entry])
root.order.add_edge(artifact_intake_to_condition_check, condition_check_to_material_test)
root.order.add_edge(condition_check_to_material_test, material_test_to_style_compare)
root.order.add_edge(material_test_to_style_compare, style_compare_to_carbon_dating)
root.order.add_edge(style_compare_to_carbon_dating, carbon_dating_to_document_review_and_forger_scan)
root.order.add_edge(carbon_dating_to_document_review_and_forger_scan, document_review_and_forger_scan_to_panel_review)
root.order.add_edge(document_review_and_forger_scan_to_panel_review, panel_review_to_report_draft)
root.order.add_edge(panel_review_to_report_draft, report_draft_to_final_approval)
root.order.add_edge(report_draft_to_final_approval, final_approval_to_catalog_entry)