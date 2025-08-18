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

# Define the loops and choices
art_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[art_selection, inventory_check])
legal_draft_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_draft, contract_sign, insurance_setup])
transport_loop = OperatorPOWL(operator=Operator.LOOP, children=[transport_plan, secure_transit])
art_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[art_install, condition_check, appraisal_log])
payment_loop = OperatorPOWL(operator=Operator.LOOP, children=[payment_process, lease_renew])
deinstall_loop = OperatorPOWL(operator=Operator.LOOP, children=[deinstall_art, return_inspect, purchase_option])

# Define the root POWL model
root = StrictPartialOrder(nodes=[client_consult, needs_assess, art_selection_loop, legal_draft_loop, transport_loop, art_install_loop, payment_loop, deinstall_loop])
root.order.add_edge(client_consult, needs_assess)
root.order.add_edge(needs_assess, art_selection_loop)
root.order.add_edge(art_selection_loop, legal_draft_loop)
root.order.add_edge(legal_draft_loop, transport_loop)
root.order.add_edge(transport_loop, art_install_loop)
root.order.add_edge(art_install_loop, payment_loop)
root.order.add_edge(payment_loop, deinstall_loop)
root.order.add_edge(deinstall_loop, deinstall_loop)