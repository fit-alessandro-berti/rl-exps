import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) as objects
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

# Define the partial order graph
root = StrictPartialOrder(
    nodes=[
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
    ],
    order={
        Milk_Sourcing: Culture_Selection,
        Culture_Selection: Milk_Pasteurize,
        Milk_Pasteurize: Curd_Formation,
        Curd_Formation: Whey_Separation,
        Whey_Separation: Mold_Inoculate,
        Mold_Inoculate: Cheese_Pressing,
        Cheese_Pressing: Aging_Setup,
        Aging_Setup: Humidity_Control,
        Humidity_Control: Flavor_Testing,
        Flavor_Testing: Packaging_Design,
        Packaging_Design: Label_Approval,
        Label_Approval: Order_Forecast,
        Order_Forecast: Regulation_Audit,
        Regulation_Audit: Waste_Recycling,
        Waste_Recycling: Market_Delivery,
        Market_Delivery: Customer_Feedback
    }
)

print(root)