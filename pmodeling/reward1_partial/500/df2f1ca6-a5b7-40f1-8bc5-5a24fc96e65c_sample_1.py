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

skip = SilentTransition()

# Define the control flow operators
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, artisan_vetting])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[sample_review, design_finalize])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[batch_scheduling, quality_check])
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[custom_packaging, demand_forecast])
exclusive_choice5 = OperatorPOWL(operator=Operator.XOR, children=[price_adjust, inventory_sync])
exclusive_choice6 = OperatorPOWL(operator=Operator.XOR, children=[order_processing, craft_coordination])
exclusive_choice7 = OperatorPOWL(operator=Operator.XOR, children=[shipment_plan, market_analysis])
exclusive_choice8 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, trend_monitor])

# Define the partial order
root = StrictPartialOrder(nodes=[exclusive_choice1, exclusive_choice2, exclusive_choice3, exclusive_choice4, exclusive_choice5, exclusive_choice6, exclusive_choice7, exclusive_choice8])
root.order.add_edge(exclusive_choice1, exclusive_choice2)
root.order.add_edge(exclusive_choice2, exclusive_choice3)
root.order.add_edge(exclusive_choice3, exclusive_choice4)
root.order.add_edge(exclusive_choice4, exclusive_choice5)
root.order.add_edge(exclusive_choice5, exclusive_choice6)
root.order.add_edge(exclusive_choice6, exclusive_choice7)
root.order.add_edge(exclusive_choice7, exclusive_choice8)

# Print the root
print(root)