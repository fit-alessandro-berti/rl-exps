import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define nodes
quality_testing_node = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, milk_sourcing])
coagulation_node = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, quality_testing_node])
curd_cutting_node = OperatorPOWL(operator=Operator.XOR, children=[coagulation, coagulation_node])
whey_draining_node = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, curd_cutting_node])
molding_cheese_node = OperatorPOWL(operator=Operator.XOR, children=[whey_draining, whey_draining_node])
pressing_block_node = OperatorPOWL(operator=Operator.XOR, children=[molding_cheese, molding_cheese_node])
brining_bath_node = OperatorPOWL(operator=Operator.XOR, children=[pressing_block, pressing_block_node])
aging_control_node = OperatorPOWL(operator=Operator.XOR, children=[brining_bath, brining_bath_node])
flavor_profiling_node = OperatorPOWL(operator=Operator.XOR, children=[aging_control, aging_control_node])
packaging_design_node = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling, flavor_profiling_node])
demand_forecast_node = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, packaging_design_node])
retail_outreach_node = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, demand_forecast_node])
customer_feedback_node = OperatorPOWL(operator=Operator.XOR, children=[retail_outreach, retail_outreach_node])

# Define root
root = StrictPartialOrder(nodes=[quality_testing_node, demand_forecast_node, customer_feedback_node])
root.order.add_edge(quality_testing_node, demand_forecast_node)
root.order.add_edge(demand_forecast_node, customer_feedback_node)

print(root)