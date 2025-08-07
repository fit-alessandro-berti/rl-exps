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

# Define the partial order
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