import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, farm_audit, milk_testing, batch_forming, curd_cutting, molding_cheese, salting_process, aging_control, quality_check])
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_printing, inventory_update])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[retail_coordination, shipping_prep])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[order_receiving, customer_feedback])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, limited_release])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)

# Print the root
print(root)