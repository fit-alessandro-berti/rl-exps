import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

artifact_intake = Transition(label='Artifact Intake')
visual_scan = Transition(label='Visual Scan')
material_test = Transition(label='Material Test')
radiocarbon_check = Transition(label='Radiocarbon Check')
provenance_search = Transition(label='Provenance Search')
archive_review = Transition(label='Archive Review')
expert_consult = Transition(label='Expert Consult')
microscope_exam = Transition(label='Microscope Exam')
infrared_scan = Transition(label='Infrared Scan')
legal_verify = Transition(label='Legal Verify')
condition_report = Transition(label='Condition Report')
digital_catalog = Transition(label='Digital Catalog')
ownership_audit = Transition(label='Ownership Audit')
restoration_plan = Transition(label='Restoration Plan')
final_approval = Transition(label='Final Approval')
authentication_cert = Transition(label='Authentication Cert')

skip = SilentTransition()

# Define the workflow
artifact_intake_to_visual_scan = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, visual_scan])
visual_scan_to_material_test = OperatorPOWL(operator=Operator.XOR, children=[visual_scan, material_test])
material_test_to_radiocarbon_check = OperatorPOWL(operator=Operator.XOR, children=[material_test, radiocarbon_check])
radiocarbon_check_to_provenance_search = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_check, provenance_search])
provenance_search_to_archive_review = OperatorPOWL(operator=Operator.XOR, children=[provenance_search, archive_review])
archive_review_to_expert_consult = OperatorPOWL(operator=Operator.XOR, children=[archive_review, expert_consult])
expert_consult_to_microscope_exam = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, microscope_exam])
microscope_exam_to_infrared_scan = OperatorPOWL(operator=Operator.XOR, children=[microscope_exam, infrared_scan])
infrared_scan_to_legal_verify = OperatorPOWL(operator=Operator.XOR, children=[infrared_scan, legal_verify])
legal_verify_to_condition_report = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, condition_report])
condition_report_to_digital_catalog = OperatorPOWL(operator=Operator.XOR, children=[condition_report, digital_catalog])
digital_catalog_to_ownership_audit = OperatorPOWL(operator=Operator.XOR, children=[digital_catalog, ownership_audit])
ownership_audit_to_restoration_plan = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, restoration_plan])
restoration_plan_to_final_approval = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, final_approval])
final_approval_to_authentication_cert = OperatorPOWL(operator=Operator.XOR, children=[final_approval, authentication_cert])

root = StrictPartialOrder(nodes=[
    artifact_intake_to_visual_scan,
    visual_scan_to_material_test,
    material_test_to_radiocarbon_check,
    radiocarbon_check_to_provenance_search,
    provenance_search_to_archive_review,
    archive_review_to_expert_consult,
    expert_consult_to_microscope_exam,
    microscope_exam_to_infrared_scan,
    infrared_scan_to_legal_verify,
    legal_verify_to_condition_report,
    condition_report_to_digital_catalog,
    digital_catalog_to_ownership_audit,
    ownership_audit_to_restoration_plan,
    restoration_plan_to_final_approval,
    final_approval_to_authentication_cert
])
root.order.add_edge(artifact_intake_to_visual_scan, visual_scan_to_material_test)
root.order.add_edge(visual_scan_to_material_test, material_test_to_radiocarbon_check)
root.order.add_edge(material_test_to_radiocarbon_check, radiocarbon_check_to_provenance_search)
root.order.add_edge(radiocarbon_check_to_provenance_search, provenance_search_to_archive_review)
root.order.add_edge(provenance_search_to_archive_review, archive_review_to_expert_consult)
root.order.add_edge(archive_review_to_expert_consult, expert_consult_to_microscope_exam)
root.order.add_edge(expert_consult_to_microscope_exam, microscope_exam_to_infrared_scan)
root.order.add_edge(microscope_exam_to_infrared_scan, infrared_scan_to_legal_verify)
root.order.add_edge(infrared_scan_to_legal_verify, legal_verify_to_condition_report)
root.order.add_edge(legal_verify_to_condition_report, condition_report_to_digital_catalog)
root.order.add_edge(condition_report_to_digital_catalog, digital_catalog_to_ownership_audit)
root.order.add_edge(digital_catalog_to_ownership_audit, ownership_audit_to_restoration_plan)
root.order.add_edge(ownership_audit_to_restoration_plan, restoration_plan_to_final_approval)
root.order.add_edge(restoration_plan_to_final_approval, final_approval_to_authentication_cert)