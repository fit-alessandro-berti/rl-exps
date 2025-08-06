import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define nodes and loops
client_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_consult, needs_assess])
art_loop = OperatorPOWL(operator=Operator.LOOP, children=[art_selection, inventory_check])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_draft, contract_sign, insurance_setup, transport_plan, secure_transit])
logistics_loop = OperatorPOWL(operator=Operator.LOOP, children=[art_install, condition_check, appraisal_log])
finance_loop = OperatorPOWL(operator=Operator.LOOP, children=[lease_renew, payment_process])
deinstallation_loop = OperatorPOWL(operator=Operator.LOOP, children=[deinstall_art, return_inspect, purchase_option])

# Define partial order
root = StrictPartialOrder(nodes=[client_loop, art_loop, legal_loop, logistics_loop, finance_loop, deinstallation_loop])
root.order.add_edge(client_loop, art_loop)
root.order.add_edge(art_loop, legal_loop)
root.order.add_edge(legal_loop, logistics_loop)
root.order.add_edge(logistics_loop, finance_loop)
root.order.add_edge(finance_loop, deinstallation_loop)

# Print the root
print(root)