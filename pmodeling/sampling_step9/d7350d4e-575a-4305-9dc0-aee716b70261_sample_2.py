import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loops
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, sample_collection])
sample_loop = OperatorPOWL(operator=Operator.LOOP, children=[spectroscopy_test, carbon_dating])
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, legal_clearance, cultural_assessment])
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_scan, report_draft])
stakeholder_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet, acquisition_vote])
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan, condition_report])
archival_loop = OperatorPOWL(operator=Operator.LOOP, children=[archival_entry, final_approval])

# Define the XORs
provenance_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_loop, skip])
sample_xor = OperatorPOWL(operator=Operator.XOR, children=[sample_loop, skip])
expert_xor = OperatorPOWL(operator=Operator.XOR, children=[expert_loop, skip])
report_xor = OperatorPOWL(operator=Operator.XOR, children=[report_loop, skip])
stakeholder_xor = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_loop, skip])
restoration_xor = OperatorPOWL(operator=Operator.XOR, children=[restoration_loop, skip])
archival_xor = OperatorPOWL(operator=Operator.XOR, children=[archival_loop, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[provenance_xor, sample_xor, expert_xor, report_xor, stakeholder_xor, restoration_xor, archival_xor])
root.order.add_edge(provenance_xor, sample_xor)
root.order.add_edge(sample_xor, expert_xor)
root.order.add_edge(expert_xor, report_xor)
root.order.add_edge(report_xor, stakeholder_xor)
root.order.add_edge(stakeholder_xor, restoration_xor)
root.order.add_edge(restoration_xor, archival_xor)

print(root)