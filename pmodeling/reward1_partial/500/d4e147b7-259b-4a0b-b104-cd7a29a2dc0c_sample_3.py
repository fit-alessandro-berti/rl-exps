import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the workflow structure
loop_artifact_intake = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, visual_scan, material_test, radiocarbon_check, provenance_search, archive_review, expert_consult, microscope_exam, infrared_scan, legal_verify, condition_report, digital_catalog, ownership_audit, restoration_plan, final_approval])
xor_authentication_cert = OperatorPOWL(operator=Operator.XOR, children=[authentication_cert, skip])

# Construct the root Partial Order
root = StrictPartialOrder(nodes=[loop_artifact_intake, xor_authentication_cert])
root.order.add_edge(loop_artifact_intake, xor_authentication_cert)

print(root)