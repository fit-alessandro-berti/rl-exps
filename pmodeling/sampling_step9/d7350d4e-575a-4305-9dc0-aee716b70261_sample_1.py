import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, sample_collection])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[spectroscopy_test, carbon_dating])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, legal_clearance])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[cultural_assessment, digital_scan])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, stakeholder_meet])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[acquisition_vote, restoration_plan])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, archival_entry])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[final_approval, acquisition_vote])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop1)

# Print the POWL model
print(root)