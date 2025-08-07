import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
farm_audit    = Transition(label='Farm Audit')
milk_testing  = Transition(label='Milk Testing')
batch_forming = Transition(label='Batch Forming')
curd_cutting  = Transition(label='Curd Cutting')
molding       = Transition(label='Molding Cheese')
salting       = Transition(label='Salting Process')
aging_control = Transition(label='Aging Control')
quality_check = Transition(label='Quality Check')
packaging     = Transition(label='Packaging Design')
label_print   = Transition(label='Label Printing')
inventory     = Transition(label='Inventory Update')
order_recv    = Transition(label='Order Receiving')
retail_coord  = Transition(label='Retail Coordination')
shipping_prep = Transition(label='Shipping Prep')
customer_fb   = Transition(label='Customer Feedback')
demand_forest = Transition(label='Demand Forecast')
limited_rel   = Transition(label='Limited Release')

# Loop for seasonal milk sourcing
# Sequence: Farm Audit -> Milk Testing -> Batch Forming -> Curd Cutting -> Molding Cheese
sourcing_seq = StrictPartialOrder(nodes=[farm_audit, milk_testing, batch_forming, curd_cutting, molding])
sourcing_seq.order.add_edge(farm_audit, milk_testing)
sourcing_seq.order.add_edge(milk_testing, batch_forming)
sourcing_seq.order.add_edge(batch_forming, curd_cutting)
sourcing_seq.order.add_edge(curd_cutting, molding)

# Loop for aging control (until exit)
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, silent_transition])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    sourcing_seq,
    salting,
    quality_check,
    packaging,
    label_print,
    inventory,
    order_recv,
    retail_coord,
    shipping_prep,
    customer_fb,
    demand_forest,
    limited_rel
])

# Add edges to form the control-flow
root.order.add_edge(milk_sourcing, sourcing_seq)
root.order.add_edge(sourcing_seq, salting)
root.order.add_edge(salting, quality_check)
root.order.add_edge(quality_check, packaging)
root.order.add_edge(packaging, label_print)
root.order.add_edge(label_print, inventory)
root.order.add_edge(inventory, order_recv)
root.order.add_edge(order_recv, retail_coord)
root.order.add_edge(retail_coord, shipping_prep)
root.order.add_edge(shipping_prep, customer_fb)
root.order.add_edge(customer_fb, demand_forest)
root.order.add_edge(demand_forest, limited_rel)