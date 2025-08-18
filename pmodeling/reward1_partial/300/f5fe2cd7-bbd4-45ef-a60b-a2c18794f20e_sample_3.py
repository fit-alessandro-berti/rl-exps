from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[discrepancy_flag, alternative_source])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[re_examination, expert_consult])
loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, document_audit, xor2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, final_approval])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan, radiocarbon_test, stylistic_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[xor3, xor4])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[xor, xor5])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor6])
root.order.add_edge(xor6, xor)
root.order.add_edge(xor6, xor5)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor5, xor3)
root.order.add_edge(xor5, xor4)

print(root)