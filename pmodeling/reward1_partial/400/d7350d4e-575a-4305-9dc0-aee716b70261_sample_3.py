import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process structure
provenance_check_to_sample_collection = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, sample_collection])
sample_collection_to_spectroscopy_test = OperatorPOWL(operator=Operator.XOR, children=[sample_collection, spectroscopy_test])
spectroscopy_test_to_carbon_dating = OperatorPOWL(operator=Operator.XOR, children=[spectroscopy_test, carbon_dating])
carbon_dating_to_expert_review = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, expert_review])
expert_review_to_legal_clearance = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_clearance])
legal_clearance_to_cultural_assessment = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, cultural_assessment])
cultural_assessment_to_digital_scan = OperatorPOWL(operator=Operator.XOR, children=[cultural_assessment, digital_scan])
digital_scan_to_report_draft = OperatorPOWL(operator=Operator.XOR, children=[digital_scan, report_draft])
report_draft_to_stakeholder_meet = OperatorPOWL(operator=Operator.XOR, children=[report_draft, stakeholder_meet])
stakeholder_meet_to_acquisition_vote = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, acquisition_vote])
acquisition_vote_to_restoration_plan = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, restoration_plan])
restoration_plan_to_condition_report = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, condition_report])
condition_report_to_archival_entry = OperatorPOWL(operator=Operator.XOR, children=[condition_report, archival_entry])
archival_entry_to_final_approval = OperatorPOWL(operator=Operator.XOR, children=[archival_entry, final_approval])

# Define the partial order
root = StrictPartialOrder(nodes=[
    provenance_check_to_sample_collection,
    sample_collection_to_spectroscopy_test,
    spectroscopy_test_to_carbon_dating,
    carbon_dating_to_expert_review,
    expert_review_to_legal_clearance,
    legal_clearance_to_cultural_assessment,
    cultural_assessment_to_digital_scan,
    digital_scan_to_report_draft,
    report_draft_to_stakeholder_meet,
    stakeholder_meet_to_acquisition_vote,
    acquisition_vote_to_restoration_plan,
    restoration_plan_to_condition_report,
    condition_report_to_archival_entry,
    archival_entry_to_final_approval
])

# Add dependencies
root.order.add_edge(provenance_check_to_sample_collection, sample_collection_to_spectroscopy_test)
root.order.add_edge(sample_collection_to_spectroscopy_test, spectroscopy_test_to_carbon_dating)
root.order.add_edge(spectroscopy_test_to_carbon_dating, carbon_dating_to_expert_review)
root.order.add_edge(carbon_dating_to_expert_review, expert_review_to_legal_clearance)
root.order.add_edge(expert_review_to_legal_clearance, legal_clearance_to_cultural_assessment)
root.order.add_edge(legal_clearance_to_cultural_assessment, cultural_assessment_to_digital_scan)
root.order.add_edge(cultural_assessment_to_digital_scan, digital_scan_to_report_draft)
root.order.add_edge(digital_scan_to_report_draft, report_draft_to_stakeholder_meet)
root.order.add_edge(report_draft_to_stakeholder_meet, stakeholder_meet_to_acquisition_vote)
root.order.add_edge(stakeholder_meet_to_acquisition_vote, acquisition_vote_to_restoration_plan)
root.order.add_edge(acquisition_vote_to_restoration_plan, restoration_plan_to_condition_report)
root.order.add_edge(restoration_plan_to_condition_report, condition_report_to_archival_entry)
root.order.add_edge(condition_report_to_archival_entry, archival_entry_to_final_approval)

print(root)