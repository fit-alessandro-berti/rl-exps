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

# Define silent transitions for empty labels
skip1 = SilentTransition()
skip2 = SilentTransition()

# Define the POWL model structure
root = StrictPartialOrder(
    nodes=[
        artifact_intake,
        condition_check,
        provenance_research,
        scientific_testing,
        radiocarbon_dating,
        spectroscopy_scan,
        legal_clearance,
        heritage_compliance,
        digital_archiving,
        expert_review,
        committee_vote,
        acquisition_approval,
        conservation_plan,
        storage_setup,
        stakeholder_update
    ],
    order={
        # Initial artifact intake and condition check
        artifact_intake: condition_check,
        # Provenance research
        condition_check: provenance_research,
        # Scientific testing
        provenance_research: scientific_testing,
        # Radiocarbon dating and spectroscopy scan
        scientific_testing: OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_dating, spectroscopy_scan]),
        # Legal clearance and heritage compliance
        OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_dating, spectroscopy_scan]): OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, heritage_compliance]),
        # Digital archiving
        OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, heritage_compliance]): digital_archiving,
        # Expert review and committee vote
        digital_archiving: OperatorPOWL(operator=Operator.XOR, children=[expert_review, committee_vote]),
        # Acquisition approval
        OperatorPOWL(operator=Operator.XOR, children=[expert_review, committee_vote]): acquisition_approval,
        # Conservation plan and storage setup
        acquisition_approval: OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, storage_setup]),
        # Stakeholder update
        OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, storage_setup]): stakeholder_update
    }
)

# Add dependencies for the partial order
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, provenance_research)
root.order.add_edge(provenance_research, scientific_testing)
root.order.add_edge(scientific_testing, OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_dating, spectroscopy_scan]))
root.order.add_edge(OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_dating, spectroscopy_scan]), OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, heritage_compliance]))
root.order.add_edge(OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, heritage_compliance]), digital_archiving)
root.order.add_edge(digital_archiving, OperatorPOWL(operator=Operator.XOR, children=[expert_review, committee_vote]))
root.order.add_edge(OperatorPOWL(operator=Operator.XOR, children=[expert_review, committee_vote]), acquisition_approval)
root.order.add_edge(acquisition_approval, OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, storage_setup]))
root.order.add_edge(OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, storage_setup]), stakeholder_update)

# Print the root
print(root)