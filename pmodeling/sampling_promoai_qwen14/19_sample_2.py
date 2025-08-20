import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Login = Transition(label='Login')
Select_items = Transition(label='Select items')
Set_payment_method = Transition(label='Set payment method')
Pay = Transition(label='Pay')
Complete_installment_agreement = Transition(label='Complete installment agreement')
Select_free_reward = Transition(label='Select free reward')
Deliver_items = Transition(label='Deliver_items')
Return_items = Transition(label='Return items')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Pay, Complete_installment_agreement])
xor = OperatorPOWL(operator=Operator.XOR, children=[loop, skip])

root = StrictPartialOrder(nodes=[Login, Select_items, Set_payment_method, xor, Select_free_reward, Deliver_items, Return_items])
root.order.add_edge(Login, Select_items)
root.order.add_edge(Login, Set_payment_method)
root.order.add_edge(Select_items, xor)
root.order.add_edge(Set_payment_method, xor)
root.order.add_edge(xor, Select_free_reward)
root.order.add_edge(Select_free_reward, Deliver_items)
root.order.add_edge(Deliver_items, Return_items)