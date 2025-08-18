import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Create the process structure
material_sourcing_to_artisan_vetting = OperatorPOWL(operator=Operator.AND, children=[material_sourcing, artisan_vetting])
artisan_vetting_to_sample_review = OperatorPOWL(operator=Operator.AND, children=[artisan_vetting, sample_review])
sample_review_to_design_finalize = OperatorPOWL(operator=Operator.AND, children=[sample_review, design_finalize])
design_finalize_to_batch_scheduling = OperatorPOWL(operator=Operator.AND, children=[design_finalize, batch_scheduling])
batch_scheduling_to_quality_check = OperatorPOWL(operator=Operator.AND, children=[batch_scheduling, quality_check])
quality_check_to_custom_packaging = OperatorPOWL(operator=Operator.AND, children=[quality_check, custom_packaging])
custom_packaging_to_demand_forecast = OperatorPOWL(operator=Operator.AND, children=[custom_packaging, demand_forecast])
demand_forecast_to_price_adjust = OperatorPOWL(operator=Operator.AND, children=[demand_forecast, price_adjust])
price_adjust_to_inventory_sync = OperatorPOWL(operator=Operator.AND, children=[price_adjust, inventory_sync])
inventory_sync_to_order_processing = OperatorPOWL(operator=Operator.AND, children=[inventory_sync, order_processing])
order_processing_to_craft_coordination = OperatorPOWL(operator=Operator.AND, children=[order_processing, craft_coordination])
craft_coordination_to_shipment_plan = OperatorPOWL(operator=Operator.AND, children=[craft_coordination, shipment_plan])
shipment_plan_to_market_analysis = OperatorPOWL(operator=Operator.AND, children=[shipment_plan, market_analysis])
market_analysis_to_feedback_loop = OperatorPOWL(operator=Operator.AND, children=[market_analysis, feedback_loop])
feedback_loop_to_trend_monitor = OperatorPOWL(operator=Operator.AND, children=[feedback_loop, trend_monitor])

# Define the partial order relationships
root = StrictPartialOrder(nodes=[
    material_sourcing_to_artisan_vetting,
    artisan_vetting_to_sample_review,
    sample_review_to_design_finalize,
    design_finalize_to_batch_scheduling,
    batch_scheduling_to_quality_check,
    quality_check_to_custom_packaging,
    custom_packaging_to_demand_forecast,
    demand_forecast_to_price_adjust,
    price_adjust_to_inventory_sync,
    inventory_sync_to_order_processing,
    order_processing_to_craft_coordination,
    craft_coordination_to_shipment_plan,
    shipment_plan_to_market_analysis,
    market_analysis_to_feedback_loop,
    feedback_loop_to_trend_monitor
])

# Add edges based on the dependencies
root.order.add_edge(material_sourcing_to_artisan_vetting, artisan_vetting_to_sample_review)
root.order.add_edge(artisan_vetting_to_sample_review, sample_review_to_design_finalize)
root.order.add_edge(sample_review_to_design_finalize, design_finalize_to_batch_scheduling)
root.order.add_edge(design_finalize_to_batch_scheduling, batch_scheduling_to_quality_check)
root.order.add_edge(batch_scheduling_to_quality_check, quality_check_to_custom_packaging)
root.order.add_edge(quality_check_to_custom_packaging, custom_packaging_to_demand_forecast)
root.order.add_edge(custom_packaging_to_demand_forecast, demand_forecast_to_price_adjust)
root.order.add_edge(demand_forecast_to_price_adjust, price_adjust_to_inventory_sync)
root.order.add_edge(price_adjust_to_inventory_sync, inventory_sync_to_order_processing)
root.order.add_edge(inventory_sync_to_order_processing, order_processing_to_craft_coordination)
root.order.add_edge(order_processing_to_craft_coordination, craft_coordination_to_shipment_plan)
root.order.add_edge(craft_coordination_to_shipment_plan, shipment_plan_to_market_analysis)
root.order.add_edge(shipment_plan_to_market_analysis, market_analysis_to_feedback_loop)
root.order.add_edge(market_analysis_to_feedback_loop, feedback_loop_to_trend_monitor)

# Print the root node
print(root)