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

# Define the loops and choices
payment_choice = OperatorPOWL(operator=Operator.XOR, children=[pay, complete_installment_agreement])
return_loop = OperatorPOWL(operator=Operator.LOOP, children=[return_items, deliver_items])

# Define the root structure
root = StrictPartialOrder(nodes=[login, select_items, set_payment_method, payment_choice, select_free_reward, deliver_items, return_loop])
root.order.add_edge(login, select_items)
root.order.add_edge(login, set_payment_method)
root.order.add_edge(select_items, payment_choice)
root.order.add_edge(select_items, select_free_reward)
root.order.add_edge(payment_choice, deliver_items)
root.order.add_edge(deliver_items, return_loop)
root.order.add_edge(return_loop, deliver_items)