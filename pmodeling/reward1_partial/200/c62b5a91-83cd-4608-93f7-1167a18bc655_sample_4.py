import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
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

# Define the loop and exclusive choice
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    scientific_testing, radiocarbon_dating, spectroscopy_scan
])
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[
    legal_clearance, heritage_compliance
])

# Define the root partial order
root = StrictPartialOrder(nodes=[
    artifact_intake, condition_check, provenance_research, exclusive_choice,
    loop, digital_archiving, expert_review, committee_vote, acquisition_approval,
    conservation_plan, storage_setup, stakeholder_update
])

# Add dependencies
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(artifact_intake, provenance_research)
root.order.add_edge(condition_check, provenance_research)
root.order.add_edge(provenance_research, exclusive_choice)
root.order.add_edge(exclusive_choice, loop)
root.order.add_edge(exclusive_choice, digital_archiving)
root.order.add_edge(digital_archiving, expert_review)
root.order.add_edge(expert_review, committee_vote)
root.order.add_edge(committee_vote, acquisition_approval)
root.order.add_edge(acquisition_approval, conservation_plan)
root.order.add_edge(conservation_plan, storage_setup)
root.order.add_edge(storage_setup, stakeholder_update)