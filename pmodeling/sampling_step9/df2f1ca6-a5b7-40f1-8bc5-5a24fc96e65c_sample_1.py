import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define loop nodes
loop_artisan_vetting = OperatorPOWL(operator=Operator.LOOP, children=[artisan_vetting])
loop_quality_check = OperatorPOWL(operator=Operator.LOOP, children=[quality_check])

# Define exclusive choice nodes
xor_demand_forecast = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, skip])
xor_price_adjust = OperatorPOWL(operator=Operator.XOR, children=[price_adjust, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[material_sourcing, artisan_vetting, sample_review, design_finalize, batch_scheduling, loop_artisan_vetting, loop_quality_check, custom_packaging, demand_forecast, price_adjust, inventory_sync, order_processing, craft_coordination, shipment_plan, market_analysis, feedback_loop, xor_demand_forecast, xor_price_adjust, trend_monitor])
root.order.add_edge(material_sourcing, artisan_vetting)
root.order.add_edge(artisan_vetting, sample_review)
root.order.add_edge(sample_review, design_finalize)
root.order.add_edge(design_finalize, batch_scheduling)
root.order.add_edge(batch_scheduling, loop_artisan_vetting)
root.order.add_edge(batch_scheduling, loop_quality_check)
root.order.add_edge(loop_artisan_vetting, custom_packaging)
root.order.add_edge(loop_artisan_vetting, loop_quality_check)
root.order.add_edge(loop_quality_check, custom_packaging)
root.order.add_edge(custom_packaging, demand_forecast)
root.order.add_edge(custom_packaging, price_adjust)
root.order.add_edge(demand_forecast, inventory_sync)
root.order.add_edge(price_adjust, inventory_sync)
root.order.add_edge(inventory_sync, order_processing)
root.order.add_edge(order_processing, craft_coordination)
root.order.add_edge(craft_coordination, shipment_plan)
root.order.add_edge(shipment_plan, market_analysis)
root.order.add_edge(market_analysis, feedback_loop)
root.order.add_edge(feedback_loop, trend_monitor)

# Print the POWL model
print(root)