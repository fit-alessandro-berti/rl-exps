import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their respective labels
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Selection = Transition(label='Culture Selection')
Milk_Testing = Transition(label='Milk Testing')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Aging_Setup = Transition(label='Aging Setup')
Env_Monitoring = Transition(label='Env Monitoring')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Design = Transition(label='Packaging Design')
Blockchain_Entry = Transition(label='Blockchain Entry')
Quality_Audit = Transition(label='Quality Audit')
Retail_Sync = Transition(label='Retail Sync')
Transport_Prep = Transition(label='Transport Prep')
Delivery_Tracking = Transition(label='Delivery Tracking')
Customer_Feedback = Transition(label='Customer Feedback')

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model structure
root = StrictPartialOrder(nodes=[
    Milk_Sourcing, 
    Culture_Selection, 
    Milk_Testing, 
    Curd_Formation, 
    Whey_Separation, 
    Molding_Cheese, 
    Salting_Process, 
    Aging_Setup, 
    Env_Monitoring, 
    Flavor_Profiling, 
    Packaging_Design, 
    Blockchain_Entry, 
    Quality_Audit, 
    Retail_Sync, 
    Transport_Prep, 
    Delivery_Tracking, 
    Customer_Feedback
])

# Define the partial order dependencies
root.order.add_edge(Milk_Sourcing, Culture_Selection)
root.order.add_edge(Milk_Sourcing, Milk_Testing)
root.order.add_edge(Culture_Selection, Curd_Formation)
root.order.add_edge(Milk_Testing, Curd_Formation)
root.order.add_edge(Curd_Formation, Whey_Separation)
root.order.add_edge(Whey_Separation, Molding_Cheese)
root.order.add_edge(Molding_Cheese, Salting_Process)
root.order.add_edge(Salting_Process, Aging_Setup)
root.order.add_edge(Aging_Setup, Env_Monitoring)
root.order.add_edge(Env_Monitoring, Flavor_Profiling)
root.order.add_edge(Flavor_Profiling, Packaging_Design)
root.order.add_edge(Packaging_Design, Blockchain_Entry)
root.order.add_edge(Blockchain_Entry, Quality_Audit)
root.order.add_edge(Quality_Audit, Retail_Sync)
root.order.add_edge(Retail_Sync, Transport_Prep)
root.order.add_edge(Transport_Prep, Delivery_Tracking)
root.order.add_edge(Delivery_Tracking, Customer_Feedback)

# Return the root of the POWL model
return root