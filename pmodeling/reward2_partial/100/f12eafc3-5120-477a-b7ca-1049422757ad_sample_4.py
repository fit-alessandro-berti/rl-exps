import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Milk_Selection = Transition(label='Milk Selection')
Quality_Testing = Transition(label='Quality Testing')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Cheese_Crafting = Transition(label='Cheese Crafting')
Controlled_Aging = Transition(label='Controlled Aging')
Sensory_Review = Transition(label='Sensory Review')
Custom_Packaging = Transition(label='Custom Packaging')
Label_Printing = Transition(label='Label Printing')
Export_Licensing = Transition(label='Export Licensing')
Documentation_Prep = Transition(label='Documentation Prep')
Customs_Clearance = Transition(label='Customs Clearance')
Cold_Shipping = Transition(label='Cold Shipping')
Delivery_Tracking = Transition(label='Delivery Tracking')
Feedback_Review = Transition(label='Feedback Review')
Market_Analysis = Transition(label='Market Analysis')

# Define the process
root = StrictPartialOrder(nodes=[Milk_Selection, Quality_Testing, Milk_Pasteurize, Cheese_Crafting, Controlled_Aging, Sensory_Review, Custom_Packaging, Label_Printing, Export_Licensing, Documentation_Prep, Customs_Clearance, Cold_Shipping, Delivery_Tracking, Feedback_Review, Market_Analysis])

# Define the dependencies
root.order.add_edge(Milk_Selection, Quality_Testing)
root.order.add_edge(Quality_Testing, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Cheese_Crafting)
root.order.add_edge(Cheese_Crafting, Controlled_Aging)
root.order.add_edge(Controlled_Aging, Sensory_Review)
root.order.add_edge(Sensory_Review, Custom_Packaging)
root.order.add_edge(Custom_Packaging, Label_Printing)
root.order.add_edge(Label_Printing, Export_Licensing)
root.order.add_edge(Export_Licensing, Documentation_Prep)
root.order.add_edge(Documentation_Prep, Customs_Clearance)
root.order.add_edge(Customs_Clearance, Cold_Shipping)
root.order.add_edge(Cold_Shipping, Delivery_Tracking)
root.order.add_edge(Delivery_Tracking, Feedback_Review)
root.order.add_edge(Feedback_Review, Market_Analysis)

print(root)