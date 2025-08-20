import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
login = Transition(label='Login')
select_items = Transition(label='Select items')
set_payment_method = Transition(label='Set payment method')
pay = Transition(label='Pay')
select_reward = Transition(label='Select free reward')
complete_installment = Transition(label='Complete installment agreement')
deliver = Transition(label='Deliver items')
return_items = Transition(label='Return items')
skip = SilentTransition()

loop_pay = OperatorPOWL(operator=Operator.LOOP, children=[pay])
xor_select_reward = OperatorPOWL(operator=Operator.XOR, children=[select_reward, skip])
xor_pay_installment = OperatorPOWL(operator=Operator.XOR, children=[pay, complete_installment])

root = StrictPartialOrder(nodes=[login, select_items, set_payment_method, loop_pay, xor_select_reward, xor_pay_installment, deliver, return_items])
root.order.add_edge(login, select_items)
root.order.add_edge(select_items, set_payment_method)
root.order.add_edge(set_payment_method, loop_pay)
root.order.add_edge(loop_pay, xor_select_reward)
root.order.add_edge(xor_select_reward, xor_pay_installment)
root.order.add_edge(xor_pay_installment, deliver)
root.order.add_edge(deliver, return_items)
root.order.add_edge(return_items, loop_pay)