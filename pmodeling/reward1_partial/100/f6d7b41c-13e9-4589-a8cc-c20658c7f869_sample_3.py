import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
client_consult = Transition(label='Client Consult')
needs_assess = Transition(label='Needs Assess')
art_selection = Transition(label='Art Selection')
inventory_check = Transition(label='Inventory Check')
legal_draft = Transition(label='Legal Draft')
contract_sign = Transition(label='Contract Sign')
insurance_setup = Transition(label='Insurance Setup')
transport_plan = Transition(label='Transport Plan')
secure_transit = Transition(label='Secure Transit')
art_install = Transition(label='Art Install')
condition_check = Transition(label='Condition Check')
appraisal_log = Transition(label='Appraisal Log')
lease_renew = Transition(label='Lease Renew')
payment_process = Transition(label='Payment Process')
deinstall_art = Transition(label='Deinstall Art')
return_inspect = Transition(label='Return Inspect')
purchase_option = Transition(label='Purchase Option')

# Define the POWL structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[art_selection, inventory_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_draft, contract_sign])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, transport_plan])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[secure_transit, art_install])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[condition_check, appraisal_log])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[lease_renew, payment_process])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[deinstall_art, return_inspect])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[purchase_option, purchase_option])  # Assuming purchase option can be repeated

# Construct the partial order
root = StrictPartialOrder(nodes=[client_consult, needs_assess, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(client_consult, needs_assess)
root.order.add_edge(needs_assess, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor8)

# Print the root model
print(root)