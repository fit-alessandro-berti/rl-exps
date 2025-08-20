from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Login = Transition(label='Login')
Select_items = Transition(label='Select items')
Set_payment_method = Transition(label='Set payment method')
Pay = Transition(label='Pay')
Complete_installment_agreement = Transition(label='Complete installment agreement')
Select_free_reward = Transition(label='Select free reward')
Deliver_items = Transition(label='Deliver items')
Return_items = Transition(label='Return items')

# Define the partial order
nodes = [Login, Select_items, Set_payment_method, Pay, Complete_installment_agreement, Select_free_reward, Deliver_items, Return_items]
order = set()

# Define the loop for returning items
loop = OperatorPOWL(operator=Operator.LOOP, children=[Return_items, Deliver_items])
order.add((loop, Deliver_items))

# Define the choice between paying and completing an installment agreement
xor = OperatorPOWL(operator=Operator.XOR, children=[Pay, Complete_installment_agreement])

# Define the partial order of the process
root = StrictPartialOrder(nodes=nodes, order=order)

# Add edges to the order set
root.order.add_edge(Login, Select_items)
root.order.add_edge(Login, Set_payment_method)
root.order.add_edge(Select_items, xor)
root.order.add_edge(Set_payment_method, xor)
root.order.add_edge(xor, Select_free_reward)
root.order.add_edge(Select_free_reward, loop)
root.order.add_edge(loop, Deliver_items)

# Print the POWL model
print(root)