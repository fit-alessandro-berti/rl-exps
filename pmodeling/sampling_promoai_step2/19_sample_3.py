import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
login = Transition(label='Login')
select_items = Transition(label='Select items')
set_payment_method = Transition(label='Set payment method')
pay = Transition(label='Pay')
complete_installment_agreement = Transition(label='Complete installment agreement')
select_free_reward = Transition(label='Select free reward')
deliver_items = Transition(label='Deliver items')
return_items = Transition(label='Return items')

# Define the POWL model
root = StrictPartialOrder(nodes=[login, select_items, set_payment_method, pay, complete_installment_agreement, select_free_reward, deliver_items, return_items])
root.order.add_edge(login, select_items)
root.order.add_edge(login, set_payment_method)
root.order.add_edge(select_items, pay)
root.order.add_edge(select_items, complete_installment_agreement)
root.order.add_edge(set_payment_method, pay)
root.order.add_edge(set_payment_method, complete_installment_agreement)
root.order.add_edge(pay, select_free_reward)
root.order.add_edge(complete_installment_agreement, select_free_reward)
root.order.add_edge(select_free_reward, deliver_items)
root.order.add_edge(deliver_items, return_items)

# Print the POWL model
print(root)