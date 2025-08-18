import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sourcing = Transition(label='Material Sourcing')
vetting = Transition(label='Artisan Vetting')
review = Transition(label='Sample Review')
finalize = Transition(label='Design Finalize')
batch = Transition(label='Batch Scheduling')
quality = Transition(label='Quality Check')
packaging = Transition(label='Custom Packaging')
demand = Transition(label='Demand Forecast')
price = Transition(label='Price Adjust')
sync = Transition(label='Inventory Sync')
order = Transition(label='Order Processing')
coordination = Transition(label='Craft Coordination')
shipment = Transition(label='Shipment Plan')
market = Transition(label='Market Analysis')
feedback = Transition(label='Feedback Loop')
trend = Transition(label='Trend Monitor')

# Define partial order
root = StrictPartialOrder(nodes=[
    sourcing, vetting, review, finalize, batch, quality, packaging, demand, price, sync, order, coordination, shipment, market, feedback, trend
])

# Define dependencies
root.order.add_edge(sourcing, vetting)
root.order.add_edge(vetting, review)
root.order.add_edge(review, finalize)
root.order.add_edge(finalize, batch)
root.order.add_edge(batch, quality)
root.order.add_edge(quality, packaging)
root.order.add_edge(packaging, demand)
root.order.add_edge(demand, price)
root.order.add_edge(price, sync)
root.order.add_edge(sync, order)
root.order.add_edge(order, coordination)
root.order.add_edge(coordination, shipment)
root.order.add_edge(shipment, market)
root.order.add_edge(market, feedback)
root.order.add_edge(feedback, trend)

print(root)