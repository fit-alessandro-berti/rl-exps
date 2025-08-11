import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the POWL model
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
condition_report_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, visual_scan, material_test, radiocarbon_check, provenance_search, archive_review, expert_consult, microscope_exam, infrared_scan, legal_verify])
final_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, digital_catalog, ownership_audit, restoration_plan])

# Define exclusive choice nodes
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[final_approval, authentication_cert])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[condition_report_loop, final_approval_loop, exclusive_choice])
root.order.add_edge(condition_report_loop, final_approval_loop)
root.order.add_edge(final_approval_loop, exclusive_choice)

# Save the final result in the variable 'root'