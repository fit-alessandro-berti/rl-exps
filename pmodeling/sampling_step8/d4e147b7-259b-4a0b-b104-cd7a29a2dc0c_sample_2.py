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

# Define silent transitions (if any, as per the process description)
skip = SilentTransition()

# Define the workflow structure
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (artifact_intake, visual_scan),
        (visual_scan, material_test),
        (material_test, radiocarbon_check),
        (radiocarbon_check, provenance_search),
        (provenance_search, archive_review),
        (archive_review, expert_consult),
        (expert_consult, microscope_exam),
        (microscope_exam, infrared_scan),
        (infrared_scan, legal_verify),
        (legal_verify, condition_report),
        (condition_report, digital_catalog),
        (digital_catalog, ownership_audit),
        (ownership_audit, restoration_plan),
        (restoration_plan, final_approval),
        (final_approval, authentication_cert)
    ]
)

# Note: The 'root' variable now contains the defined POWL model for the described process.