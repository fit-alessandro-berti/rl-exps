import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Farm_Audit = Transition(label='Farm Audit')
Milk_Testing = Transition(label='Milk Testing')
Batch_Forming = Transition(label='Batch Forming')
Curd_Cutting = Transition(label='Curd Cutting')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Aging_Control = Transition(label='Aging Control')
Quality_Check = Transition(label='Quality Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Inventory_Update = Transition(label='Inventory Update')
Order_Receiving = Transition(label='Order Receiving')
Retail_Coordination = Transition(label='Retail Coordination')
Shipping_Prep = Transition(label='Shipping Prep')
Customer_Feedback = Transition(label='Customer Feedback')
Demand_Forecast = Transition(label='Demand Forecast')
Limited_Release = Transition(label='Limited Release')

# Define silent activities
skip = SilentTransition()

# Define loops and choices
loop_farm_audit = OperatorPOWL(operator=Operator.LOOP, children=[Farm_Audit, Milk_Sourcing])
loop_milk_testing = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Testing, Batch_Forming])
loop_curd_cutting = OperatorPOWL(operator=Operator.LOOP, children=[Curd_Cutting, Molding_Cheese])
loop_salting_process = OperatorPOWL(operator=Operator.LOOP, children=[Salting_Process, Aging_Control])
loop_quality_check = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Check, Packaging_Design])
loop_inventory_update = OperatorPOWL(operator=Operator.LOOP, children=[Inventory_Update, Order_Receiving])
loop_retail_coordination = OperatorPOWL(operator=Operator.LOOP, children=[Retail_Coordination, Shipping_Prep])
loop_customer_feedback = OperatorPOWL(operator=Operator.LOOP, children=[Customer_Feedback, Demand_Forecast])
loop_limited_release = OperatorPOWL(operator=Operator.LOOP, children=[Limited_Release])

xor_demand_forecast = OperatorPOWL(operator=Operator.XOR, children=[Demand_Forecast, skip])
xor_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[Customer_Feedback, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop_farm_audit, loop_milk_testing, loop_curd_cutting, loop_salting_process, loop_quality_check, loop_inventory_update, loop_retail_coordination, loop_customer_feedback, loop_limited_release, xor_demand_forecast, xor_customer_feedback])
root.order.add_edge(loop_farm_audit, loop_milk_testing)
root.order.add_edge(loop_milk_testing, loop_curd_cutting)
root.order.add_edge(loop_curd_cutting, loop_salting_process)
root.order.add_edge(loop_salting_process, loop_quality_check)
root.order.add_edge(loop_quality_check, loop_inventory_update)
root.order.add_edge(loop_inventory_update, loop_retail_coordination)
root.order.add_edge(loop_retail_coordination, loop_customer_feedback)
root.order.add_edge(loop_customer_feedback, loop_limited_release)
root.order.add_edge(loop_limited_release, xor_demand_forecast)
root.order.add_edge(loop_limited_release, xor_customer_feedback)
root.order.add_edge(xor_demand_forecast, loop_retail_coordination)
root.order.add_edge(xor_customer_feedback, loop_retail_coordination)

# Save the root of the POWL model
root = root