import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.algo.filtering.powl.powl import apply as powl_apply

Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Culture = Transition(label='Starter Culture')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Cheese = Transition(label='Molding Cheese')
Pressing_Block = Transition(label='Pressing Block')
Brining_Bath = Transition(label='Brining Bath')
Aging_Control = Transition(label='Aging Control')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Design = Transition(label='Packaging Design')
Demand_Forecast = Transition(label='Demand Forecast')
Retail_Outreach = Transition(label='Retail Outreach')
Customer_Feedback = Transition(label='Customer Feedback')

# Create a partial order
root = StrictPartialOrder(nodes=[
    Milk_Sourcing, Quality_Testing, Starter_Culture, Coagulation, Curd_Cutting, Whey_Draining,
    Molding_Cheese, Pressing_Block, Brining_Bath, Aging_Control, Flavor_Profiling, Packaging_Design,
    Demand_Forecast, Retail_Outreach, Customer_Feedback
])

# Define the dependencies
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, Starter_Culture)
root.order.add_edge(Starter_Culture, Coagulation)
root.order.add_edge(Coagulation, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Draining)
root.order.add_edge(Whey_Draining, Molding_Cheese)
root.order.add_edge(Molding_Cheese, Pressing_Block)
root.order.add_edge(Pressing_Block, Brining_Bath)
root.order.add_edge(Brining_Bath, Aging_Control)
root.order.add_edge(Aging_Control, Flavor_Profiling)
root.order.add_edge(Flavor_Profiling, Packaging_Design)
root.order.add_edge(Packaging_Design, Demand_Forecast)
root.order.add_edge(Demand_Forecast, Retail_Outreach)
root.order.add_edge(Retail_Outreach, Customer_Feedback)

# Apply the POWL model
filtered_powl = powl_apply(root, None, None)

# Get the root of the filtered POWL model
root = filtered_powl.root