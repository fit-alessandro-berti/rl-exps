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

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[art_selection, inventory_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[legal_draft, contract_sign])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[insurance_setup, transport_plan])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[secure_transit, art_install])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[condition_check, appraisal_log])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[lease_renew, payment_process])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[deinstall_art, return_inspect])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[purchase_option, skip])

# Define root node
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop1)