from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the loop for the lease renewal process
loop = OperatorPOWL(operator=Operator.LOOP, children=[lease_renew, payment_process])

# Define the exclusive choice for the artwork selection process
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[art_selection, inventory_check])

# Create the POWL model
root = StrictPartialOrder(nodes=[client_consult, needs_assess, exclusive_choice, legal_draft, contract_sign, insurance_setup, transport_plan, secure_transit, art_install, condition_check, appraisal_log, loop, deinstall_art, return_inspect, purchase_option])

# Define the order of execution
root.order.add_edge(client_consult, needs_assess)
root.order.add_edge(needs_assess, exclusive_choice)
root.order.add_edge(exclusive_choice, legal_draft)
root.order.add_edge(legal_draft, contract_sign)
root.order.add_edge(contract_sign, insurance_setup)
root.order.add_edge(insurance_setup, transport_plan)
root.order.add_edge(transport_plan, secure_transit)
root.order.add_edge(secure_transit, art_install)
root.order.add_edge(art_install, condition_check)
root.order.add_edge(condition_check, appraisal_log)
root.order.add_edge(appraisal_log, loop)
root.order.add_edge(loop, lease_renew)
root.order.add_edge(loop, payment_process)
root.order.add_edge(lease_renew, deinstall_art)
root.order.add_edge(lease_renew, return_inspect)
root.order.add_edge(lease_renew, purchase_option)
root.order.add_edge(deinstall_art, return_inspect)
root.order.add_edge(return_inspect, purchase_option)

print(root)