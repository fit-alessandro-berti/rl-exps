import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Define the operators (choices and loops)
# No loops are needed here as there are no explicit loops in the process description.
xor1 = OperatorPOWL(operator=Operator.XOR, children=[stylistic_review, expert_consult])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[document_audit, legal_verify])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, discrepancy_flag])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[re_examination, alternative_source])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, catalog_entry])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_plan, final_approval])

# Construct the partial order
root = StrictPartialOrder(nodes=[provenance_check, material_scan, radiocarbon_test, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, radiocarbon_test)
root.order.add_edge(radiocarbon_test, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, final_approval)

print(root)