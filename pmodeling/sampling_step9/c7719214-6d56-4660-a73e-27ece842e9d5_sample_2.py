import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Milk_Sourcing = Transition(label='Milk Sourcing')
Diet_Monitoring = Transition(label='Diet Monitoring')
Culture_Selection = Transition(label='Culture Selection')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Mold_Inoculate = Transition(label='Mold Inoculate')
Press_Forming = Transition(label='Press Forming')
Salt_Application = Transition(label='Salt Application')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Flavor_Testing = Transition(label='Flavor Testing')
Packaging_Design = Transition(label='Packaging Design')
Order_Processing = Transition(label='Order Processing')
Retail_Delivery = Transition(label='Retail Delivery')
Event_Coordination = Transition(label='Event Coordination')
Feedback_Review = Transition(label='Feedback Review')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Sourcing, Diet_Monitoring, Culture_Selection, Milk_Pasteurize, Curd_Cutting, Whey_Draining, Mold_Inoculate, Press_Forming, Salt_Application, Aging_Setup, Humidity_Control, Flavor_Testing, Packaging_Design, Order_Processing, Retail_Delivery, Event_Coordination, Feedback_Review])
xor = OperatorPOWL(operator=Operator.XOR, children=[Retail_Delivery, Event_Coordination])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)