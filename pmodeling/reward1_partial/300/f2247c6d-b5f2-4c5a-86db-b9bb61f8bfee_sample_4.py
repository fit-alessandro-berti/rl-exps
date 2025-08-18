import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for the refurbishment process
refurbishment_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Receive_Returns,
    Inspect_Items,
    Segregate_Stock,
    Wipe_Data,
    Harvest_Parts,
    Refurbish_Units,
    Test_Quality,
    Recycle_Waste,
    Dispose_Defects,
    Update_Inventory,
    Coordinate_Resale,
    Process_Refunds,
    Analyze_Patterns,
    Improve_Design,
    Report_Metrics
])

# Define the XOR for inventory updates and coordinate resale
inventory_xor = OperatorPOWL(operator=Operator.XOR, children=[
    Update_Inventory,
    Coordinate_Resale
])

# Define the root model
root = StrictPartialOrder(nodes=[refurbishment_loop, inventory_xor])
root.order.add_edge(refurbishment_loop, inventory_xor)

print(root)