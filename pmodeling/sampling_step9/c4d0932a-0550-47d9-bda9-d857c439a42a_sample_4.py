import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define silent transitions
skip = SilentTransition()

# Define the loops and choices
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, starter_culture, coagulation, curd_cutting, whey_draining, molding_cheese, pressing_block, brining_bath, aging_control, flavor_profiling])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, flavor_profiling, packaging_design])
retail_loop = OperatorPOWL(operator=Operator.LOOP, children=[retail_outreach, customer_feedback])

# Define the partial order
root = StrictPartialOrder(nodes=[quality_loop, aging_loop, retail_loop])
root.order.add_edge(quality_loop, aging_loop)
root.order.add_edge(aging_loop, retail_loop)

# Print the POWL model
print(root)