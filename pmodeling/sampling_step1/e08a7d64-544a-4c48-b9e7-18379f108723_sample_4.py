import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, insurance_quote])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, condition_report])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, digital_scan])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, customs_clear])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[certification, exhibit_setup])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[owner_notify, final_audit])

# Define the partial order
root = StrictPartialOrder(nodes=[provenance_check, material_testing, expert_review, xor1, xor2, xor3, xor4, xor5, xor6])

# Define the dependencies
root.order.add_edge(provenance_check, material_testing)
root.order.add_edge(provenance_check, expert_review)
root.order.add_edge(material_testing, xor1)
root.order.add_edge(expert_review, xor1)
root.order.add_edge(xor1, risk_assess)
root.order.add_edge(xor1, condition_report)
root.order.add_edge(risk_assess, xor2)
root.order.add_edge(condition_report, xor2)
root.order.add_edge(xor2, catalog_entry)
root.order.add_edge(xor2, digital_scan)
root.order.add_edge(catalog_entry, xor3)
root.order.add_edge(digital_scan, xor3)
root.order.add_edge(xor3, transport_plan)
root.order.add_edge(xor3, customs_clear)
root.order.add_edge(transport_plan, xor4)
root.order.add_edge(customs_clear, xor4)
root.order.add_edge(xor4, certification)
root.order.add_edge(xor4, exhibit_setup)
root.order.add_edge(certification, xor5)
root.order.add_edge(exhibit_setup, xor5)
root.order.add_edge(xor5, owner_notify)
root.order.add_edge(xor5, final_audit)
root.order.add_edge(owner_notify, xor6)
root.order.add_edge(final_audit, xor6)

# Print the final POWL model
print(root)