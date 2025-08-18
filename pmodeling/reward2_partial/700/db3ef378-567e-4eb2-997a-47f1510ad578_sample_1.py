import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the artisan cheese production process
# Raw milk collection from specialized breeds
Milk_Collection = Transition(label='Milk Collection')

# Preparation of microbial culture
Culture_Prep = Transition(label='Culture Prep')

# Formation of curd
Curd_Formation = Transition(label='Curd Formation')

# Separation of whey
Whey_Separation = Transition(label='Whey Separation')

# Molding of cheese
Molding_Cheese = Transition(label='Molding Cheese')

# Salting process
Salting_Process = Transition(label='Salting Process')

# Initial aging
Initial_Aging = Transition(label='Initial Aging')

# Humidity control
Humidity_Control = Transition(label='Humidity Control')

# Temperature check
Temperature_Check = Transition(label='Temperature Check')

# Flavor testing
Flavor_Testing = Transition(label='Flavor Testing')

# Final aging
Final_Aging = Transition(label='Final Aging')

# Packaging artisanal
Packaging_Artisanal = Transition(label='Packaging Artisanal')

# Label printing
Label_Printing = Transition(label='Label Printing')

# Inventory audit
Inventory_Audit = Transition(label='Inventory Audit')

# Order fulfillment
Order_Fulfillment = Transition(label='Order Fulfillment')

# Subscription setup
Subscription_Setup = Transition(label='Subscription Setup')

# Event marketing
Event_Marketing = Transition(label='Event Marketing')

# Define the process flow as a StrictPartialOrder
root = StrictPartialOrder(nodes=[
    Milk_Collection,
    Culture_Prep,
    Curd_Formation,
    Whey_Separation,
    Molding_Cheese,
    Salting_Process,
    Initial_Aging,
    Humidity_Control,
    Temperature_Check,
    Flavor_Testing,
    Final_Aging,
    Packaging_Artisanal,
    Label_Printing,
    Inventory_Audit,
    Order_Fulfillment,
    Subscription_Setup,
    Event_Marketing
])

# Define the dependencies (partial order)
root.order.add_edge(Milk_Collection, Culture_Prep)
root.order.add_edge(Culture_Prep, Curd_Formation)
root.order.add_edge(Curd_Formation, Whey_Separation)
root.order.add_edge(Whey_Separation, Molding_Cheese)
root.order.add_edge(Molding_Cheese, Salting_Process)
root.order.add_edge(Salting_Process, Initial_Aging)
root.order.add_edge(Initial_Aging, Humidity_Control)
root.order.add_edge(Humidity_Control, Temperature_Check)
root.order.add_edge(Temperature_Check, Flavor_Testing)
root.order.add_edge(Flavor_Testing, Final_Aging)
root.order.add_edge(Final_Aging, Packaging_Artisanal)
root.order.add_edge(Packaging_Artisanal, Label_Printing)
root.order.add_edge(Label_Printing, Inventory_Audit)
root.order.add_edge(Inventory_Audit, Order_Fulfillment)
root.order.add_edge(Order_Fulfillment, Subscription_Setup)
root.order.add_edge(Subscription_Setup, Event_Marketing)