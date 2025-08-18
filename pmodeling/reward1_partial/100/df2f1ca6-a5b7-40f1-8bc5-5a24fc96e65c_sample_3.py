import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their labels
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

# Define the silent transition (tau label)
skip = SilentTransition()

# Define the exclusive choice between Sample Review and Skip
xor_sample = OperatorPOWL(operator=Operator.XOR, children=[sample_review, skip])

# Define the exclusive choice between Design Finalize and Skip
xor_design = OperatorPOWL(operator=Operator.XOR, children=[design_finalize, skip])

# Define the exclusive choice between Quality Check and Skip
xor_quality = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])

# Define the exclusive choice between Custom Packaging and Skip
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[custom_packaging, skip])

# Define the exclusive choice between Inventory Sync and Skip
xor_inventory = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, skip])

# Define the exclusive choice between Order Processing and Skip
xor_order = OperatorPOWL(operator=Operator.XOR, children=[order_processing, skip])

# Define the exclusive choice between Craft Coordination and Skip
xor_craft = OperatorPOWL(operator=Operator.XOR, children=[craft_coordination, skip])

# Define the exclusive choice between Shipment Plan and Skip
xor_shipment = OperatorPOWL(operator=Operator.XOR, children=[shipment_plan, skip])

# Define the exclusive choice between Market Analysis and Skip
xor_market = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])

# Define the exclusive choice between Feedback Loop and Skip
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, skip])

# Define the exclusive choice between Trend Monitor and Skip
xor_trend = OperatorPOWL(operator=Operator.XOR, children=[trend_monitor, skip])

# Define the loop between Material Sourcing and Artisan Vetting
loop = OperatorPOWL(operator=Operator.LOOP, children=[artisan_vetting, material_sourcing])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    loop,
    xor_sample,
    xor_design,
    xor_quality,
    xor_packaging,
    xor_inventory,
    xor_order,
    xor_craft,
    xor_shipment,
    xor_market,
    xor_feedback,
    xor_trend
])

# Define the edges in the partial order
root.order.add_edge(loop, xor_sample)
root.order.add_edge(loop, xor_design)
root.order.add_edge(loop, xor_quality)
root.order.add_edge(loop, xor_packaging)
root.order.add_edge(loop, xor_inventory)
root.order.add_edge(loop, xor_order)
root.order.add_edge(loop, xor_craft)
root.order.add_edge(loop, xor_shipment)
root.order.add_edge(loop, xor_market)
root.order.add_edge(loop, xor_feedback)
root.order.add_edge(loop, xor_trend)

# Print the root to verify the model
print(root)