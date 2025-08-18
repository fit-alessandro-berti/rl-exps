from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the loop for aging control
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_control])

# Define the exclusive choice for flavor profiling and packaging design
xor_flavor_packaging = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling, packaging_design])

# Define the partial order
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, starter_culture, coagulation, curd_cutting, whey_draining, molding_cheese, pressing_block, brining_bath, loop_aging, xor_flavor_packaging, demand_forecast, retail_outreach, customer_feedback])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_culture)
root.order.add_edge(starter_culture, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_cheese)
root.order.add_edge(molding_cheese, pressing_block)
root.order.add_edge(pressing_block, brining_bath)
root.order.add_edge(brining_bath, loop_aging)
root.order.add_edge(loop_aging, xor_flavor_packaging)
root.order.add_edge(xor_flavor_packaging, demand_forecast)
root.order.add_edge(demand_forecast, retail_outreach)
root.order.add_edge(retail_outreach, customer_feedback)