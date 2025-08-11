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

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()

# Define loops
provenance_research_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_research, skip1])
scientific_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[scientific_testing, skip2])

# Define XORs
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, heritage_compliance])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, committee_vote])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, provenance_research_loop, scientific_testing_loop, xor1, xor2, acquisition_approval, conservation_plan, storage_setup, stakeholder_update])
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, provenance_research_loop)
root.order.add_edge(provenance_research_loop, scientific_testing_loop)
root.order.add_edge(scientific_testing_loop, xor1)
root.order.add_edge(xor1, acquisition_approval)
root.order.add_edge(acquisition_approval, conservation_plan)
root.order.add_edge(conservation_plan, storage_setup)
root.order.add_edge(storage_setup, stakeholder_update)

# Print the root of the POWL model
print(root)