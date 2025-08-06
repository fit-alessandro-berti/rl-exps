import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, insurance_quote])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, expert_review])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, owner_notify])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, customs_clear])

# Define XOR nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_setup, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[provenance_check, loop1, loop2, loop3, loop4, xor1, xor2, certification, final_audit])

# Add dependencies between nodes
root.order.add_edge(provenance_check, loop1)
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, certification)
root.order.add_edge(certification, final_audit)
root.order.add_edge(provenance_check, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, exhibit_setup)
root.order.add_edge(exhibit_setup, final_audit)
root.order.add_edge(provenance_check, loop3)
root.order.add_edge(loop3, xor2)
root.order.add_edge(xor2, exhibit_setup)
root.order.add_edge(exhibit_setup, final_audit)
root.order.add_edge(provenance_check, loop4)
root.order.add_edge(loop4, xor1)
root.order.add_edge(xor1, certification)
root.order.add_edge(certification, final_audit)

# Print the root POWL model
print(root)