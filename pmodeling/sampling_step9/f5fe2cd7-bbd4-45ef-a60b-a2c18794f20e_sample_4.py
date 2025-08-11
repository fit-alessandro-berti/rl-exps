import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, discrepancy_flag])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[discrepancy_flag, re_examination, alternative_source])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[re_examination, alternative_source])

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[document_audit, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, xor3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[stylistic_review, xor4])

# Define the root node
root = StrictPartialOrder(nodes=[provenance_check, material_scan, xor5, acquisition_vote, catalog_entry, exhibit_plan, final_approval])
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, xor5)
root.order.add_edge(xor5, acquisition_vote)
root.order.add_edge(acquisition_vote, catalog_entry)
root.order.add_edge(catalog_entry, exhibit_plan)
root.order.add_edge(exhibit_plan, final_approval)
root.order.add_edge(final_approval, skip)
root.order.add_edge(skip, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop1)
root.order.add_edge(loop3, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)

# Print the root node
print(root)