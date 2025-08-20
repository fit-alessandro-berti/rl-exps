import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
login = Transition(label='Login')
select_items = Transition(label='Select items')
set_payment_method = Transition(label='Set payment method')
pay = Transition(label='Pay')
complete_installment_agreement = Transition(label='Complete installment agreement')
select_free_reward = Transition(label='Select free reward')
deliver_items = Transition(label='Deliver items')
return_items = Transition(label='Return items')

# Define silent activities
skip = SilentTransition()

# Define POWL models
select_items_and_set_payment_method = OperatorPOWL(operator=Operator.XOR, children=[select_items, set_payment_method])
select_items_and_set_payment_method_loop = OperatorPOWL(operator=Operator.LOOP, children=[select_items_and_set_payment_method])
pay_or_complete_installment_agreement = OperatorPOWL(operator=Operator.XOR, children=[pay, complete_installment_agreement])
select_free_reward_loop = OperatorPOWL(operator=Operator.LOOP, children=[select_free_reward])

# Define partial order
root = StrictPartialOrder(nodes=[login, select_items_and_set_payment_method_loop, pay_or_complete_installment_agreement, select_free_reward_loop, deliver_items, return_items])
root.order.add_edge(login, select_items_and_set_payment_method_loop)
root.order.add_edge(select_items_and_set_payment_method_loop, pay_or_complete_installment_agreement)
root.order.add_edge(pay_or_complete_installment_agreement, select_free_reward_loop)
root.order.add_edge(select_free_reward_loop, deliver_items)
root.order.add_edge(deliver_items, return_items)

# Print the final result
print(root)