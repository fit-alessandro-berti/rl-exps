import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent activities
skip = SilentTransition()

# Define the workflow steps
visual_scan_then_test = OperatorPOWL(operator=Operator.XOR, children=[visual_scan, material_test])
test_then_radiocarbon = OperatorPOWL(operator=Operator.XOR, children=[material_test, radiocarbon_check])
radiocarbon_then_archive = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_check, archive_review])
archive_then_expert = OperatorPOWL(operator=Operator.XOR, children=[archive_review, expert_consult])
expert_then_microscope = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, microscope_exam])
microscope_then_infrared = OperatorPOWL(operator=Operator.XOR, children=[microscope_exam, infrared_scan])
infrared_then_legal = OperatorPOWL(operator=Operator.XOR, children=[infrared_scan, legal_verify])
legal_then_condition = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, condition_report])
condition_then_catalog = OperatorPOWL(operator=Operator.XOR, children=[condition_report, digital_catalog])
catalog_then_audit = OperatorPOWL(operator=Operator.XOR, children=[digital_catalog, ownership_audit])
audit_then_plan = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, restoration_plan])
plan_then_approval = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, final_approval])

# Define the workflow
root = StrictPartialOrder(nodes=[artifact_intake, visual_scan_then_test, test_then_radiocarbon, radiocarbon_then_archive, archive_then_expert, expert_then_microscope, microscope_then_infrared, infrared_then_legal, legal_then_condition, condition_then_catalog, catalog_then_audit, audit_then_plan, plan_then_approval, authentication_cert])
root.order.add_edge(artifact_intake, visual_scan_then_test)
root.order.add_edge(visual_scan_then_test, test_then_radiocarbon)
root.order.add_edge(test_then_radiocarbon, radiocarbon_then_archive)
root.order.add_edge(radiocarbon_then_archive, archive_then_expert)
root.order.add_edge(archive_then_expert, expert_then_microscope)
root.order.add_edge(expert_then_microscope, microscope_then_infrared)
root.order.add_edge(microscope_then_infrared, infrared_then_legal)
root.order.add_edge(infrared_then_legal, legal_then_condition)
root.order.add_edge(legal_then_condition, condition_then_catalog)
root.order.add_edge(condition_then_catalog, catalog_then_audit)
root.order.add_edge(catalog_then_audit, audit_then_plan)
root.order.add_edge(audit_then_plan, plan_then_approval)
root.order.add_edge(plan_then_approval, authentication_cert)