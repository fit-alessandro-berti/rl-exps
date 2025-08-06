import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
# Material Sourcing
sourcing = Transition(label='Material Sourcing')

# Artisan Vetting
vetting = Transition(label='Artisan Vetting')

# Sample Review
sample_review = Transition(label='Sample Review')

# Design Finalize
design_finalize = Transition(label='Design Finalize')

# Batch Scheduling
batch_scheduling = Transition(label='Batch Scheduling')

# Quality Check
quality_check = Transition(label='Quality Check')

# Custom Packaging
custom_packaging = Transition(label='Custom Packaging')

# Demand Forecast
demand_forecast = Transition(label='Demand Forecast')

# Price Adjust
price_adjust = Transition(label='Price Adjust')

# Inventory Sync
inventory_sync = Transition(label='Inventory Sync')

# Order Processing
order_processing = Transition(label='Order Processing')

# Craft Coordination
craft_coordination = Transition(label='Craft Coordination')

# Shipment Plan
shipment_plan = Transition(label='Shipment Plan')

# Market Analysis
market_analysis = Transition(label='Market Analysis')

# Feedback Loop
feedback_loop = Transition(label='Feedback Loop')

# Trend Monitor
trend_monitor = Transition(label='Trend Monitor')

# Define the partial order
root = StrictPartialOrder(nodes=[
    sourcing,
    vetting,
    sample_review,
    design_finalize,
    batch_scheduling,
    quality_check,
    custom_packaging,
    demand_forecast,
    price_adjust,
    inventory_sync,
    order_processing,
    craft_coordination,
    shipment_plan,
    market_analysis,
    feedback_loop,
    trend_monitor
])

# Define the dependencies between activities
root.order.add_edge(sourcing, vetting)
root.order.add_edge(vetting, sample_review)
root.order.add_edge(sample_review, design_finalize)
root.order.add_edge(design_finalize, batch_scheduling)
root.order.add_edge(batch_scheduling, quality_check)
root.order.add_edge(quality_check, custom_packaging)
root.order.add_edge(custom_packaging, demand_forecast)
root.order.add_edge(demand_forecast, price_adjust)
root.order.add_edge(price_adjust, inventory_sync)
root.order.add_edge(inventory_sync, order_processing)
root.order.add_edge(order_processing, craft_coordination)
root.order.add_edge(craft_coordination, shipment_plan)
root.order.add_edge(shipment_plan, market_analysis)
root.order.add_edge(market_analysis, feedback_loop)
root.order.add_edge(feedback_loop, trend_monitor)

# Print the root POWL model
print(root)