from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their corresponding labels
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Selection = Transition(label='Culture Selection')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Mold_Inoculate = Transition(label='Mold Inoculate')
Cheese_Pressing = Transition(label='Cheese Pressing')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Flavor_Testing = Transition(label='Flavor Testing')
Packaging_Design = Transition(label='Packaging Design')
Label_Approval = Transition(label='Label Approval')
Order_Forecast = Transition(label='Order Forecast')
Regulation_Audit = Transition(label='Regulation Audit')
Waste_Recycling = Transition(label='Waste Recycling')
Market_Delivery = Transition(label='Market Delivery')
Customer_Feedback = Transition(label='Customer Feedback')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    Culture_Selection,
    Milk_Pasteurize,
    Curd_Formation,
    Whey_Separation,
    Mold_Inoculate,
    Cheese_Pressing,
    Aging_Setup,
    Humidity_Control,
    Flavor_Testing,
    Packaging_Design,
    Label_Approval,
    Order_Forecast,
    Regulation_Audit,
    Waste_Recycling,
    Market_Delivery,
    Customer_Feedback
])

# Define the order dependencies
root.order.add_edge(Milk_Sourcing, Culture_Selection)
root.order.add_edge(Culture_Selection, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Curd_Formation)
root.order.add_edge(Curd_Formation, Whey_Separation)
root.order.add_edge(Whey_Separation, Mold_Inoculate)
root.order.add_edge(Mold_Inoculate, Cheese_Pressing)
root.order.add_edge(Cheese_Pressing, Aging_Setup)
root.order.add_edge(Aging_Setup, Humidity_Control)
root.order.add_edge(Humidity_Control, Flavor_Testing)
root.order.add_edge(Flavor_Testing, Packaging_Design)
root.order.add_edge(Packaging_Design, Label_Approval)
root.order.add_edge(Label_Approval, Order_Forecast)
root.order.add_edge(Order_Forecast, Regulation_Audit)
root.order.add_edge(Regulation_Audit, Waste_Recycling)
root.order.add_edge(Waste_Recycling, Market_Delivery)
root.order.add_edge(Market_Delivery, Customer_Feedback)

# Print the root of the POWL model
print(root)