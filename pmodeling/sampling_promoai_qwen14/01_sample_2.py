import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ReceiveInquiry = Transition(label='Receive customer inquiry')
CollectInfo = Transition(label='Collect customer information')
AddressConcerns = Transition(label='Address customer concerns or questions')
GuideSelection = Transition(label='Guide customer in selecting product/service')
ProvideQuote = Transition(label='Provide quote')
PlaceOrder = Transition(label='Place order')
RecordOrder = Transition(label='Record order in system')
SendConfirmation = Transition(label='Send order confirmation to customer')

# Define silent transition
skip = SilentTransition()

# Define loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[AddressConcerns, skip])

# Define XOR node
xor = OperatorPOWL(operator=Operator.XOR, children=[GuideSelection, skip])

# Define root node
root = StrictPartialOrder(nodes=[ReceiveInquiry, loop, xor, ProvideQuote, PlaceOrder, RecordOrder, SendConfirmation])

# Define order of execution
root.order.add_edge(ReceiveInquiry, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, ProvideQuote)
root.order.add_edge(ProvideQuote, PlaceOrder)
root.order.add_edge(PlaceOrder, RecordOrder)
root.order.add_edge(RecordOrder, SendConfirmation)