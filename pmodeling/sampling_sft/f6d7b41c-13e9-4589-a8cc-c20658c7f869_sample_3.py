import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
client_consult    = Transition(label='Client Consult')
needs_assess      = Transition(label='Needs Assess')
art_selection     = Transition(label='Art Selection')
inventory_check   = Transition(label='Inventory Check')
legal_draft       = Transition(label='Legal Draft')
contract_sign     = Transition(label='Contract Sign')
insurance_setup   = Transition(label='Insurance Setup')
transport_plan    = Transition(label='Transport Plan')
secure_transit    = Transition(label='Secure Transit')
art_install       = Transition(label='Art Install')
condition_check   = Transition(label='Condition Check')
appraisal_log     = Transition(label='Appraisal Log')
lease_renew       = Transition(label='Lease Renew')
payment_process   = Transition(label='Payment Process')
deinstall_art     = Transition(label='Deinstall Art')
return_inspect    = Transition(label='Return Inspect')
purchase_option   = Transition(label='Purchase Option')

# Loop for periodic condition check and appraisal
skip = SilentTransition()
condition_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_check, skip])
appraisal_loop = OperatorPOWL(operator=Operator.LOOP, children=[appraisal_log, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    client_consult, needs_assess, art_selection, inventory_check,
    legal_draft, contract_sign, insurance_setup, transport_plan,
    secure_transit, art_install, condition_loop, appraisal_loop,
    lease_renew, payment_process, deinstall_art, return_inspect,
    purchase_option
])

# Define the control-flow dependencies
root.order.add_edge(client_consult, needs_assess)
root.order.add_edge(needs_assess, art_selection)
root.order.add_edge(art_selection, inventory_check)
root.order.add_edge(inventory_check, legal_draft)
root.order.add_edge(legal_draft, contract_sign)
root.order.add_edge(contract_sign, insurance_setup)
root.order.add_edge(insurance_setup, transport_plan)
root.order.add_edge(transport_plan, secure_transit)
root.order.add_edge(secure_transit, art_install)

# After installation, do the periodic checks and appraisals
root.order.add_edge(art_install, condition_loop)
root.order.add_edge(art_install, appraisal_loop)

# After the loop, proceed to renewal and payment
root.order.add_edge(condition_loop, lease_renew)
root.order.add_edge(appraisal_loop, lease_renew)
root.order.add_edge(lease_renew, payment_process)

# Finally, do the deinstallation and either return or purchase
root.order.add_edge(payment_process, deinstall_art)
root.order.add_edge(deinstall_art, return_inspect)
root.order.add_edge(deinstall_art, purchase_option)