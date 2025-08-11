import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Select_Crops = Transition(label='Select Crops')
Install_Modules = Transition(label='Install Modules')
Setup_Sensors = Transition(label='Setup Sensors')
Calibrate_Climate = Transition(label='Calibrate Climate')
Configure_Lighting = Transition(label='Configure Lighting')
Integrate_IoT = Transition(label='Integrate IoT')
Train_Staff = Transition(label='Train Staff')
Run_Trials = Transition(label='Run Trials')
Analyze_Data = Transition(label='Analyze Data')
Optimize_Yield = Transition(label='Optimize Yield')
Check_Compliance = Transition(label='Check Compliance')
Plan_Marketing = Transition(label='Plan Marketing')
Launch_Facility = Transition(label='Launch Facility')

# Define silent transitions for empty labels
skip = SilentTransition()

# Define exclusive choice operators
Select_Crops_XOR = OperatorPOWL(operator=Operator.XOR, children=[Select_Crops, skip])

# Define loop operators
Site_Survey_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey])
Design_Layout_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Design_Layout])

# Define the root POWL model
root = StrictPartialOrder(nodes=[Site_Survey_Loop, Design_Layout_Loop, Select_Crops_XOR])
root.order.add_edge(Site_Survey_Loop, Design_Layout_Loop)
root.order.add_edge(Design_Layout_Loop, Select_Crops_XOR)

# Add additional operators for the process
Calibrate_Climate_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Calibrate_Climate])
Integrate_IoT_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Integrate_IoT])
Train_Staff_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Train_Staff])
Run_Trials_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Run_Trials])
Analyze_Data_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Analyze_Data])
Optimize_Yield_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Optimize_Yield])
Check_Compliance_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Check_Compliance])
Plan_Marketing_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Plan_Marketing])
Launch_Facility_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Launch_Facility])

# Add additional edges to the root model
root.order.add_edge(Site_Survey_Loop, Calibrate_Climate_Loop)
root.order.add_edge(Calibrate_Climate_Loop, Integrate_IoT_Loop)
root.order.add_edge(Integrate_IoT_Loop, Train_Staff_Loop)
root.order.add_edge(Train_Staff_Loop, Run_Trials_Loop)
root.order.add_edge(Run_Trials_Loop, Analyze_Data_Loop)
root.order.add_edge(Analyze_Data_Loop, Optimize_Yield_Loop)
root.order.add_edge(Optimize_Yield_Loop, Check_Compliance_Loop)
root.order.add_edge(Check_Compliance_Loop, Plan_Marketing_Loop)
root.order.add_edge(Plan_Marketing_Loop, Launch_Facility_Loop)