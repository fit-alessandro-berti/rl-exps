import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
material_sourcing = Transition(label='Material Sourcing')
artisan_vetting = Transition(label='Artisan Vetting')
sample_review = Transition(label='Sample Review')
design_finalize = Transition(label='Design Finalize')
batch_scheduling = Transition(label='Batch Scheduling')
quality_check = Transition(label='Quality Check')
custom_packaging = Transition(label='Custom Packaging')
demand_forecast = Transition(label='Demand Forecast')
price_adjust = Transition(label='Price Adjust')
inventory_sync = Transition(label='Inventory Sync')
order_processing = Transition(label='Order Processing')
craft_coordination = Transition(label='Craft Coordination')
shipment_plan = Transition(label='Shipment Plan')
market_analysis = Transition(label='Market Analysis')
feedback_loop = Transition(label='Feedback Loop')
trend_monitor = Transition(label='Trend Monitor')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, artisan_vetting])

# Define partial order
partial_order = StrictPartialOrder(nodes=[
    exclusive_choice,
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

# Define dependencies
partial_order.order.add_edge(exclusive_choice, sample_review)
partial_order.order.add_edge(sample_review, design_finalize)
partial_order.order.add_edge(design_finalize, batch_scheduling)
partial_order.order.add_edge(batch_scheduling, quality_check)
partial_order.order.add_edge(quality_check, custom_packaging)
partial_order.order.add_edge(custom_packaging, demand_forecast)
partial_order.order.add_edge(demand_forecast, price_adjust)
partial_order.order.add_edge(price_adjust, inventory_sync)
partial_order.order.add_edge(inventory_sync, order_processing)
partial_order.order.add_edge(order_processing, craft_coordination)
partial_order.order.add_edge(craft_coordination, shipment_plan)
partial_order.order.add_edge(shipment_plan, market_analysis)
partial_order.order.add_edge(market_analysis, feedback_loop)
partial_order.order.add_edge(feedback_loop, trend_monitor)

# Set root
root = partial_order