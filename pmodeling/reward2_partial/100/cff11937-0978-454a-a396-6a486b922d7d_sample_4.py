import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Culture = Transition(label='Starter Culture')
Milk_Fermentation = Transition(label='Milk Fermentation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Pressing_Cheese = Transition(label='Pressing Cheese')
Cave_Aging = Transition(label='Cave Aging')
Sample_Tasting = Transition(label='Sample Tasting')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Design = Transition(label='Packaging Design')
Cold_Storage = Transition(label='Cold Storage')
Logistics_Planning = Transition(label='Logistics Planning')
Pop-up_Sales = Transition(label='Pop-up Sales')
Customer_Feedback = Transition(label='Customer Feedback')
Recipe_Adjusting = Transition(label='Recipe Adjusting')

# Define the POWL model
root = StrictPartialOrder(nodes=[Milk_Sourcing, Quality_Testing, Starter_Culture, Milk_Fermentation, Curd_Cutting, Whey_Draining, Pressing_Cheese, Cave_Aging, Sample_Tasting, Flavor_Profiling, Packaging_Design, Cold_Storage, Logistics_Planning, Pop-up_Sales, Customer_Feedback, Recipe_Adjusting])

# Define the dependencies between activities
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, Starter_Culture)
root.order.add_edge(Starter_Culture, Milk_Fermentation)
root.order.add_edge(Milk_Fermentation, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Draining)
root.order.add_edge(Whey_Draining, Pressing_Cheese)
root.order.add_edge(Pressing_Cheese, Cave_Aging)
root.order.add_edge(Cave_Aging, Sample_Tasting)
root.order.add_edge(Sample_Tasting, Flavor_Profiling)
root.order.add_edge(Flavor_Profiling, Packaging_Design)
root.order.add_edge(Packaging_Design, Cold_Storage)
root.order.add_edge(Cold_Storage, Logistics_Planning)
root.order.add_edge(Logistics_Planning, Pop-up_Sales)
root.order.add_edge(Pop-up_Sales, Customer_Feedback)
root.order.add_edge(Customer_Feedback, Recipe_Adjusting)

# Print the root of the POWL model
print(root)