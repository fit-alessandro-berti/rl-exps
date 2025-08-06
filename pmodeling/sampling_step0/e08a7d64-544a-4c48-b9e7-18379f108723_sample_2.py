import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
expert_review = Transition(label='Expert Review')
legal_verify = Transition(label='Legal Verify')
risk_assess = Transition(label='Risk Assess')
insurance_quote = Transition(label='Insurance Quote')
catalog_entry = Transition(label='Catalog Entry')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
transport_plan = Transition(label='Transport Plan')
customs_clear = Transition(label='Customs Clear')
certification = Transition(label='Certification')
exhibit_setup = Transition(label='Exhibit Setup')
owner_notify = Transition(label='Owner Notify')
final_audit = Transition(label='Final Audit')

# Define the silent transitions
skip = SilentTransition()

# Define the loops and XORs
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, legal_verify, risk_assess])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[insurance_quote, catalog_entry, digital_scan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, transport_plan, customs_clear])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[certification, exhibit_setup, owner_notify])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[final_audit, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, xor3, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, skip)

print(root)