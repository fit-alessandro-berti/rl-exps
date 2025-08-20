import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Login = Transition(label='Login')
SelectItems = Transition(label='Select items')
SetPaymentMethod = Transition(label='Set payment method')
Pay = Transition(label='Pay')
CompleteInstallmentAgreement = Transition(label='Complete installment agreement')
SelectFreeReward = Transition(label='Select free reward')
DeliverItems = Transition(label='Deliver items')
ReturnItems = Transition(label='Return items')

LoginToSelectItems = OperatorPOWL(operator=Operator.SEQUENCE, children=[Login, SelectItems])
SelectItemsToSetPaymentMethod = OperatorPOWL(operator=Operator.SEQUENCE, children=[SelectItems, SetPaymentMethod])
SetPaymentMethodToPayOrCompleteInstallmentAgreement = OperatorPOWL(operator=Operator.XOR, children=[Pay, CompleteInstallmentAgreement])
SelectItemsToSelectFreeReward = OperatorPOWL(operator=Operator.SEQUENCE, children=[SelectItems, SelectFreeReward])
SelectFreeRewardToDeliverItems = OperatorPOWL(operator=Operator.SEQUENCE, children=[SelectFreeReward, DeliverItems])
ReturnItemsToDeliverItems = OperatorPOWL(operator=Operator.LOOP, children=[ReturnItems, DeliverItems])

root = StrictPartialOrder(nodes=[LoginToSelectItems, SelectItemsToSetPaymentMethod, SetPaymentMethodToPayOrCompleteInstallmentAgreement, SelectItemsToSelectFreeReward, SelectFreeRewardToDeliverItems, ReturnItemsToDeliverItems])
root.order.add_edge(LoginToSelectItems, SelectItemsToSetPaymentMethod)
root.order.add_edge(SelectItemsToSetPaymentMethod, SetPaymentMethodToPayOrCompleteInstallmentAgreement)
root.order.add_edge(SetPaymentMethodToPayOrCompleteInstallmentAgreement, SelectItemsToSelectFreeReward)
root.order.add_edge(SelectItemsToSelectFreeReward, SelectFreeRewardToDeliverItems)
root.order.add_edge(SelectFreeRewardToDeliverItems, ReturnItemsToDeliverItems)
root.order.add_edge(ReturnItemsToDeliverItems, SelectFreeRewardToDeliverItems)