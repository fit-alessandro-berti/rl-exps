import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing   = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
coagulation     = Transition(label='Coagulation')
curd_cutting    = Transition(label='Curd Cutting')
whey_draining   = Transition(label='Whey Draining')
molding_cheese  = Transition(label='Molding Cheese')
pressing_block  = Transition(label='Pressing Block')
brining_bath    = Transition(label='Brining Bath')
aging_control   = Transition(label='Aging Control')
flavor_profiling= Transition(label='Flavor Profiling')
packaging_design= Transition(label='Packaging Design')
demand_forecast = Transition(label='Demand Forecast')
retail_outreach = Transition(label='Retail Outreach')
customer_feedback=Transition(label='Customer Feedback')

# Define the aging sub-process as a partial order
aging_sub = StrictPartialOrder(nodes=[aging_control, flavor_profiling])
# No order edges => these two can run in parallel

# Define the feedback loop: after packaging, do feedback, then either exit or do the aging sub-process again
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, customer_feedback])

# Assemble the overall process as a strict partial order
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
    aging_sub,
    demand_forecast,
    retail_outreach,
    feedback_loop
])

# Sequence the initial milk‐to‐packaging activities
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_culture)
root.order.add_edge(starter_culture, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_cheese)
root.order.add_edge(molding_cheese, pressing_block)
root.order.add_edge(pressing_block, brining_bath)
root.order.add_edge(brining_bath, aging_sub)

# After aging, sequence forecasting, then outreach
root.order.add_edge(aging_sub, demand_forecast)
root.order.add_edge(demand_forecast, retail_outreach)

# Finally, connect the feedback loop after packaging
root.order.add_edge(packaging_design, feedback_loop)