import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Site_Survey = Transition(label='Site Survey')
Structure_Prep = Transition(label='Structure Prep')
System_Install = Transition(label='System Install')
Env_Control = Transition(label='Env Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Crop_Select = Transition(label='Crop Select')
AI_Setup = Transition(label='AI Setup')
Worker_Train = Transition(label='Worker Train')
Pest_Control = Transition(label='Pest Control')
Irrigation_Plan = Transition(label='Irrigation Plan')
Data_Monitor = Transition(label='Data Monitor')
Yield_Forecast = Transition(label='Yield Forecast')
Energy_Audit = Transition(label='Energy Audit')
Market_Setup = Transition(label='Market Setup')
Logistics_Plan = Transition(label='Logistics Plan')
Waste_Manage = Transition(label='Waste Manage')

# Define the silent transitions (no action)
skip = SilentTransition()

# Define the loop for AI Setup
loop = OperatorPOWL(operator=Operator.LOOP, children=[AI_Setup, skip])

# Define the XOR for Pest Control
xor = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, skip])

# Define the POWL model
root = StrictPartialOrder(nodes=[Site_Survey, Structure_Prep, System_Install, Env_Control, Nutrient_Mix, Crop_Select, AI_Setup, Worker_Train, Pest_Control, Irrigation_Plan, Data_Monitor, Yield_Forecast, Energy_Audit, Market_Setup, Logistics_Plan, Waste_Manage, loop, xor])
root.order.add_edge(Site_Survey, Structure_Prep)
root.order.add_edge(Structure_Prep, System_Install)
root.order.add_edge(System_Install, Env_Control)
root.order.add_edge(Env_Control, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Crop_Select)
root.order.add_edge(Crop_Select, AI_Setup)
root.order.add_edge(AI_Setup, Worker_Train)
root.order.add_edge(Worker_Train, Pest_Control)
root.order.add_edge(Pest_Control, Irrigation_Plan)
root.order.add_edge(Irrigation_Plan, Data_Monitor)
root.order.add_edge(Data_Monitor, Yield_Forecast)
root.order.add_edge(Yield_Forecast, Energy_Audit)
root.order.add_edge(Energy_Audit, Market_Setup)
root.order.add_edge(Market_Setup, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Waste_Manage)
root.order.add_edge(AI_Setup, loop)
root.order.add_edge(Pest_Control, xor)