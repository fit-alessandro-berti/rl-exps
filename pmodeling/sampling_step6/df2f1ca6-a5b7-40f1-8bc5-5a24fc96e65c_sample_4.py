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

# Define the partial order
root = StrictPartialOrder(nodes=[
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

# Add dependencies if needed (e.g., to specify the order of activities)
# root.order.add_edge(material_sourcing, artisan_vetting)
# root.order.add_edge(material_sourcing, sample_review)
# root.order.add_edge(material_sourcing, design_finalize)
# root.order.add_edge(material_sourcing, batch_scheduling)
# root.order.add_edge(material_sourcing, quality_check)
# root.order.add_edge(material_sourcing, custom_packaging)
# root.order.add_edge(material_sourcing, demand_forecast)
# root.order.add_edge(material_sourcing, price_adjust)
# root.order.add_edge(material_sourcing, inventory_sync)
# root.order.add_edge(material_sourcing, order_processing)
# root.order.add_edge(material_sourcing, craft_coordination)
# root.order.add_edge(material_sourcing, shipment_plan)
# root.order.add_edge(material_sourcing, market_analysis)
# root.order.add_edge(material_sourcing, feedback_loop)
# root.order.add_edge(material_sourcing, trend_monitor)

# The final POWL model is stored in the 'root' variable
print(root)