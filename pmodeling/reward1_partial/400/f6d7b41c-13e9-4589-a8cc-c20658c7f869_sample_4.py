import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Add activities as transitions
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

# Add activities to the root
root.nodes.append(client_consult)
root.nodes.append(needs_assess)
root.nodes.append(art_selection)
root.nodes.append(inventory_check)
root.nodes.append(legal_draft)
root.nodes.append(contract_sign)
root.nodes.append(insurance_setup)
root.nodes.append(transport_plan)
root.nodes.append(secure_transit)
root.nodes.append(art_install)
root.nodes.append(condition_check)
root.nodes.append(appraisal_log)
root.nodes.append(lease_renew)
root.nodes.append(payment_process)
root.nodes.append(deinstall_art)
root.nodes.append(return_inspect)
root.nodes.append(purchase_option)

# Define the order of activities
root.order.add_edge(client_consult, needs_assess)
root.order.add_edge(needs_assess, art_selection)
root.order.add_edge(art_selection, inventory_check)
root.order.add_edge(inventory_check, legal_draft)
root.order.add_edge(legal_draft, contract_sign)
root.order.add_edge(contract_sign, insurance_setup)
root.order.add_edge(insurance_setup, transport_plan)
root.order.add_edge(transport_plan, secure_transit)
root.order.add_edge(secure_transit, art_install)
root.order.add_edge(art_install, condition_check)
root.order.add_edge(condition_check, appraisal_log)
root.order.add_edge(appraisal_log, lease_renew)
root.order.add_edge(lease_renew, payment_process)
root.order.add_edge(payment_process, deinstall_art)
root.order.add_edge(deinstall_art, return_inspect)
root.order.add_edge(return_inspect, purchase_option)

# Print the final POWL model
print(root)