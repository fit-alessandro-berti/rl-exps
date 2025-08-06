import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan, archival_entry, final_approval])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, sample_collection])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, stakeholder_meet])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_clearance])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[cultural_assessment, digital_scan])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[report_draft, stakeholder_meet])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, stakeholder_meet])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, stakeholder_meet])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[archival_entry, stakeholder_meet])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, stakeholder_meet])

# Connect the partial order
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor3, xor6)
root.order.add_edge(xor4, xor7)
root.order.add_edge(xor5, xor8)
root.order.add_edge(xor6, xor9)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, loop)