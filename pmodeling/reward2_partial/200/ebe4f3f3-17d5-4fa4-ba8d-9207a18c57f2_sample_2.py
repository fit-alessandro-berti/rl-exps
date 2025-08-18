from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, farm_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, batch_forming])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, molding_cheese])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[salting_process, aging_control])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, packaging_design])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[label_printing, inventory_update])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[order_receiving, retail_coordination])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[shipping_prep, customer_feedback])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, limited_release])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)

print(root)