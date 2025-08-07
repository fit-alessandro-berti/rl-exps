from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the process
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

# Define the partial order
root = StrictPartialOrder(nodes=[
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
])

# Since there are no explicit dependencies mentioned, we assume all activities are concurrent
# and connect them accordingly. However, in a real-world scenario, dependencies would be
# specified and added to the 'root.order' set.

print(root)