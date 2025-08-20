import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Login = Transition(label='Login')
SelectItems = Transition(label='Select items')
SetPaymentMethod = Transition(label='Set payment method')
Pay = Transition(label='Pay')
CompleteInstallmentAgreement = Transition(label='Complete installment agreement')
SelectFreeReward = Transition(label='Select free reward')
DeliverItems = Transition(label='Deliver items')
ReturnItems = Transition(label='Return items')

# Define the loops
ReturnItemsLoop = OperatorPOWL(operator=Operator.LOOP, children=[ReturnItems, DeliverItems])

# Define the choice nodes
PaymentChoice = OperatorPOWL(operator=Operator.XOR, children=[Pay, CompleteInstallmentAgreement])
RewardChoice = OperatorPOWL(operator=Operator.XOR, children=[SelectFreeReward, SilentTransition()])

# Define the partial orders
OrderPO = StrictPartialOrder(nodes=[Login, SelectItems, SetPaymentMethod, PaymentChoice, RewardChoice, DeliverItems, ReturnItemsLoop])
OrderPO.order.add_edge(Login, SelectItems)
OrderPO.order.add_edge(Login, SetPaymentMethod)
OrderPO.order.add_edge(SelectItems, PaymentChoice)
OrderPO.order.add_edge(SelectItems, RewardChoice)
OrderPO.order.add_edge(SetPaymentMethod, PaymentChoice)
OrderPO.order.add_edge(PaymentChoice, DeliverItems)
OrderPO.order.add_edge(RewardChoice, DeliverItems)
OrderPO.order.add_edge(DeliverItems, ReturnItemsLoop)

root = OrderPO