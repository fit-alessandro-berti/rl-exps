import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        provenance_check, sample_collection, spectroscopy_test, carbon_dating, expert_review, legal_clearance,
        cultural_assessment, digital_scan, report_draft, stakeholder_meet, acquisition_vote, restoration_plan,
        condition_report, archival_entry, final_approval
    ],
    order=[
        # Provenance Check -> Sample Collection
        (provenance_check, sample_collection),
        # Sample Collection -> Spectroscopy Test
        (sample_collection, spectroscopy_test),
        # Sample Collection -> Carbon Dating
        (sample_collection, carbon_dating),
        # Spectroscopy Test -> Expert Review
        (spectroscopy_test, expert_review),
        # Carbon Dating -> Expert Review
        (carbon_dating, expert_review),
        # Expert Review -> Legal Clearance
        (expert_review, legal_clearance),
        # Legal Clearance -> Cultural Assessment
        (legal_clearance, cultural_assessment),
        # Cultural Assessment -> Digital Scan
        (cultural_assessment, digital_scan),
        # Digital Scan -> Report Draft
        (digital_scan, report_draft),
        # Report Draft -> Stakeholder Meet
        (report_draft, stakeholder_meet),
        # Stakeholder Meet -> Acquisition Vote
        (stakeholder_meet, acquisition_vote),
        # Acquisition Vote -> Restoration Plan
        (acquisition_vote, restoration_plan),
        # Restoration Plan -> Condition Report
        (restoration_plan, condition_report),
        # Condition Report -> Archival Entry
        (condition_report, archival_entry),
        # Archival Entry -> Final Approval
        (archival_entry, final_approval)
    ]
)

print(root)