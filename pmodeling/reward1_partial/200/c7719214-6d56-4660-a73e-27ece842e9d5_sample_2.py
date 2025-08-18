import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the loop nodes for aging and event coordination
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Aging_Setup, Humidity_Control])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Event_Coordination, Feedback_Review])

# Define the exclusive choice for packaging and order processing
xor = OperatorPOWL(operator=Operator.XOR, children=[Packaging_Design, Order_Processing])

# Define the root POWL model
root = StrictPartialOrder(nodes=[Milk_Sourcing, Diet_Monitoring, Culture_Selection, Milk_Pasteurize, Curd_Cutting, Whey_Draining, Mold_Inoculate, Press_Forming, Salt_Application, loop1, loop2, xor])
root.order.add_edge(Milk_Sourcing, Diet_Monitoring)
root.order.add_edge(Diet_Monitoring, Culture_Selection)
root.order.add_edge(Culture_Selection, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Draining)
root.order.add_edge(Whey_Draining, Mold_Inoculate)
root.order.add_edge(Mold_Inoculate, Press_Forming)
root.order.add_edge(Press_Forming, Salt_Application)
root.order.add_edge(Salt_Application, loop1)
root.order.add_edge(loop1, Aging_Setup)
root.order.add_edge(Aging_Setup, Humidity_Control)
root.order.add_edge(Humidity_Control, loop2)
root.order.add_edge(loop2, Event_Coordination)
root.order.add_edge(Event_Coordination, Feedback_Review)
root.order.add_edge(Feedback_Review, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor)
root.order.add_edge(xor, Packaging_Design)
root.order.add_edge(Packaging_Design, Order_Processing)
root.order.add_edge(Order_Processing, Retail_Delivery)

print(root)