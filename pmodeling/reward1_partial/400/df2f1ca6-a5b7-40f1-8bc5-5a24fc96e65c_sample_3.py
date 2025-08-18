import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define relationships
xor_artisan = OperatorPOWL(operator=Operator.XOR, children=[artisan_vetting, material_sourcing])
xor_design = OperatorPOWL(operator=Operator.XOR, children=[sample_review, design_finalize])
xor_scheduling = OperatorPOWL(operator=Operator.XOR, children=[batch_scheduling, quality_check])
xor_pricing = OperatorPOWL(operator=Operator.XOR, children=[price_adjust, demand_forecast])
xor_inventory = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, craft_coordination])
xor_order = OperatorPOWL(operator=Operator.XOR, children=[order_processing, shipment_plan])
xor_market = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, feedback_loop])
xor_trend = OperatorPOWL(operator=Operator.XOR, children=[trend_monitor, market_analysis])

# Define root model
root = StrictPartialOrder(nodes=[xor_artisan, xor_design, xor_scheduling, xor_pricing, xor_inventory, xor_order, xor_market, xor_trend])
root.order.add_edge(xor_artisan, xor_design)
root.order.add_edge(xor_design, xor_scheduling)
root.order.add_edge(xor_scheduling, xor_pricing)
root.order.add_edge(xor_pricing, xor_inventory)
root.order.add_edge(xor_inventory, xor_order)
root.order.add_edge(xor_order, xor_market)
root.order.add_edge(xor_market, xor_trend)

print(root)