import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
login = Transition(label='Login')
select_items = Transition(label='Select items')
set_payment_method = Transition(label='Set payment method')
pay = Transition(label='Pay')
complete_installment_agreement = Transition(label='Complete installment agreement')
select_free_reward = Transition(label='Select free reward')
deliver_items = Transition(label='Deliver items')
return_items = Transition(label='Return items')

# Define silent transitions
skip = SilentTransition()

# Define the partial order model
root = StrictPartialOrder()

# Define the choices
xor_select_payment_method = OperatorPOWL(operator=Operator.XOR, children=[set_payment_method, skip])
xor_select_free_reward = OperatorPOWL(operator=Operator.XOR, children=[select_free_reward, skip])

# Define the loops
loop_select_items = OperatorPOWL(operator=Operator.LOOP, children=[select_items, xor_select_payment_method, xor_select_free_reward])
loop_return_items = OperatorPOWL(operator=Operator.LOOP, children=[return_items, deliver_items])

# Define the main path
xor_login_pay = OperatorPOWL(operator=Operator.XOR, children=[login, pay])
xor_login_installment = OperatorPOWL(operator=Operator.XOR, children=[login, complete_installment_agreement])

# Add the nodes to the root
root.add_node(loop_select_items)
root.add_node(loop_return_items)
root.add_node(xor_login_pay)
root.add_node(xor_login_installment)

# Add the edges
root.add_edge(xor_login_pay, loop_select_items)
root.add_edge(xor_login_installment, loop_select_items)
root.add_edge(loop_select_items, loop_return_items)
root.add_edge(loop_select_items, xor_login_pay)
root.add_edge(loop_select_items, xor_login_installment)
root.add_edge(loop_return_items, xor_login_pay)
root.add_edge(loop_return_items, xor_login_installment)

# Set the order
root.order.add_edge(loop_select_items, xor_login_pay)
root.order.add_edge(loop_select_items, xor_login_installment)
root.order.add_edge(loop_return_items, xor_login_pay)
root.order.add_edge(loop_return_items, xor_login_installment)