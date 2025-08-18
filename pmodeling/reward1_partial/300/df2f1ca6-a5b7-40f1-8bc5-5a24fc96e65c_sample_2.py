from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Define the loop for the core process
core_process = StrictPartialOrder(nodes=[
    material_sourcing,
    artisan_vetting,
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
core_process.order.add_edge(material_sourcing, artisan_vetting)
core_process.order.add_edge(artisan_vetting, sample_review)
core_process.order.add_edge(sample_review, design_finalize)
core_process.order.add_edge(design_finalize, batch_scheduling)
core_process.order.add_edge(batch_scheduling, quality_check)
core_process.order.add_edge(quality_check, custom_packaging)
core_process.order.add_edge(custom_packaging, demand_forecast)
core_process.order.add_edge(demand_forecast, price_adjust)
core_process.order.add_edge(price_adjust, inventory_sync)
core_process.order.add_edge(inventory_sync, order_processing)
core_process.order.add_edge(order_processing, craft_coordination)
core_process.order.add_edge(craft_coordination, shipment_plan)
core_process.order.add_edge(shipment_plan, market_analysis)
core_process.order.add_edge(market_analysis, feedback_loop)
core_process.order.add_edge(feedback_loop, trend_monitor)

# Define the overall process
root = StrictPartialOrder(nodes=[core_process])