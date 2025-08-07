import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their exact names
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Press_Cheese = Transition(label='Press Cheese')
Salt_Application = Transition(label='Salt Application')
Controlled_Aging = Transition(label='Controlled Aging')
Sensory_Check = Transition(label='Sensory Check')
Batch_Packaging = Transition(label='Batch Packaging')
Label_Printing = Transition(label='Label Printing')
Cold_Storage = Transition(label='Cold Storage')
Logistics_Plan = Transition(label='Logistics Plan')
Retail_Delivery = Transition(label='Retail Delivery')
Feedback_Review = Transition(label='Feedback Review')
Demand_Forecast = Transition(label='Demand Forecast')
Provenance_Track = Transition(label='Provenance Track')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    Quality_Testing,
    Milk_Pasteurize,
    Curd_Formation,
    Whey_Separation,
    Press_Cheese,
    Salt_Application,
    Controlled_Aging,
    Sensory_Check,
    Batch_Packaging,
    Label_Printing,
    Cold_Storage,
    Logistics_Plan,
    Retail_Delivery,
    Feedback_Review,
    Demand_Forecast,
    Provenance_Track
])

# Define the partial order dependencies
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Curd_Formation)
root.order.add_edge(Curd_Formation, Whey_Separation)
root.order.add_edge(Whey_Separation, Press_Cheese)
root.order.add_edge(Press_Cheese, Salt_Application)
root.order.add_edge(Salt_Application, Controlled_Aging)
root.order.add_edge(Controlled_Aging, Sensory_Check)
root.order.add_edge(Sensory_Check, Batch_Packaging)
root.order.add_edge(Batch_Packaging, Label_Printing)
root.order.add_edge(Label_Printing, Cold_Storage)
root.order.add_edge(Cold_Storage, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Retail_Delivery)
root.order.add_edge(Retail_Delivery, Feedback_Review)
root.order.add_edge(Feedback_Review, Demand_Forecast)
root.order.add_edge(Demand_Forecast, Provenance_Track)

print(root)