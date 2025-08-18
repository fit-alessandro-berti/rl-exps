import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
provenance_research = Transition(label='Provenance Research')
scientific_testing = Transition(label='Scientific Testing')
radiocarbon_dating = Transition(label='Radiocarbon Dating')
spectroscopy_scan = Transition(label='Spectroscopy Scan')
legal_clearance = Transition(label='Legal Clearance')
heritage_compliance = Transition(label='Heritage Compliance')
digital_archiving = Transition(label='Digital Archiving')
expert_review = Transition(label='Expert Review')
committee_vote = Transition(label='Committee Vote')
acquisition_approval = Transition(label='Acquisition Approval')
conservation_plan = Transition(label='Conservation Plan')
storage_setup = Transition(label='Storage Setup')
stakeholder_update = Transition(label='Stakeholder Update')

# Define silent transitions
skip = SilentTransition()

# Define partial order nodes
artifact_intake_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[artifact_intake])
condition_check_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[condition_check])
provenance_research_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[provenance_research])
scientific_testing_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[scientific_testing])
radiocarbon_dating_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[radiocarbon_dating])
spectroscopy_scan_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[spectroscopy_scan])
legal_clearance_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[legal_clearance])
heritage_compliance_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[heritage_compliance])
digital_archiving_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[digital_archiving])
expert_review_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[expert_review])
committee_vote_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[committee_vote])
acquisition_approval_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[acquisition_approval])
conservation_plan_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[conservation_plan])
storage_setup_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[storage_setup])
stakeholder_update_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[stakeholder_update])

# Define partial order edges
partial_order = StrictPartialOrder(nodes=[
    artifact_intake_node,
    condition_check_node,
    provenance_research_node,
    scientific_testing_node,
    radiocarbon_dating_node,
    spectroscopy_scan_node,
    legal_clearance_node,
    heritage_compliance_node,
    digital_archiving_node,
    expert_review_node,
    committee_vote_node,
    acquisition_approval_node,
    conservation_plan_node,
    storage_setup_node,
    stakeholder_update_node
])

partial_order.order.add_edge(artifact_intake_node, condition_check_node)
partial_order.order.add_edge(artifact_intake_node, provenance_research_node)
partial_order.order.add_edge(condition_check_node, scientific_testing_node)
partial_order.order.add_edge(provenance_research_node, scientific_testing_node)
partial_order.order.add_edge(scientific_testing_node, radiocarbon_dating_node)
partial_order.order.add_edge(scientific_testing_node, spectroscopy_scan_node)
partial_order.order.add_edge(radiocarbon_dating_node, legal_clearance_node)
partial_order.order.add_edge(spectroscopy_scan_node, legal_clearance_node)
partial_order.order.add_edge(legal_clearance_node, heritage_compliance_node)
partial_order.order.add_edge(heritage_compliance_node, digital_archiving_node)
partial_order.order.add_edge(digital_archiving_node, expert_review_node)
partial_order.order.add_edge(expert_review_node, committee_vote_node)
partial_order.order.add_edge(committee_vote_node, acquisition_approval_node)
partial_order.order.add_edge(acquisition_approval_node, conservation_plan_node)
partial_order.order.add_edge(conservation_plan_node, storage_setup_node)
partial_order.order.add_edge(storage_setup_node, stakeholder_update_node)

# Set root to the partial order
root = partial_order