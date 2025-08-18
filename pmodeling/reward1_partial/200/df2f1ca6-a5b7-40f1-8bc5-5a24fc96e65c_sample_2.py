from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop_artisan = OperatorPOWL(operator=Operator.LOOP, children=[artisan_vetting, sample_review, design_finalize, batch_scheduling, quality_check])
xor_demand = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, price_adjust, inventory_sync])
xor_craft = OperatorPOWL(operator=Operator.XOR, children=[order_processing, craft_coordination, shipment_plan])
xor_market = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, feedback_loop, trend_monitor])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_artisan, xor_demand, xor_craft, xor_market])
root.order.add_edge(loop_artisan, xor_demand)
root.order.add_edge(loop_artisan, xor_craft)
root.order.add_edge(loop_artisan, xor_market)
root.order.add_edge(xor_demand, xor_craft)
root.order.add_edge(xor_demand, xor_market)
root.order.add_edge(xor_craft, xor_market)

# Return the root
root = root