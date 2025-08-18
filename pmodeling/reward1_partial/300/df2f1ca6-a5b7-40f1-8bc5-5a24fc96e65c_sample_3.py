import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the operators for the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[sample_review, artisan_vetting])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[batch_scheduling, quality_check])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[custom_packaging, inventory_sync])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[order_processing, craft_coordination])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[shipment_plan, market_analysis])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, price_adjust])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, trend_monitor])

# Define the loop for the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[material_sourcing, loop])
root.order.add_edge(material_sourcing, loop)

print(root)