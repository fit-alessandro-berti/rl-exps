import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
radiocarbon_test = Transition(label='Radiocarbon Test')
stylistic_review = Transition(label='Stylistic Review')
expert_consult = Transition(label='Expert Consult')
document_audit = Transition(label='Document Audit')
legal_verify = Transition(label='Legal Verify')
condition_report = Transition(label='Condition Report')
discrepancy_flag = Transition(label='Discrepancy Flag')
re_examination = Transition(label='Re-examination')
alternative_source = Transition(label='Alternative Source')
acquisition_vote = Transition(label='Acquisition Vote')
catalog_entry = Transition(label='Catalog Entry')
exhibit_plan = Transition(label='Exhibit Plan')
final_approval = Transition(label='Final Approval')

skip = SilentTransition()

provenance_check_to_material_scan = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])
material_scan_to_radiocarbon_test = OperatorPOWL(operator=Operator.XOR, children=[material_scan, radiocarbon_test])
radiocarbon_test_to_stylistic_review = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, stylistic_review])
stylistic_review_to_expert_consult = OperatorPOWL(operator=Operator.XOR, children=[stylistic_review, expert_consult])
expert_consult_to_document_audit = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, document_audit])
document_audit_to_legal_verify = OperatorPOWL(operator=Operator.XOR, children=[document_audit, legal_verify])
legal_verify_to_condition_report = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, condition_report])
condition_report_to_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[condition_report, discrepancy_flag])
discrepancy_flag_to_re_examination = OperatorPOWL(operator=Operator.XOR, children=[discrepancy_flag, re_examination])
re_examination_to_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[re_examination, alternative_source])
alternative_source_to_acquisition_vote = OperatorPOWL(operator=Operator.XOR, children=[alternative_source, acquisition_vote])
acquisition_vote_to_catalog_entry = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, catalog_entry])
catalog_entry_to_exhibit_plan = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, exhibit_plan])
exhibit_plan_to_final_approval = OperatorPOWL(operator=Operator.XOR, children=[exhibit_plan, final_approval])

root = StrictPartialOrder(nodes=[
    provenance_check_to_material_scan,
    material_scan_to_radiocarbon_test,
    radiocarbon_test_to_stylistic_review,
    stylistic_review_to_expert_consult,
    expert_consult_to_document_audit,
    document_audit_to_legal_verify,
    legal_verify_to_condition_report,
    condition_report_to_discrepancy_flag,
    discrepancy_flag_to_re_examination,
    re_examination_to_alternative_source,
    alternative_source_to_acquisition_vote,
    acquisition_vote_to_catalog_entry,
    catalog_entry_to_exhibit_plan,
    exhibit_plan_to_final_approval
])

root.order.add_edge(provenance_check_to_material_scan, material_scan_to_radiocarbon_test)
root.order.add_edge(material_scan_to_radiocarbon_test, radiocarbon_test_to_stylistic_review)
root.order.add_edge(radiocarbon_test_to_stylistic_review, stylistic_review_to_expert_consult)
root.order.add_edge(stylistic_review_to_expert_consult, expert_consult_to_document_audit)
root.order.add_edge(expert_consult_to_document_audit, document_audit_to_legal_verify)
root.order.add_edge(document_audit_to_legal_verify, legal_verify_to_condition_report)
root.order.add_edge(legal_verify_to_condition_report, condition_report_to_discrepancy_flag)
root.order.add_edge(condition_report_to_discrepancy_flag, discrepancy_flag_to_re_examination)
root.order.add_edge(discrepancy_flag_to_re_examination, re_examination_to_alternative_source)
root.order.add_edge(re_examination_to_alternative_source, alternative_source_to_acquisition_vote)
root.order.add_edge(alternative_source_to_acquisition_vote, acquisition_vote_to_catalog_entry)
root.order.add_edge(acquisition_vote_to_catalog_entry, catalog_entry_to_exhibit_plan)
root.order.add_edge(catalog_entry_to_exhibit_plan, exhibit_plan_to_final_approval)