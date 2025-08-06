import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define nodes
provenance_node = OperatorPOWL(operator=Operator.PARALLEL, children=[provenance_check, sample_collection])
sample_node = OperatorPOWL(operator=Operator.PARALLEL, children=[spectroscopy_test, carbon_dating])
expert_node = OperatorPOWL(operator=Operator.PARALLEL, children=[expert_review, legal_clearance])
cultural_node = OperatorPOWL(operator=Operator.PARALLEL, children=[cultural_assessment, digital_scan])
report_node = OperatorPOWL(operator=Operator.PARALLEL, children=[report_draft, stakeholder_meet])
acquisition_node = OperatorPOWL(operator=Operator.PARALLEL, children=[acquisition_vote, restoration_plan])
condition_node = OperatorPOWL(operator=Operator.PARALLEL, children=[condition_report, archival_entry])
final_node = OperatorPOWL(operator=Operator.PARALLEL, children=[final_approval])

# Define order
root = StrictPartialOrder(nodes=[provenance_node, sample_node, expert_node, cultural_node, report_node, acquisition_node, condition_node, final_node])
root.order.add_edge(provenance_node, sample_node)
root.order.add_edge(sample_node, expert_node)
root.order.add_edge(expert_node, cultural_node)
root.order.add_edge(cultural_node, report_node)
root.order.add_edge(report_node, acquisition_node)
root.order.add_edge(acquisition_node, condition_node)
root.order.add_edge(condition_node, final_node)