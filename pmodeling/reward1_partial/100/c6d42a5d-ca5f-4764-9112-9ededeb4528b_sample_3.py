import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Soil_Sample = Transition(label='Soil Sample')
Crop_Select = Transition(label='Crop Select')
Irrigation_Plan = Transition(label='Irrigation Plan')
Permit_Apply = Transition(label='Permit Apply')
Material_Order = Transition(label='Material Order')
Bed_Install = Transition(label='Bed Install')
Pest_Control = Transition(label='Pest Control')
Solar_Setup = Transition(label='Solar Setup')
Staff_Train = Transition(label='Staff Train')
Market_Outreach = Transition(label='Market Outreach')
System_Setup = Transition(label='System Setup')
Supplier_Contact = Transition(label='Supplier Contact')
Health_Monitor = Transition(label='Health Monitor')

# Define silent transitions for skipping
Skip1 = SilentTransition()
Skip2 = SilentTransition()

# Define exclusive choices for activities
Site_Survey_Choice = OperatorPOWL(operator=Operator.XOR, children=[Site_Survey, Skip1])
Load_Test_Choice = OperatorPOWL(operator=Operator.XOR, children=[Load_Test, Skip2])
Soil_Sample_Choice = OperatorPOWL(operator=Operator.XOR, children=[Soil_Sample, Skip2])
Crop_Select_Choice = OperatorPOWL(operator=Operator.XOR, children=[Crop_Select, Skip2])
Irrigation_Plan_Choice = OperatorPOWL(operator=Operator.XOR, children=[Irrigation_Plan, Skip2])
Permit_Apply_Choice = OperatorPOWL(operator=Operator.XOR, children=[Permit_Apply, Skip2])
Material_Order_Choice = OperatorPOWL(operator=Operator.XOR, children=[Material_Order, Skip2])
Bed_Install_Choice = OperatorPOWL(operator=Operator.XOR, children=[Bed_Install, Skip2])
Pest_Control_Choice = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, Skip2])
Solar_Setup_Choice = OperatorPOWL(operator=Operator.XOR, children=[Solar_Setup, Skip2])
Staff_Train_Choice = OperatorPOWL(operator=Operator.XOR, children=[Staff_Train, Skip2])
Market_Outreach_Choice = OperatorPOWL(operator=Operator.XOR, children=[Market_Outreach, Skip2])
System_Setup_Choice = OperatorPOWL(operator=Operator.XOR, children=[System_Setup, Skip2])
Supplier_Contact_Choice = OperatorPOWL(operator=Operator.XOR, children=[Supplier_Contact, Skip2])
Health_Monitor_Choice = OperatorPOWL(operator=Operator.XOR, children=[Health_Monitor, Skip2])

# Define loops for activities
Site_Survey_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey_Choice, Permit_Apply_Choice])
Load_Test_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Load_Test_Choice, Permit_Apply_Choice])
Soil_Sample_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Soil_Sample_Choice, Permit_Apply_Choice])
Crop_Select_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Select_Choice, Permit_Apply_Choice])
Irrigation_Plan_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Irrigation_Plan_Choice, Permit_Apply_Choice])
Material_Order_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Material_Order_Choice, Permit_Apply_Choice])
Bed_Install_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Bed_Install_Choice, Permit_Apply_Choice])
Pest_Control_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Control_Choice, Permit_Apply_Choice])
Solar_Setup_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Solar_Setup_Choice, Permit_Apply_Choice])
Staff_Train_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Staff_Train_Choice, Permit_Apply_Choice])
Market_Outreach_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Market_Outreach_Choice, Permit_Apply_Choice])
System_Setup_Loop = OperatorPOWL(operator=Operator.LOOP, children=[System_Setup_Choice, Permit_Apply_Choice])
Supplier_Contact_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Supplier_Contact_Choice, Permit_Apply_Choice])
Health_Monitor_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Health_Monitor_Choice, Permit_Apply_Choice])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[
    Site_Survey_Loop,
    Load_Test_Loop,
    Soil_Sample_Loop,
    Crop_Select_Loop,
    Irrigation_Plan_Loop,
    Permit_Apply_Choice,
    Material_Order_Loop,
    Bed_Install_Loop,
    Pest_Control_Loop,
    Solar_Setup_Loop,
    Staff_Train_Loop,
    Market_Outreach_Loop,
    System_Setup_Loop,
    Supplier_Contact_Loop,
    Health_Monitor_Loop
])

# Add edges between nodes based on their dependencies
root.order.add_edge(Site_Survey_Loop, Permit_Apply_Choice)
root.order.add_edge(Permit_Apply_Choice, Material_Order_Loop)
root.order.add_edge(Material_Order_Loop, Bed_Install_Loop)
root.order.add_edge(Bed_Install_Loop, Pest_Control_Loop)
root.order.add_edge(Pest_Control_Loop, Solar_Setup_Loop)
root.order.add_edge(Solar_Setup_Loop, Staff_Train_Loop)
root.order.add_edge(Staff_Train_Loop, Market_Outreach_Loop)
root.order.add_edge(Market_Outreach_Loop, System_Setup_Loop)
root.order.add_edge(System_Setup_Loop, Supplier_Contact_Loop)
root.order.add_edge(Supplier_Contact_Loop, Health_Monitor_Loop)