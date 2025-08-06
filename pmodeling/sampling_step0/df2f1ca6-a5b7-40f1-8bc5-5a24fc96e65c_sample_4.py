import pm4py

# Define the activities
material_sourcing = pm4py.objects.powl.obj.Transition(label='Material Sourcing')
artisan_vetting = pm4py.objects.powl.obj.Transition(label='Artisan Vetting')
sample_review = pm4py.objects.powl.obj.Transition(label='Sample Review')
design_finalize = pm4py.objects.powl.obj.Transition(label='Design Finalize')
batch_scheduling = pm4py.objects.powl.obj.Transition(label='Batch Scheduling')
quality_check = pm4py.objects.powl.obj.Transition(label='Quality Check')
custom_packaging = pm4py.objects.powl.obj.Transition(label='Custom Packaging')
demand_forecast = pm4py.objects.powl.obj.Transition(label='Demand Forecast')
price_adjust = pm4py.objects.powl.obj.Transition(label='Price Adjust')
inventory_sync = pm4py.objects.powl.obj.Transition(label='Inventory Sync')
order_processing = pm4py.objects.powl.obj.Transition(label='Order Processing')
craft_coordination = pm4py.objects.powl.obj.Transition(label='Craft Coordination')
shipment_plan = pm4py.objects.powl.obj.Transition(label='Shipment Plan')
market_analysis = pm4py.objects.powl.obj.Transition(label='Market Analysis')
feedback_loop = pm4py.objects.powl.obj.Transition(label='Feedback Loop')
trend_monitor = pm4py.objects.powl.obj.Transition(label='Trend Monitor')

# Define the exclusive choice for sample review and design finalize
xor = pm4py.objects.powl.obj.OperatorPOWL(
    operator=pm4py.objects.powl.obj.Operator.XOR,
    children=[sample_review, design_finalize]
)

# Define the loop for quality check, custom packaging, inventory sync, order processing, craft coordination, and shipment plan
loop = pm4py.objects.powl.obj.OperatorPOWL(
    operator=pm4py.objects.powl.obj.Operator.LOOP,
    children=[quality_check, custom_packaging, inventory_sync, order_processing, craft_coordination, shipment_plan]
)

# Define the partial order
root = pm4py.objects.powl.obj.StrictPartialOrder(
    nodes=[loop, xor]
)
root.order.add_edge(loop, xor)

# Print the root node for verification
print(root)