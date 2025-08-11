import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
radiocarbon_test = Transition(label='Radiocarbon Test')
stylistic_review = Transition(label='Stylistic Review')
expert_consult = Transition(label='Expert Consult')
document_audit = Transition(label='Document Audit')
legal_verify = Transition(label='Legal Verify')
condition_report = Transition(label='Condition Report')
discrepancy_flag = Transition(label='Discrepancy Flag')
re_examination = Transition(label='Re-examination')
alternative_source = Transition(label='Alternative Source')
acquisition_vote = Transition(label='Acquisition Vote')
catalog_entry = Transition(label='Catalog Entry')
exhibit_plan = Transition(label='Exhibit Plan')
final_approval = Transition(label='Final Approval')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[discrepancy_flag, alternative_source])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, re_examination])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, document_audit])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, stylistic_review])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test, material_scan])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, acquisition_vote])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[catalog_entry, exhibit_plan])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[final_approval, loop1])

# Define partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop1)

# Print the final result
print(root)