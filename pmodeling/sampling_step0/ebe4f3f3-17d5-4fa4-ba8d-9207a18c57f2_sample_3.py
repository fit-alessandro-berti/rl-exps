import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
farm_audit = Transition(label='Farm Audit')
milk_testing = Transition(label='Milk Testing')
batch_forming = Transition(label='Batch Forming')
curd_cutting = Transition(label='Curd Cutting')
molding_cheese = Transition(label='Molding Cheese')
salting_process = Transition(label='Salting Process')
aging_control = Transition(label='Aging Control')
quality_check = Transition(label='Quality Check')
packaging_design = Transition(label='Packaging Design')
label_printing = Transition(label='Label Printing')
inventory_update = Transition(label='Inventory Update')
order_receiving = Transition(label='Order Receiving')
retail_coordination = Transition(label='Retail Coordination')
shipping_prep = Transition(label='Shipping Prep')
customer_feedback = Transition(label='Customer Feedback')
demand_forecast = Transition(label='Demand Forecast')
limited_release = Transition(label='Limited Release')

# Define the silent activities
skip_milk_sourcing = SilentTransition()
skip_farm_audit = SilentTransition()
skip_milk_testing = SilentTransition()
skip_batch_forming = SilentTransition()
skip_curd_cutting = SilentTransition()
skip_molding_cheese = SilentTransition()
skip_salting_process = SilentTransition()
skip_aging_control = SilentTransition()
skip_quality_check = SilentTransition()
skip_inventory_update = SilentTransition()
skip_order_receiving = SilentTransition()
skip_retail_coordination = SilentTransition()
skip_shipping_prep = SilentTransition()
skip_demand_forecast = SilentTransition()
skip_limited_release = SilentTransition()

# Define the operators
choice_milk_sourcing = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, skip_milk_sourcing])
choice_farm_audit = OperatorPOWL(operator=Operator.XOR, children=[farm_audit, skip_farm_audit])
choice_milk_testing = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, skip_milk_testing])
choice_batch_forming = OperatorPOWL(operator=Operator.XOR, children=[batch_forming, skip_batch_forming])
choice_curd_cutting = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, skip_curd_cutting])
choice_molding_cheese = OperatorPOWL(operator=Operator.XOR, children=[molding_cheese, skip_molding_cheese])
choice_salting_process = OperatorPOWL(operator=Operator.XOR, children=[salting_process, skip_salting_process])
choice_aging_control = OperatorPOWL(operator=Operator.XOR, children=[aging_control, skip_aging_control])
choice_quality_check = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip_quality_check])
choice_inventory_update = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, skip_inventory_update])
choice_order_receiving = OperatorPOWL(operator=Operator.XOR, children=[order_receiving, skip_order_receiving])
choice_retail_coordination = OperatorPOWL(operator=Operator.XOR, children=[retail_coordination, skip_retail_coordination])
choice_shipping_prep = OperatorPOWL(operator=Operator.XOR, children=[shipping_prep, skip_shipping_prep])
choice_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip_customer_feedback])
choice_demand_forecast = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, skip_demand_forecast])
choice_limited_release = OperatorPOWL(operator=Operator.XOR, children=[limited_release, skip_limited_release])

# Define the loop for milk sourcing
loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[choice_milk_sourcing, choice_farm_audit])

# Define the loop for milk testing
loop_milk_testing = OperatorPOWL(operator=Operator.LOOP, children=[choice_milk_testing, choice_batch_forming])

# Define the loop for curd cutting
loop_curd_cutting = OperatorPOWL(operator=Operator.LOOP, children=[choice_curd_cutting, choice_molding_cheese])

# Define the loop for salting process
loop_salting_process = OperatorPOWL(operator=Operator.LOOP, children=[choice_salting_process, choice_aging_control])

# Define the loop for quality check
loop_quality_check = OperatorPOWL(operator=Operator.LOOP, children=[choice_quality_check, choice_inventory_update])

# Define the loop for order receiving
loop_order_receiving = OperatorPOWL(operator=Operator.LOOP, children=[choice_order_receiving, choice_retail_coordination])

# Define the loop for retail coordination
loop_retail_coordination = OperatorPOWL(operator=Operator.LOOP, children=[choice_retail_coordination, choice_shipping_prep])

# Define the loop for shipping preparation
loop_shipping_prep = OperatorPOWL(operator=Operator.LOOP, children=[choice_shipping_prep, choice_customer_feedback])

# Define the loop for customer feedback
loop_customer_feedback = OperatorPOWL(operator=Operator.LOOP, children=[choice_customer_feedback, choice_demand_forecast])

# Define the loop for demand forecast
loop_demand_forecast = OperatorPOWL(operator=Operator.LOOP, children=[choice_demand_forecast, choice_limited_release])

# Define the root
root = StrictPartialOrder(nodes=[
    loop_milk_sourcing,
    loop_milk_testing,
    loop_curd_cutting,
    loop_salting_process,
    loop_quality_check,
    loop_order_receiving,
    loop_retail_coordination,
    loop_shipping_prep,
    loop_customer_feedback,
    loop_demand_forecast,
    choice_milk_sourcing,
    choice_farm_audit,
    choice_milk_testing,
    choice_batch_forming,
    choice_curd_cutting,
    choice_molding_cheese,
    choice_salting_process,
    choice_aging_control,
    choice_quality_check,
    choice_inventory_update,
    choice_order_receiving,
    choice_retail_coordination,
    choice_shipping_prep,
    choice_customer_feedback,
    choice_demand_forecast,
    choice_limited_release,
])

# Add edges
root.order.add_edge(loop_milk_sourcing, choice_milk_sourcing)
root.order.add_edge(loop_milk_sourcing, choice_farm_audit)
root.order.add_edge(choice_milk_sourcing, choice_milk_testing)
root.order.add_edge(choice_milk_testing, choice_batch_forming)
root.order.add_edge(choice_batch_forming, choice_curd_cutting)
root.order.add_edge(choice_curd_cutting, choice_molding_cheese)
root.order.add_edge(choice_molding_cheese, choice_salting_process)
root.order.add_edge(choice_salting_process, choice_aging_control)
root.order.add_edge(choice_aging_control, choice_quality_check)
root.order.add_edge(choice_quality_check, choice_inventory_update)
root.order.add_edge(choice_inventory_update, choice_order_receiving)
root.order.add_edge(choice_order_receiving, choice_retail_coordination)
root.order.add_edge(choice_retail_coordination, choice_shipping_prep)
root.order.add_edge(choice_shipping_prep, choice_customer_feedback)
root.order.add_edge(choice_customer_feedback, choice_demand_forecast)
root.order.add_edge(choice_demand_forecast, choice_limited_release)

# Print the root
print(root)