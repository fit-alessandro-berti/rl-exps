import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing    = Transition(label='Milk Sourcing')
quality_testing  = Transition(label='Quality Testing')
starter_culture  = Transition(label='Starter Culture')
coagulation      = Transition(label='Coagulation')
curd_cutting     = Transition(label='Curd Cutting')
whey_draining    = Transition(label='Whey Draining')
molding_cheese   = Transition(label='Molding Cheese')
pressing_block   = Transition(label='Pressing Block')
brining_bath     = Transition(label='Brining Bath')
aging_control    = Transition(label='Aging Control')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
demand_forecast  = Transition(label='Demand Forecast')
retail_outreach  = Transition(label='Retail Outreach')
customer_feedback= Transition(label='Customer Feedback')

# Silent transition for loop continuation
skip = SilentTransition()

# Loop for continuous aging and profiling
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_control, flavor_profiling]
)

# Choice between packaging or skip (no packaging for niche markets)
packaging_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[packaging_design, skip]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    starter_culture,
    coagulation,
    curd_cutting,
    whey_draining,
    molding_cheese,
    pressing_block,
    brining_bath,
    aging_loop,
    packaging_choice,
    demand_forecast,
    retail_outreach,
    customer_feedback
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_culture)
root.order.add_edge(starter_culture, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_cheese)
root.order.add_edge(molding_cheese, pressing_block)
root.order.add_edge(pressing_block, brining_bath)
root.order.add_edge(brining_bath, aging_loop)
root.order.add_edge(aging_loop, packaging_choice)
root.order.add_edge(packaging_choice, demand_forecast)
root.order.add_edge(demand_forecast, retail_outreach)
root.order.add_edge(retail_outreach, customer_feedback)

# The feedback loop closes the process
root.order.add_edge(customer_feedback, milk_sourcing)