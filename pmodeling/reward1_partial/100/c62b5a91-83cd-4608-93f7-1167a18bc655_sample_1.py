import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the relationships
artifact_intake_order = OperatorPOWL(operator=Operator.ORDER, children=[condition_check, provenance_research, scientific_testing, radiocarbon_dating, spectroscopy_scan, legal_clearance, heritage_compliance])
provenance_research_order = OperatorPOWL(operator=Operator.ORDER, children=[digital_archiving, expert_review, committee_vote])
scientific_testing_order = OperatorPOWL(operator=Operator.ORDER, children=[radiocarbon_dating, spectroscopy_scan])
legal_clearance_order = OperatorPOWL(operator=Operator.ORDER, children=[heritage_compliance])
committee_vote_order = OperatorPOWL(operator=Operator.ORDER, children=[acquisition_approval, conservation_plan])
expert_review_order = OperatorPOWL(operator=Operator.ORDER, children=[digital_archiving])
conservation_plan_order = OperatorPOWL(operator=Operator.ORDER, children=[storage_setup, stakeholder_update])

# Construct the POWL model
root = StrictPartialOrder(nodes=[artifact_intake_order, provenance_research_order, scientific_testing_order, legal_clearance_order, committee_vote_order, expert_review_order, conservation_plan_order])
root.order.add_edge(artifact_intake_order, provenance_research_order)
root.order.add_edge(provenance_research_order, digital_archiving)
root.order.add_edge(provenance_research_order, expert_review)
root.order.add_edge(provenance_research_order, committee_vote)
root.order.add_edge(scientific_testing_order, radiocarbon_dating)
root.order.add_edge(scientific_testing_order, spectroscopy_scan)
root.order.add_edge(legal_clearance_order, heritage_compliance)
root.order.add_edge(committee_vote_order, acquisition_approval)
root.order.add_edge(committee_vote_order, conservation_plan)
root.order.add_edge(expert_review_order, digital_archiving)
root.order.add_edge(conservation_plan_order, storage_setup)
root.order.add_edge(conservation_plan_order, stakeholder_update)

print(root)