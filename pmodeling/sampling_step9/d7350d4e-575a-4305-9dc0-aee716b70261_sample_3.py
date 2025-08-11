import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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
skip = SilentTransition()

# Define the process
provenance_check_next = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
sample_collection_next = OperatorPOWL(operator=Operator.XOR, children=[sample_collection, skip])
spectroscopy_test_next = OperatorPOWL(operator=Operator.XOR, children=[spectroscopy_test, skip])
carbon_dating_next = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, skip])
expert_review_next = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
legal_clearance_next = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, skip])
cultural_assessment_next = OperatorPOWL(operator=Operator.XOR, children=[cultural_assessment, skip])
digital_scan_next = OperatorPOWL(operator=Operator.XOR, children=[digital_scan, skip])
report_draft_next = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
stakeholder_meet_next = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, skip])
acquisition_vote_next = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, skip])
restoration_plan_next = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, skip])
condition_report_next = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
archival_entry_next = OperatorPOWL(operator=Operator.XOR, children=[archival_entry, skip])
final_approval_next = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Create the root node
root = StrictPartialOrder(nodes=[provenance_check_next, sample_collection_next, spectroscopy_test_next, carbon_dating_next, expert_review_next, legal_clearance_next, cultural_assessment_next, digital_scan_next, report_draft_next, stakeholder_meet_next, acquisition_vote_next, restoration_plan_next, condition_report_next, archival_entry_next, final_approval_next])

# Add dependencies
root.order.add_edge(provenance_check_next, sample_collection_next)
root.order.add_edge(sample_collection_next, spectroscopy_test_next)
root.order.add_edge(spectroscopy_test_next, carbon_dating_next)
root.order.add_edge(carbon_dating_next, expert_review_next)
root.order.add_edge(expert_review_next, legal_clearance_next)
root.order.add_edge(legal_clearance_next, cultural_assessment_next)
root.order.add_edge(cultural_assessment_next, digital_scan_next)
root.order.add_edge(digital_scan_next, report_draft_next)
root.order.add_edge(report_draft_next, stakeholder_meet_next)
root.order.add_edge(stakeholder_meet_next, acquisition_vote_next)
root.order.add_edge(acquisition_vote_next, restoration_plan_next)
root.order.add_edge(restoration_plan_next, condition_report_next)
root.order.add_edge(condition_report_next, archival_entry_next)
root.order.add_edge(archival_entry_next, final_approval_next)

# Print the root node
print(root)