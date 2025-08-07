import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
provenance_check = Transition(label='Provenance Check')
sample_collection = Transition(label='Sample Collection')
spectroscopy_test = Transition(label='Spectroscopy Test')
carbon_dating = Transition(label='Carbon Dating')
expert_review = Transition(label='Expert Review')
legal_clearance = Transition(label='Legal Clearance')
cultural_assessment = Transition(label='Cultural Assessment')
digital_scan = Transition(label='Digital Scan')
report_draft = Transition(label='Report Draft')
stakeholder_meet = Transition(label='Stakeholder Meet')
acquisition_vote = Transition(label='Acquisition Vote')
restoration_plan = Transition(label='Restoration Plan')
condition_report = Transition(label='Condition Report')
archival_entry = Transition(label='Archival Entry')
final_approval = Transition(label='Final Approval')

# Define the root node as a strict partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    sample_collection,
    spectroscopy_test,
    carbon_dating,
    expert_review,
    legal_clearance,
    cultural_assessment,
    digital_scan,
    report_draft,
    stakeholder_meet,
    acquisition_vote,
    restoration_plan,
    condition_report,
    archival_entry,
    final_approval
])
# There are no dependencies in this process, so no edges are added

# Print the root node to confirm it's the final result
print(root)