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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define loop for material test and microscope exam
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, microscope_exam])

# Define exclusive choice for expert consult and infrared scan
xor = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, infrared_scan])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[artifact_intake, visual_scan, loop, xor, radiocarbon_check, provenance_search, archive_review, legal_verify, condition_report, digital_catalog, ownership_audit, restoration_plan, final_approval, authentication_cert])

# Define the dependencies between nodes
root.order.add_edge(artifact_intake, visual_scan)
root.order.add_edge(visual_scan, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, radiocarbon_check)
root.order.add_edge(radiocarbon_check, provenance_search)
root.order.add_edge(provenance_search, archive_review)
root.order.add_edge(archive_review, legal_verify)
root.order.add_edge(legal_verify, condition_report)
root.order.add_edge(condition_report, digital_catalog)
root.order.add_edge(digital_catalog, ownership_audit)
root.order.add_edge(ownership_audit, restoration_plan)
root.order.add_edge(restoration_plan, final_approval)
root.order.add_edge(final_approval, authentication_cert)