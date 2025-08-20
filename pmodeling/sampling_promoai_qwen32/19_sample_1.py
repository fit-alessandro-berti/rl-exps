from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Login = Transition(label='Login')
Select_items = Transition(label='Select items')
Set_payment_method = Transition(label='Set payment method')
Pay = Transition(label='Pay')
Complete_installment_agreement = Transition(label='Complete installment agreement')
Select_free_reward = Transition(label='Select free reward')
Deliver_items = Transition(label='Deliver items')
Return_items = Transition(label='Return items')

# Define loops
loop_return_items = OperatorPOWL(operator=Operator.LOOP, children=[Return_items, Deliver_items])

# Define choices
choice_payment = OperatorPOWL(operator=Operator.XOR, children=[Pay, Complete_installment_agreement])
choice_reward = OperatorPOWL(operator=Operator.XOR, children=[Select_free_reward, SilentTransition()])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[Login, Select_items, Set_payment_method, choice_payment, choice_reward, Deliver_items, loop_return_items])
root.order.add_edge(Login, Select_items)
root.order.add_edge(Login, Set_payment_method)
root.order.add_edge(Select_items, choice_reward)
root.order.add_edge(Set_payment_method, choice_payment)
root.order.add_edge(choice_payment, Deliver_items)
root.order.add_edge(choice_reward, Deliver_items)
root.order.add_edge(Deliver_items, loop_return_items)