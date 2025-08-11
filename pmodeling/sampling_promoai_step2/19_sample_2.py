import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
login = Transition(label='Login')
select_items = Transition(label='Select items')
set_payment_method = Transition(label='Set payment method')
select_free_reward = Transition(label='Select free reward')
pay = Transition(label='Pay')
complete_installment_agreement = Transition(label='Complete installment agreement')
deliver_items = Transition(label='Deliver items')
return_items = Transition(label='Return items')

# Create the POWL model
root = StrictPartialOrder(nodes=[login, select_items, set_payment_method, select_free_reward, pay, complete_installment_agreement, deliver_items, return_items])

# Define the control flow
root.order.add_edge(login, select_items)
root.order.add_edge(select_items, set_payment_method)
root.order.add_edge(set_payment_method, select_free_reward)
root.order.add_edge(select_free_reward, pay)
root.order.add_edge(pay, complete_installment_agreement)
root.order.add_edge(complete_installment_agreement, deliver_items)
root.order.add_edge(deliver_items, return_items)

# Print the root model
print(root)