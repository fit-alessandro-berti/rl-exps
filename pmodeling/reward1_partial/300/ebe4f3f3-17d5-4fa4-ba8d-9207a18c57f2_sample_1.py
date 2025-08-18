import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define partial order structure
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    farm_audit,
    milk_testing,
    batch_forming,
    curd_cutting,
    molding_cheese,
    salting_process,
    aging_control,
    quality_check,
    packaging_design,
    label_printing,
    inventory_update,
    order_receiving,
    retail_coordination,
    shipping_prep,
    customer_feedback,
    demand_forecast,
    limited_release
])

# Define dependencies
root.order.add_edge(milk_sourcing, farm_audit)
root.order.add_edge(farm_audit, milk_testing)
root.order.add_edge(milk_testing, batch_forming)
root.order.add_edge(batch_forming, curd_cutting)
root.order.add_edge(curd_cutting, molding_cheese)
root.order.add_edge(molding_cheese, salting_process)
root.order.add_edge(salting_process, aging_control)
root.order.add_edge(aging_control, quality_check)
root.order.add_edge(quality_check, packaging_design)
root.order.add_edge(packaging_design, label_printing)
root.order.add_edge(label_printing, inventory_update)
root.order.add_edge(inventory_update, order_receiving)
root.order.add_edge(order_receiving, retail_coordination)
root.order.add_edge(retail_coordination, shipping_prep)
root.order.add_edge(shipping_prep, customer_feedback)
root.order.add_edge(customer_feedback, demand_forecast)
root.order.add_edge(demand_forecast, limited_release)

print(root)