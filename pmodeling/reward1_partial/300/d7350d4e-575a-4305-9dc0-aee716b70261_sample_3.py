from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the process tree
provenance_tree = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
sample_tree = OperatorPOWL(operator=Operator.XOR, children=[sample_collection, skip])
spectroscopy_tree = OperatorPOWL(operator=Operator.XOR, children=[spectroscopy_test, skip])
carbon_dating_tree = OperatorPOWL(operator=Operator.XOR, children=[carbon_dating, skip])
expert_tree = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
legal_tree = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, skip])
cultural_tree = OperatorPOWL(operator=Operator.XOR, children=[cultural_assessment, skip])
digital_tree = OperatorPOWL(operator=Operator.XOR, children=[digital_scan, skip])
report_tree = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
stakeholder_tree = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, skip])
acquisition_tree = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, skip])
restoration_tree = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, skip])
condition_tree = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
archival_tree = OperatorPOWL(operator=Operator.XOR, children=[archival_entry, skip])
final_approval_tree = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Define the root node
root = StrictPartialOrder(nodes=[
    provenance_tree,
    sample_tree,
    spectroscopy_tree,
    carbon_dating_tree,
    expert_tree,
    legal_tree,
    cultural_tree,
    digital_tree,
    report_tree,
    stakeholder_tree,
    acquisition_tree,
    restoration_tree,
    condition_tree,
    archival_tree,
    final_approval_tree
])

# Define the order
root.order.add_edge(provenance_tree, sample_tree)
root.order.add_edge(sample_tree, spectroscopy_tree)
root.order.add_edge(spectroscopy_tree, carbon_dating_tree)
root.order.add_edge(carbon_dating_tree, expert_tree)
root.order.add_edge(expert_tree, legal_tree)
root.order.add_edge(legal_tree, cultural_tree)
root.order.add_edge(cultural_tree, digital_tree)
root.order.add_edge(digital_tree, report_tree)
root.order.add_edge(report_tree, stakeholder_tree)
root.order.add_edge(stakeholder_tree, acquisition_tree)
root.order.add_edge(acquisition_tree, restoration_tree)
root.order.add_edge(restoration_tree, condition_tree)
root.order.add_edge(condition_tree, archival_tree)
root.order.add_edge(archival_tree, final_approval_tree)

print(root)