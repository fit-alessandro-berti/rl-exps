import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the process structure using POWL operators
milk_sourcing_to_quality_testing = OperatorPOWL(operator=Operator.PO, children=[milk_sourcing, quality_testing])
quality_testing_to_starter_culture = OperatorPOWL(operator=Operator.PO, children=[quality_testing, starter_culture])
starter_culture_to_coagulation = OperatorPOWL(operator=Operator.PO, children=[starter_culture, coagulation])
coagulation_to_curd_cutting = OperatorPOWL(operator=Operator.PO, children=[coagulation, curd_cutting])
curd_cutting_to_whey_draining = OperatorPOWL(operator=Operator.PO, children=[curd_cutting, whey_draining])
whey_draining_to_molding_cheese = OperatorPOWL(operator=Operator.PO, children=[whey_draining, molding_cheese])
molding_cheese_to_pressing_block = OperatorPOWL(operator=Operator.PO, children=[molding_cheese, pressing_block])
pressing_block_to_brining_bath = OperatorPOWL(operator=Operator.PO, children=[pressing_block, brining_bath])
brining_bath_to_aging_control = OperatorPOWL(operator=Operator.PO, children=[brining_bath, aging_control])
aging_control_to_flavor_profiling = OperatorPOWL(operator=Operator.PO, children=[aging_control, flavor_profiling])
flavor_profiling_to_packaging_design = OperatorPOWL(operator=Operator.PO, children=[flavor_profiling, packaging_design])
packaging_design_to_demand_forecast = OperatorPOWL(operator=Operator.PO, children=[packaging_design, demand_forecast])
demand_forecast_to_retail_outreach = OperatorPOWL(operator=Operator.PO, children=[demand_forecast, retail_outreach])
retail_outreach_to_customer_feedback = OperatorPOWL(operator=Operator.PO, children=[retail_outreach, customer_feedback])

# Create the root StrictPartialOrder
root = StrictPartialOrder(nodes=[milk_sourcing_to_quality_testing, quality_testing_to_starter_culture, starter_culture_to_coagulation, coagulation_to_curd_cutting, curd_cutting_to_whey_draining, whey_draining_to_molding_cheese, molding_cheese_to_pressing_block, pressing_block_to_brining_bath, brining_bath_to_aging_control, aging_control_to_flavor_profiling, flavor_profiling_to_packaging_design, packaging_design_to_demand_forecast, demand_forecast_to_retail_outreach, retail_outreach_to_customer_feedback])

# Add edges to represent the flow of activities
root.order.add_edge(milk_sourcing_to_quality_testing, quality_testing_to_starter_culture)
root.order.add_edge(quality_testing_to_starter_culture, starter_culture_to_coagulation)
root.order.add_edge(starter_culture_to_coagulation, coagulation_to_curd_cutting)
root.order.add_edge(coagulation_to_curd_cutting, curd_cutting_to_whey_draining)
root.order.add_edge(curd_cutting_to_whey_draining, whey_draining_to_molding_cheese)
root.order.add_edge(whey_draining_to_molding_cheese, molding_cheese_to_pressing_block)
root.order.add_edge(molding_cheese_to_pressing_block, pressing_block_to_brining_bath)
root.order.add_edge(pressing_block_to_brining_bath, brining_bath_to_aging_control)
root.order.add_edge(brining_bath_to_aging_control, aging_control_to_flavor_profiling)
root.order.add_edge(aging_control_to_flavor_profiling, flavor_profiling_to_packaging_design)
root.order.add_edge(flavor_profiling_to_packaging_design, packaging_design_to_demand_forecast)
root.order.add_edge(packaging_design_to_demand_forecast, demand_forecast_to_retail_outreach)
root.order.add_edge(demand_forecast_to_retail_outreach, retail_outreach_to_customer_feedback)