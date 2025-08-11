import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Structure_Prep, System_Install, Env_Control, Nutrient_Mix, Crop_Select, AI_Setup, Worker_Train, Pest_Control, Irrigation_Plan, Data_Monitor, Yield_Forecast, Energy_Audit, Market_Setup, Logistics_Plan, Waste_Manage])

root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, loop)