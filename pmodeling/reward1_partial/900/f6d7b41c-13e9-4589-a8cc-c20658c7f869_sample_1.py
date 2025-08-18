import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loops and choices
art_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[art_selection, inventory_check])
art_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[art_selection_loop, skip])

legal_draft_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_draft, skip])

contract_sign_choice = OperatorPOWL(operator=Operator.XOR, children=[contract_sign, skip])

insurance_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, skip])

transport_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, skip])

secure_transit_choice = OperatorPOWL(operator=Operator.XOR, children=[secure_transit, skip])

art_install_choice = OperatorPOWL(operator=Operator.XOR, children=[art_install, skip])

condition_check_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_check, skip])

appraisal_log_choice = OperatorPOWL(operator=Operator.XOR, children=[appraisal_log, skip])

lease_renew_choice = OperatorPOWL(operator=Operator.XOR, children=[lease_renew, skip])

payment_process_choice = OperatorPOWL(operator=Operator.XOR, children=[payment_process, skip])

deinstall_art_choice = OperatorPOWL(operator=Operator.XOR, children=[deinstall_art, skip])

return_inspect_choice = OperatorPOWL(operator=Operator.XOR, children=[return_inspect, skip])

purchase_option_choice = OperatorPOWL(operator=Operator.XOR, children=[purchase_option, skip])

# Define the root Partial Order
root = StrictPartialOrder(nodes=[
    client_consult,
    needs_assess,
    art_selection_choice,
    legal_draft_choice,
    contract_sign_choice,
    insurance_setup_choice,
    transport_plan_choice,
    secure_transit_choice,
    art_install_choice,
    condition_check_choice,
    appraisal_log_choice,
    lease_renew_choice,
    payment_process_choice,
    deinstall_art_choice,
    return_inspect_choice,
    purchase_option_choice
])

# Define the order of execution
root.order.add_edge(client_consult, needs_assess)
root.order.add_edge(needs_assess, art_selection_choice)
root.order.add_edge(art_selection_choice, legal_draft_choice)
root.order.add_edge(legal_draft_choice, contract_sign_choice)
root.order.add_edge(contract_sign_choice, insurance_setup_choice)
root.order.add_edge(insurance_setup_choice, transport_plan_choice)
root.order.add_edge(transport_plan_choice, secure_transit_choice)
root.order.add_edge(secure_transit_choice, art_install_choice)
root.order.add_edge(art_install_choice, condition_check_choice)
root.order.add_edge(condition_check_choice, appraisal_log_choice)
root.order.add_edge(appraisal_log_choice, lease_renew_choice)
root.order.add_edge(lease_renew_choice, payment_process_choice)
root.order.add_edge(payment_process_choice, deinstall_art_choice)
root.order.add_edge(deinstall_art_choice, return_inspect_choice)
root.order.add_edge(return_inspect_choice, purchase_option_choice)

# Print the root
print(root)