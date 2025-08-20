from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Login = Transition(label='Login')
Select_items = Transition(label='Select items')
Set_payment_method = Transition(label='Set payment method')
Pay = Transition(label='Pay')
Complete_installment_agreement = Transition(label='Complete installment agreement')
Select_free_reward = Transition(label='Select free reward')
Deliver_items = Transition(label='Deliver items')
Return_items = Transition(label='Return items')

# Define the POWL model
# User starts an order by logging in to their account
root = Login

# Then, the user simultaneously selects the items to purchase and sets a payment method
parallel = StrictPartialOrder(nodes=[Select_items, Set_payment_method])
root.order.add_edge(root, parallel)

# Afterward, the user either pays or completes an installment agreement
choice = OperatorPOWL(operator=Operator.XOR, children=[Pay, Complete_installment_agreement])
root.order.add_edge(parallel, choice)

# After selecting the items, the user chooses between multiple options for a free reward
root.order.add_edge(Select_items, Select_free_reward)

# Finally, the items are delivered
root.order.add_edge(choice, Deliver_items)

# The user has the right to return items for exchange. Every time items are returned, a new delivery is made.
loop = OperatorPOWL(operator=Operator.LOOP, children=[Return_items, Deliver_items])
root.order.add_edge(Deliver_items, loop)

# The final result is saved in the variable 'root'