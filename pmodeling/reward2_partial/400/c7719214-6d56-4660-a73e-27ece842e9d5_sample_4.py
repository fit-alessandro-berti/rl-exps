import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    Diet_Monitoring,
    Culture_Selection,
    Milk_Pasteurize,
    Curd_Cutting,
    Whey_Draining,
    Mold_Inoculate,
    Press_Forming,
    Salt_Application,
    Aging_Setup,
    Humidity_Control,
    Flavor_Testing,
    Packaging_Design,
    Order_Processing,
    Retail_Delivery,
    Event_Coordination,
    Feedback_Review
])

# Define the partial order dependencies
root.order.add_edge(Milk_Sourcing, Diet_Monitoring)
root.order.add_edge(Diet_Monitoring, Culture_Selection)
root.order.add_edge(Culture_Selection, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Draining)
root.order.add_edge(Whey_Draining, Mold_Inoculate)
root.order.add_edge(Mold_Inoculate, Press_Forming)
root.order.add_edge(Press_Forming, Salt_Application)
root.order.add_edge(Salt_Application, Aging_Setup)
root.order.add_edge(Aging_Setup, Humidity_Control)
root.order.add_edge(Humidity_Control, Flavor_Testing)
root.order.add_edge(Flavor_Testing, Packaging_Design)
root.order.add_edge(Packaging_Design, Order_Processing)
root.order.add_edge(Order_Processing, Retail_Delivery)
root.order.add_edge(Retail_Delivery, Event_Coordination)
root.order.add_edge(Event_Coordination, Feedback_Review)

print(root)