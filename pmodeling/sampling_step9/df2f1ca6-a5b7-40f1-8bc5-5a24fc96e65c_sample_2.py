import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Material_Sourcing = Transition(label='Material Sourcing')
Artisan_Vetting = Transition(label='Artisan Vetting')
Sample_Review = Transition(label='Sample Review')
Design_Finalize = Transition(label='Design Finalize')
Batch_Scheduling = Transition(label='Batch Scheduling')
Quality_Check = Transition(label='Quality Check')
Custom_Packaging = Transition(label='Custom Packaging')
Demand_Forecast = Transition(label='Demand Forecast')
Price_Adjust = Transition(label='Price Adjust')
Inventory_Sync = Transition(label='Inventory Sync')
Order_Processing = Transition(label='Order Processing')
Craft_Coordination = Transition(label='Craft Coordination')
Shipment_Plan = Transition(label='Shipment Plan')
Market_Analysis = Transition(label='Market Analysis')
Feedback_Loop = Transition(label='Feedback Loop')
Trend_Monitor = Transition(label='Trend Monitor')

skip = SilentTransition()
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Material_Sourcing, Artisan_Vetting, Sample_Review, Design_Finalize, Batch_Scheduling, Quality_Check, Custom_Packaging])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Demand_Forecast, Price_Adjust, Inventory_Sync, Order_Processing, Craft_Coordination, Shipment_Plan, Market_Analysis])
xor = OperatorPOWL(operator=Operator.XOR, children=[Trend_Monitor, Feedback_Loop])

root = StrictPartialOrder(nodes=[loop1, loop2, xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)

# Save the final result in the variable 'root'