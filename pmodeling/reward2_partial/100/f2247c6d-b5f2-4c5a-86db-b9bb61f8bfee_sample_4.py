import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
Receive_Returns = Transition(label='Receive Returns')
Inspect_Items = Transition(label='Inspect Items')
Segregate_Stock = Transition(label='Segregate Stock')
Wipe_Data = Transition(label='Wipe Data')
Harvest_Parts = Transition(label='Harvest Parts')
Refurbish_Units = Transition(label='Refurbish Units')
Test_Quality = Transition(label='Test Quality')
Recycle_Waste = Transition(label='Recycle Waste')
Dispose_Defects = Transition(label='Dispose Defects')
Update_Inventory = Transition(label='Update Inventory')
Coordinate_Resale = Transition(label='Coordinate Resale')
Process_Refunds = Transition(label='Process Refunds')
Analyze_Patterns = Transition(label='Analyze Patterns')
Improve_Design = Transition(label='Improve Design')
Report_Metrics = Transition(label='Report Metrics')

# Define the partial order
root = StrictPartialOrder(nodes=[Receive_Returns, Inspect_Items, Segregate_Stock, Wipe_Data, Harvest_Parts, Refurbish_Units, Test_Quality, Recycle_Waste, Dispose_Defects, Update_Inventory, Coordinate_Resale, Process_Refunds, Analyze_Patterns, Improve_Design, Report_Metrics])

# Add the edges to the partial order
root.order.add_edge(Receive_Returns, Inspect_Items)
root.order.add_edge(Inspect_Items, Segregate_Stock)
root.order.add_edge(Segregate_Stock, Wipe_Data)
root.order.add_edge(Wipe_Data, Harvest_Parts)
root.order.add_edge(Harvest_Parts, Refurbish_Units)
root.order.add_edge(Refurbish_Units, Test_Quality)
root.order.add_edge(Test_Quality, Recycle_Waste)
root.order.add_edge(Recycle_Waste, Dispose_Defects)
root.order.add_edge(Dispose_Defects, Update_Inventory)
root.order.add_edge(Update_Inventory, Coordinate_Resale)
root.order.add_edge(Coordinate_Resale, Process_Refunds)
root.order.add_edge(Process_Refunds, Analyze_Patterns)
root.order.add_edge(Analyze_Patterns, Improve_Design)
root.order.add_edge(Improve_Design, Report_Metrics)