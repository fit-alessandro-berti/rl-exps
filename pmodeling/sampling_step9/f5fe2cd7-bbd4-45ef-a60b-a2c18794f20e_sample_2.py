import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop_acquisition = OperatorPOWL(operator=Operator.LOOP, children=[discrepancy_flag, re_examination, alternative_source])
xor_acquisition = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, condition_report])
xor_document = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, document_audit])
xor_material = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, stylistic_review])
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_scan])

root = StrictPartialOrder(nodes=[loop_acquisition, xor_acquisition, xor_document, xor_material, xor_provenance])
root.order.add_edge(xor_provenance, xor_material)
root.order.add_edge(xor_material, xor_document)
root.order.add_edge(xor_document, xor_acquisition)
root.order.add_edge(xor_acquisition, loop_acquisition)
root.order.add_edge(loop_acquisition, acquisition_vote)
root.order.add_edge(acquisition_vote, catalog_entry)
root.order.add_edge(catalog_entry, exhibit_plan)
root.order.add_edge(exhibit_plan, final_approval)

print(root)