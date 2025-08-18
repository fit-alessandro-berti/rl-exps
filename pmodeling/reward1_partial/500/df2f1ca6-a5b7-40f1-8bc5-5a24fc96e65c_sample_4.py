import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
sourcing = Transition(label='Material Sourcing')
vetting = Transition(label='Artisan Vetting')
sample_review = Transition(label='Sample Review')
finalize_design = Transition(label='Design Finalize')
batch_schedule = Transition(label='Batch Scheduling')
quality_check = Transition(label='Quality Check')
packaging = Transition(label='Custom Packaging')
forecast = Transition(label='Demand Forecast')
price_adjust = Transition(label='Price Adjust')
inventory_sync = Transition(label='Inventory Sync')
order_processing = Transition(label='Order Processing')
craft_coordination = Transition(label='Craft Coordination')
shipment_plan = Transition(label='Shipment Plan')
market_analysis = Transition(label='Market Analysis')
feedback_loop = Transition(label='Feedback Loop')
trend_monitor = Transition(label='Trend Monitor')

# Define the POWL operators
xor_artisan = OperatorPOWL(operator=Operator.XOR, children=[vetting, sourcing])
xor_design = OperatorPOWL(operator=Operator.XOR, children=[finalize_design, sample_review])
xor_production = OperatorPOWL(operator=Operator.XOR, children=[batch_schedule, quality_check])
xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[packaging, order_processing])
xor_forecast = OperatorPOWL(operator=Operator.XOR, children=[forecast, market_analysis])
xor_price = OperatorPOWL(operator=Operator.XOR, children=[price_adjust, inventory_sync])
xor_craft = OperatorPOWL(operator=Operator.XOR, children=[craft_coordination, shipment_plan])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, trend_monitor])

# Define the POWL model
root = StrictPartialOrder(nodes=[xor_artisan, xor_design, xor_production, xor_delivery, xor_forecast, xor_price, xor_craft, xor_feedback])
root.order.add_edge(xor_artisan, xor_design)
root.order.add_edge(xor_design, xor_production)
root.order.add_edge(xor_production, xor_delivery)
root.order.add_edge(xor_delivery, xor_forecast)
root.order.add_edge(xor_forecast, xor_price)
root.order.add_edge(xor_price, xor_craft)
root.order.add_edge(xor_craft, xor_feedback)