from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (Receive_Returns, Inspect_Items),
        (Inspect_Items, Segregate_Stock),
        (Segregate_Stock, Wipe_Data),
        (Wipe_Data, Harvest_Parts),
        (Harvest_Parts, Refurbish_Units),
        (Refurbish_Units, Test_Quality),
        (Test_Quality, Recycle_Waste),
        (Recycle_Waste, Dispose_Defects),
        (Dispose_Defects, Update_Inventory),
        (Update_Inventory, Coordinate_Resale),
        (Coordinate_Resale, Process_Refunds),
        (Process_Refunds, Analyze_Patterns),
        (Analyze_Patterns, Improve_Design),
        (Improve_Design, Report_Metrics)
    ]
)