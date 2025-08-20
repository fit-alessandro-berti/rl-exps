import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
ReceiveCustomerInquiry = Transition(label='Receive customer inquiry')
CollectCustomerInformation = Transition(label='Collect customer information')
AddressCustomerConcernsOrQuestions = Transition(label='Address customer concerns or questions')
GuideCustomerInSelectingProductOrService = Transition(label='Guide customer in selecting product/service')
ProvideQuote = Transition(label='Provide quote')
PlaceOrder = Transition(label='Place order')
RecordOrderInSystem = Transition(label='Record order in system')
SendOrderConfirmationToCustomer = Transition(label='Send order confirmation to customer')

# Define a loop for the sales process
SalesProcess = OperatorPOWL(operator=Operator.LOOP, children=[
    GuideCustomerInSelectingProductOrService,
    ProvideQuote,
    PlaceOrder,
    RecordOrderInSystem,
    SendOrderConfirmationToCustomer
])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[ReceiveCustomerInquiry, CollectCustomerInformation, AddressCustomerConcernsOrQuestions, SalesProcess])
root.order.add_edge(ReceiveCustomerInquiry, CollectCustomerInformation)
root.order.add_edge(CollectCustomerInformation, AddressCustomerConcernsOrQuestions)
root.order.add_edge(AddressCustomerConcernsOrQuestions, SalesProcess)