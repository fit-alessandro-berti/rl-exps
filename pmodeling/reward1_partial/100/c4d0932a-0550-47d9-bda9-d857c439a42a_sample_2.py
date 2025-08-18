import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for aging control
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, demand_forecast, retail_outreach, customer_feedback])

# Define the exclusive choice for flavor profiling
xor_flavor = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling, packaging_design])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, starter_culture, coagulation, curd_cutting, whey_draining, molding_cheese, pressing_block, brining_bath, loop_aging, xor_flavor])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_culture)
root.order.add_edge(starter_culture, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_cheese)
root.order.add_edge(molding_cheese, pressing_block)
root.order.add_edge(pressing_block, brining_bath)
root.order.add_edge(brining_bath, aging_control)
root.order.add_edge(aging_control, demand_forecast)
root.order.add_edge(demand_forecast, retail_outreach)
root.order.add_edge(retail_outreach, customer_feedback)
root.order.add_edge(customer_feedback, aging_control)
root.order.add_edge(aging_control, loop_aging)
root.order.add_edge(loop_aging, xor_flavor)
root.order.add_edge(xor_flavor, flavor_profiling)
root.order.add_edge(xor_flavor, packaging_design)

print(root)