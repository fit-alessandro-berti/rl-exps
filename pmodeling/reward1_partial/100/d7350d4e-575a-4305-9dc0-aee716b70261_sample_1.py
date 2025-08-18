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

# Define silent transitions
skip = SilentTransition()

# Define the process steps as POWL models
provenance_check_step = OperatorPOWL(operator=Operator.SILENT, children=[provenance_check])
sample_collection_step = OperatorPOWL(operator=Operator.SILENT, children=[sample_collection])
spectroscopy_test_step = OperatorPOWL(operator=Operator.SILENT, children=[spectroscopy_test])
carbon_dating_step = OperatorPOWL(operator=Operator.SILENT, children=[carbon_dating])
expert_review_step = OperatorPOWL(operator=Operator.SILENT, children=[expert_review])
legal_clearance_step = OperatorPOWL(operator=Operator.SILENT, children=[legal_clearance])
cultural_assessment_step = OperatorPOWL(operator=Operator.SILENT, children=[cultural_assessment])
digital_scan_step = OperatorPOWL(operator=Operator.SILENT, children=[digital_scan])
report_draft_step = OperatorPOWL(operator=Operator.SILENT, children=[report_draft])
stakeholder_meet_step = OperatorPOWL(operator=Operator.SILENT, children=[stakeholder_meet])
acquisition_vote_step = OperatorPOWL(operator=Operator.SILENT, children=[acquisition_vote])
restoration_plan_step = OperatorPOWL(operator=Operator.SILENT, children=[restoration_plan])
condition_report_step = OperatorPOWL(operator=Operator.SILENT, children=[condition_report])
archival_entry_step = OperatorPOWL(operator=Operator.SILENT, children=[archival_entry])
final_approval_step = OperatorPOWL(operator=Operator.SILENT, children=[final_approval])

# Define the partial order for the process
root = StrictPartialOrder(nodes=[
    provenance_check_step,
    sample_collection_step,
    spectroscopy_test_step,
    carbon_dating_step,
    expert_review_step,
    legal_clearance_step,
    cultural_assessment_step,
    digital_scan_step,
    report_draft_step,
    stakeholder_meet_step,
    acquisition_vote_step,
    restoration_plan_step,
    condition_report_step,
    archival_entry_step,
    final_approval_step
])

# Define the dependencies between the nodes
root.order.add_edge(provenance_check_step, sample_collection_step)
root.order.add_edge(sample_collection_step, spectroscopy_test_step)
root.order.add_edge(sample_collection_step, carbon_dating_step)
root.order.add_edge(spectroscopy_test_step, expert_review_step)
root.order.add_edge(carbon_dating_step, expert_review_step)
root.order.add_edge(expert_review_step, legal_clearance_step)
root.order.add_edge(legal_clearance_step, cultural_assessment_step)
root.order.add_edge(cultural_assessment_step, digital_scan_step)
root.order.add_edge(digital_scan_step, report_draft_step)
root.order.add_edge(report_draft_step, stakeholder_meet_step)
root.order.add_edge(stakeholder_meet_step, acquisition_vote_step)
root.order.add_edge(acquisition_vote_step, restoration_plan_step)
root.order.add_edge(restoration_plan_step, condition_report_step)
root.order.add_edge(condition_report_step, archival_entry_step)
root.order.add_edge(archival_entry_step, final_approval_step)

print(root)