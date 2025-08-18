import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
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

# Define the control flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, artisan_vetting])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[sample_review, design_finalize])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[batch_scheduling, quality_check])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[custom_packaging, demand_forecast])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[price_adjust, inventory_sync])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[order_processing, craft_coordination])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[shipment_plan, market_analysis])
exclusive_choice_8 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, trend_monitor])

# Define the partial order
root = StrictPartialOrder(nodes=[exclusive_choice, exclusive_choice_2, exclusive_choice_3, exclusive_choice_4, exclusive_choice_5, exclusive_choice_6, exclusive_choice_7, exclusive_choice_8])
root.order.add_edge(exclusive_choice, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)