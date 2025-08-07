import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the root partial order with the defined activities
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

# The order of activities is assumed to be in the sequence given above
# If there is a specific dependency, it would be added here using root.order.add_edge(source, target)
# For example, if material_sourcing depends on another activity, root.order.add_edge(another_activity, material_sourcing)

# The 'root' variable now holds the POWL model for the described process