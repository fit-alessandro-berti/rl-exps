import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
sourcing = Transition(label='Material Sourcing')
vetting = Transition(label='Artisan Vetting')
review = Transition(label='Sample Review')
finalize = Transition(label='Design Finalize')
batch = Transition(label='Batch Scheduling')
quality = Transition(label='Quality Check')
packaging = Transition(label='Custom Packaging')
demand = Transition(label='Demand Forecast')
price = Transition(label='Price Adjust')
inventory = Transition(label='Inventory Sync')
order = Transition(label='Order Processing')
coordination = Transition(label='Craft Coordination')
shipment = Transition(label='Shipment Plan')
analysis = Transition(label='Market Analysis')
feedback = Transition(label='Feedback Loop')
monitor = Transition(label='Trend Monitor')

# Define silent transitions
skip_sourcing = SilentTransition()
skip_vetting = SilentTransition()
skip_review = SilentTransition()
skip_finalize = SilentTransition()
skip_batch = SilentTransition()
skip_quality = SilentTransition()
skip_packaging = SilentTransition()
skip_demand = SilentTransition()
skip_price = SilentTransition()
skip_inventory = SilentTransition()
skip_order = SilentTransition()
skip_coordination = SilentTransition()
skip_shipment = SilentTransition()
skip_analysis = SilentTransition()
skip_feedback = SilentTransition()
skip_monitor = SilentTransition()

# Define the process flow
root = StrictPartialOrder(nodes=[
    sourcing,
    vetting,
    review,
    finalize,
    batch,
    quality,
    packaging,
    demand,
    price,
    inventory,
    order,
    coordination,
    shipment,
    analysis,
    feedback,
    monitor
])

# Define the dependencies between activities
root.order.add_edge(sourcing, vetting)
root.order.add_edge(vetting, review)
root.order.add_edge(review, finalize)
root.order.add_edge(finalize, batch)
root.order.add_edge(batch, quality)
root.order.add_edge(quality, packaging)
root.order.add_edge(packaging, demand)
root.order.add_edge(demand, price)
root.order.add_edge(price, inventory)
root.order.add_edge(inventory, order)
root.order.add_edge(order, coordination)
root.order.add_edge(coordination, shipment)
root.order.add_edge(shipment, analysis)
root.order.add_edge(analysis, feedback)
root.order.add_edge(feedback, monitor)