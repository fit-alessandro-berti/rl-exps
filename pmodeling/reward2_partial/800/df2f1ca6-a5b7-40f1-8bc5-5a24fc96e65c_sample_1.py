import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
sourcing = Transition(label='Material Sourcing')
vetting = Transition(label='Artisan Vetting')
review = Transition(label='Sample Review')
finalize = Transition(label='Design Finalize')
batch_scheduling = Transition(label='Batch Scheduling')
quality_check = Transition(label='Quality Check')
packaging = Transition(label='Custom Packaging')
demand_forecast = Transition(label='Demand Forecast')
price_adjust = Transition(label='Price Adjust')
inventory_sync = Transition(label='Inventory Sync')
order_processing = Transition(label='Order Processing')
coordination = Transition(label='Craft Coordination')
shipment_plan = Transition(label='Shipment Plan')
market_analysis = Transition(label='Market Analysis')
feedback_loop = Transition(label='Feedback Loop')
trend_monitor = Transition(label='Trend Monitor')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    sourcing,
    vetting,
    review,
    finalize,
    batch_scheduling,
    quality_check,
    packaging,
    demand_forecast,
    price_adjust,
    inventory_sync,
    order_processing,
    coordination,
    shipment_plan,
    market_analysis,
    feedback_loop,
    trend_monitor
])

# Define the order between transitions
root.order.add_edge(sourcing, vetting)
root.order.add_edge(vetting, review)
root.order.add_edge(review, finalize)
root.order.add_edge(finalize, batch_scheduling)
root.order.add_edge(batch_scheduling, quality_check)
root.order.add_edge(quality_check, packaging)
root.order.add_edge(packaging, demand_forecast)
root.order.add_edge(demand_forecast, price_adjust)
root.order.add_edge(price_adjust, inventory_sync)
root.order.add_edge(inventory_sync, order_processing)
root.order.add_edge(order_processing, coordination)
root.order.add_edge(coordination, shipment_plan)
root.order.add_edge(shipment_plan, market_analysis)
root.order.add_edge(market_analysis, feedback_loop)
root.order.add_edge(feedback_loop, trend_monitor)

print(root)