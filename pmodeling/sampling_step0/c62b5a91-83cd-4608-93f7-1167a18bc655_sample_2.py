import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define loops and XORs for the workflow
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_research])
scientific_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[scientific_testing])
legal_clearance_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_clearance])
heritage_compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[heritage_compliance])
conservation_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[conservation_plan])
storage_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[storage_setup])
stakeholder_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_update])

# Define the workflow structure
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, provenance_loop, scientific_testing_loop, legal_clearance_loop, heritage_compliance_loop, digital_archiving, expert_review, committee_vote, acquisition_approval, conservation_plan_loop, storage_setup_loop, stakeholder_update_loop])
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, provenance_loop)
root.order.add_edge(provenance_loop, scientific_testing_loop)
root.order.add_edge(scientific_testing_loop, legal_clearance_loop)
root.order.add_edge(legal_clearance_loop, heritage_compliance_loop)
root.order.add_edge(heritage_compliance_loop, digital_archiving)
root.order.add_edge(digital_archiving, expert_review)
root.order.add_edge(expert_review, committee_vote)
root.order.add_edge(committee_vote, acquisition_approval)
root.order.add_edge(acquisition_approval, conservation_plan_loop)
root.order.add_edge(conservation_plan_loop, storage_setup_loop)
root.order.add_edge(storage_setup_loop, stakeholder_update_loop)