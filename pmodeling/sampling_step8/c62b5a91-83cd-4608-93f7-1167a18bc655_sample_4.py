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

# Define the loop for the scientific testing process
loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_dating, spectroscopy_scan])

# Define the exclusive choice for the legal clearance and heritage compliance processes
xor = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, heritage_compliance])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    provenance_research,
    scientific_testing,
    loop,
    xor,
    digital_archiving,
    expert_review,
    committee_vote,
    acquisition_approval,
    conservation_plan,
    storage_setup,
    stakeholder_update
])

# Define the dependencies between the nodes
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, provenance_research)
root.order.add_edge(provenance_research, scientific_testing)
root.order.add_edge(scientific_testing, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, digital_archiving)
root.order.add_edge(digital_archiving, expert_review)
root.order.add_edge(expert_review, committee_vote)
root.order.add_edge(committee_vote, acquisition_approval)
root.order.add_edge(acquisition_approval, conservation_plan)
root.order.add_edge(conservation_plan, storage_setup)
root.order.add_edge(storage_setup, stakeholder_update)

# Print the root model
print(root)