from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
wear_analysis = Transition(label='Wear Analysis')
image_capture = Transition(label='Image Capture')
pattern_match = Transition(label='Pattern Match')
ownership_verify = Transition(label='Ownership Verify')
ethics_review = Transition(label='Ethics Review')
carbon_dating = Transition(label='Carbon Dating')
restoration_eval = Transition(label='Restoration Eval')
report_draft = Transition(label='Report Draft')
stakeholder_review = Transition(label='Stakeholder Review')
archive_data = Transition(label='Archive Data')
exhibit_approve = Transition(label='Exhibit Approve')
condition_monitor = Transition(label='Condition Monitor')
final_certification = Transition(label='Final Certification')

# Create the POWL model
root = StrictPartialOrder(
    nodes=[
        provenance_check,
        material_scan,
        wear_analysis,
        image_capture,
        pattern_match,
        ownership_verify,
        ethics_review,
        carbon_dating,
        restoration_eval,
        report_draft,
        stakeholder_review,
        archive_data,
        exhibit_approve,
        condition_monitor,
        final_certification
    ],
    order=[
        (provenance_check, material_scan),
        (material_scan, wear_analysis),
        (wear_analysis, image_capture),
        (image_capture, pattern_match),
        (pattern_match, ownership_verify),
        (ownership_verify, ethics_review),
        (ethics_review, carbon_dating),
        (carbon_dating, restoration_eval),
        (restoration_eval, report_draft),
        (report_draft, stakeholder_review),
        (stakeholder_review, archive_data),
        (archive_data, exhibit_approve),
        (exhibit_approve, condition_monitor),
        (condition_monitor, final_certification)
    ]
)

# Print the POWL model
print(root)