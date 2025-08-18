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

# Define silent transition (tau)
skip = SilentTransition()

# Define partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    visual_scan,
    material_test,
    radiocarbon_check,
    provenance_search,
    archive_review,
    expert_consult,
    microscope_exam,
    infrared_scan,
    legal_verify,
    condition_report,
    digital_catalog,
    ownership_audit,
    restoration_plan,
    final_approval,
    authentication_cert
])

# Define dependencies between activities
root.order.add_edge(artifact_intake, visual_scan)
root.order.add_edge(visual_scan, material_test)
root.order.add_edge(material_test, radiocarbon_check)
root.order.add_edge(radiocarbon_check, provenance_search)
root.order.add_edge(provenance_search, archive_review)
root.order.add_edge(archive_review, expert_consult)
root.order.add_edge(expert_consult, microscope_exam)
root.order.add_edge(microscope_exam, infrared_scan)
root.order.add_edge(infrared_scan, legal_verify)
root.order.add_edge(legal_verify, condition_report)
root.order.add_edge(condition_report, digital_catalog)
root.order.add_edge(digital_catalog, ownership_audit)
root.order.add_edge(ownership_audit, restoration_plan)
root.order.add_edge(restoration_plan, final_approval)
root.order.add_edge(final_approval, authentication_cert)

print(root)