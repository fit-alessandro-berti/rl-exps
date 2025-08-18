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

# Define the workflow
root = StrictPartialOrder(
    nodes=[
        Milk_Selection,
        Quality_Testing,
        Milk_Pasteurize,
        Cheese_Crafting,
        Controlled_Aging,
        Sensory_Review,
        Custom_Packaging,
        Label_Printing,
        Export_Licensing,
        Documentation_Prep,
        Customs_Clearance,
        Cold_Shipping,
        Delivery_Tracking,
        Feedback_Review,
        Market_Analysis
    ],
    order=[
        (Milk_Selection, Quality_Testing),
        (Quality_Testing, Milk_Pasteurize),
        (Milk_Pasteurize, Cheese_Crafting),
        (Cheese_Crafting, Controlled_Aging),
        (Controlled_Aging, Sensory_Review),
        (Sensory_Review, Custom_Packaging),
        (Custom_Packaging, Label_Printing),
        (Label_Printing, Export_Licensing),
        (Export_Licensing, Documentation_Prep),
        (Documentation_Prep, Customs_Clearance),
        (Customs_Clearance, Cold_Shipping),
        (Cold_Shipping, Delivery_Tracking),
        (Delivery_Tracking, Feedback_Review),
        (Feedback_Review, Market_Analysis)
    ]
)