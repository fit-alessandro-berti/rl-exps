import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, cultural_assessment])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, sample_collection])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[spectroscopy_test, carbon_dating])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, digital_scan])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, stakeholder_meet])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, condition_report])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[archival_entry, final_approval])

# Define the partial order
root = StrictPartialOrder(nodes=[
    xor1, xor2, xor3, xor4, xor5, xor6, xor7
])

# Add the dependencies
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)

# Print the root model
print(root)