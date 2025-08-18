import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

artifact_intake_to_condition_check = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, condition_check])
condition_check_to_material_test = OperatorPOWL(operator=Operator.LOOP, children=[condition_check, material_test])
material_test_to_style_compare = OperatorPOWL(operator=Operator.LOOP, children=[material_test, style_compare])
style_compare_to_carbon_dating = OperatorPOWL(operator=Operator.LOOP, children=[style_compare, carbon_dating])
carbon_dating_to_document_review = OperatorPOWL(operator=Operator.LOOP, children=[carbon_dating, document_review])
document_review_to_provenance_check = OperatorPOWL(operator=Operator.LOOP, children=[document_review, provenance_check])
provenance_check_to_digital_imaging = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, digital_imaging])
digital_imaging_to_forger_scan = OperatorPOWL(operator=Operator.LOOP, children=[digital_imaging, forger_scan])
forger_scan_to_expert_consult = OperatorPOWL(operator=Operator.LOOP, children=[forger_scan, expert_consult])
expert_consult_to_historical_research = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, historical_research])
historical_research_to_panel_review = OperatorPOWL(operator=Operator.LOOP, children=[historical_research, panel_review])
panel_review_to_report_draft = OperatorPOWL(operator=Operator.LOOP, children=[panel_review, report_draft])
report_draft_to_final_approval = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, final_approval])
final_approval_to_catalog_entry = OperatorPOWL(operator=Operator.LOOP, children=[final_approval, catalog_entry])

root = StrictPartialOrder(nodes=[
    artifact_intake_to_condition_check,
    condition_check_to_material_test,
    material_test_to_style_compare,
    style_compare_to_carbon_dating,
    carbon_dating_to_document_review,
    document_review_to_provenance_check,
    provenance_check_to_digital_imaging,
    digital_imaging_to_forger_scan,
    forger_scan_to_expert_consult,
    expert_consult_to_historical_research,
    historical_research_to_panel_review,
    panel_review_to_report_draft,
    report_draft_to_final_approval,
    final_approval_to_catalog_entry
])

root.order.add_edge(artifact_intake_to_condition_check, condition_check_to_material_test)
root.order.add_edge(condition_check_to_material_test, material_test_to_style_compare)
root.order.add_edge(material_test_to_style_compare, style_compare_to_carbon_dating)
root.order.add_edge(style_compare_to_carbon_dating, carbon_dating_to_document_review)
root.order.add_edge(carbon_dating_to_document_review, document_review_to_provenance_check)
root.order.add_edge(document_review_to_provenance_check, provenance_check_to_digital_imaging)
root.order.add_edge(provenance_check_to_digital_imaging, digital_imaging_to_forger_scan)
root.order.add_edge(digital_imaging_to_forger_scan, forger_scan_to_expert_consult)
root.order.add_edge(forger_scan_to_expert_consult, expert_consult_to_historical_research)
root.order.add_edge(expert_consult_to_historical_research, historical_research_to_panel_review)
root.order.add_edge(historical_research_to_panel_review, panel_review_to_report_draft)
root.order.add_edge(panel_review_to_report_draft, report_draft_to_final_approval)
root.order.add_edge(report_draft_to_final_approval, final_approval_to_catalog_entry)