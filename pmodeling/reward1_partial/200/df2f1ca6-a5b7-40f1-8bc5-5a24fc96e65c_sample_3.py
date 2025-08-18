import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define exclusive choice (XOR) for demand forecasting and market analysis
xor_demand_analysis = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, market_analysis])

# Define loop for price adjustment and feedback loop
loop_price_feedback = OperatorPOWL(operator=Operator.LOOP, children=[price_adjust, feedback_loop])

# Define partial order for the process
root = StrictPartialOrder(nodes=[
    material_sourcing,
    artisan_vetting,
    sample_review,
    design_finalize,
    batch_scheduling,
    quality_check,
    custom_packaging,
    xor_demand_analysis,
    inventory_sync,
    order_processing,
    craft_coordination,
    shipment_plan,
    loop_price_feedback,
    trend_monitor
])

# Define edges in the partial order
root.order.add_edge(material_sourcing, artisan_vetting)
root.order.add_edge(artisan_vetting, sample_review)
root.order.add_edge(sample_review, design_finalize)
root.order.add_edge(design_finalize, batch_scheduling)
root.order.add_edge(batch_scheduling, quality_check)
root.order.add_edge(quality_check, custom_packaging)
root.order.add_edge(custom_packaging, xor_demand_analysis)
root.order.add_edge(xor_demand_analysis, inventory_sync)
root.order.add_edge(inventory_sync, order_processing)
root.order.add_edge(order_processing, craft_coordination)
root.order.add_edge(craft_coordination, shipment_plan)
root.order.add_edge(shipment_plan, loop_price_feedback)
root.order.add_edge(loop_price_feedback, trend_monitor)

# Optionally, you can visualize the model using pm4py
# pm4py.view_process_tree(root)