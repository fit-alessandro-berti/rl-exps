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

# Define the process tree structure
Milk_Sourcing.next = [Diet_Monitoring, Culture_Selection]
Diet_Monitoring.next = [Culture_Selection]
Culture_Selection.next = [Milk_Pasteurize]
Milk_Pasteurize.next = [Curd_Cutting, Whey_Draining]
Curd_Cutting.next = [Mold_Inoculate]
Whey_Draining.next = [Mold_Inoculate]
Mold_Inoculate.next = [Press_Forming]
Press_Forming.next = [Salt_Application]
Salt_Application.next = [Aging_Setup]
Aging_Setup.next = [Humidity_Control]
Humidity_Control.next = [Flavor_Testing]
Flavor_Testing.next = [Packaging_Design]
Packaging_Design.next = [Order_Processing]
Order_Processing.next = [Retail_Delivery, Event_Coordination]
Retail_Delivery.next = [Feedback_Review]
Event_Coordination.next = [Feedback_Review]

# Construct the POWL model
root = StrictPartialOrder(nodes=[Milk_Sourcing, Diet_Monitoring, Culture_Selection, Milk_Pasteurize, Curd_Cutting, Whey_Draining, Mold_Inoculate, Press_Forming, Salt_Application, Aging_Setup, Humidity_Control, Flavor_Testing, Packaging_Design, Order_Processing, Retail_Delivery, Event_Coordination, Feedback_Review])

# Add dependencies (edges) to the POWL model
root.order.add_edge(Milk_Sourcing, Diet_Monitoring)
root.order.add_edge(Milk_Sourcing, Culture_Selection)
root.order.add_edge(Diet_Monitoring, Culture_Selection)
root.order.add_edge(Culture_Selection, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Curd_Cutting)
root.order.add_edge(Milk_Pasteurize, Whey_Draining)
root.order.add_edge(Whey_Draining, Mold_Inoculate)
root.order.add_edge(Mold_Inoculate, Press_Forming)
root.order.add_edge(Press_Forming, Salt_Application)
root.order.add_edge(Salt_Application, Aging_Setup)
root.order.add_edge(Aging_Setup, Humidity_Control)
root.order.add_edge(Humidity_Control, Flavor_Testing)
root.order.add_edge(Flavor_Testing, Packaging_Design)
root.order.add_edge(Packaging_Design, Order_Processing)
root.order.add_edge(Order_Processing, Retail_Delivery)
root.order.add_edge(Order_Processing, Event_Coordination)
root.order.add_edge(Retail_Delivery, Feedback_Review)
root.order.add_edge(Event_Coordination, Feedback_Review)