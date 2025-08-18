import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_cheese = Transition(label='Molding Cheese')
pressing_block = Transition(label='Pressing Block')
brining_bath = Transition(label='Brining Bath')
aging_control = Transition(label='Aging Control')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
demand_forecast = Transition(label='Demand Forecast')
retail_outreach = Transition(label='Retail Outreach')
customer_feedback = Transition(label='Customer Feedback')

# Define the process tree
process_tree = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    starter_culture,
    coagulation,
    curd_cutting,
    whey_draining,
    molding_cheese,
    pressing_block,
    brining_bath,
    aging_control,
    flavor_profiling,
    packaging_design,
    demand_forecast,
    retail_outreach,
    customer_feedback
])

# Add the dependencies
process_tree.order.add_edge(milk_sourcing, quality_testing)
process_tree.order.add_edge(quality_testing, starter_culture)
process_tree.order.add_edge(starter_culture, coagulation)
process_tree.order.add_edge(coagulation, curd_cutting)
process_tree.order.add_edge(curd_cutting, whey_draining)
process_tree.order.add_edge(whey_draining, molding_cheese)
process_tree.order.add_edge(molding_cheese, pressing_block)
process_tree.order.add_edge(pressing_block, brining_bath)
process_tree.order.add_edge(brining_bath, aging_control)
process_tree.order.add_edge(aging_control, flavor_profiling)
process_tree.order.add_edge(flavor_profiling, packaging_design)
process_tree.order.add_edge(packaging_design, demand_forecast)
process_tree.order.add_edge(demand_forecast, retail_outreach)
process_tree.order.add_edge(retail_outreach, customer_feedback)

# Save the result in the variable 'root'
root = process_tree