import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
Site_Survey = Transition(label='Site Survey')
Structural_Audit = Transition(label='Structural Audit')
Climate_Design = Transition(label='Climate Design')
Lighting_Setup = Transition(label='Lighting Setup')
Irrigation_Plan = Transition(label='Irrigation Plan')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Install = Transition(label='Sensor Install')
AI_Calibration = Transition(label='AI Calibration')
Pest_Scan = Transition(label='Pest Scan')
Energy_Audit = Transition(label='Energy Audit')
Renewable_Sync = Transition(label='Renewable Sync')
Data_Modeling = Transition(label='Data Modeling')
Staff_Briefing = Transition(label='Staff Briefing')
Compliance_Check = Transition(label='Compliance Check')
Community_Meet = Transition(label='Community Meet')
Yield_Review = Transition(label='Yield Review')
Feedback_Loop = Transition(label='Feedback Loop')

# Define silent transitions
skip = SilentTransition()

# Define loops
Site_Survey_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Structural_Audit])
Climate_Design_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Climate_Design, Lighting_Setup, Irrigation_Plan])
Nutrient_Mix_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Nutrient_Mix, Sensor_Install, AI_Calibration])
Energy_Audit_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Energy_Audit, Renewable_Sync, Data_Modeling])
Compliance_Check_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Compliance_Check, Community_Meet, Yield_Review])

# Define XORs
Site_Survey_XOR = OperatorPOWL(operator=Operator.XOR, children=[Site_Survey_Loop, skip])
Climate_Design_XOR = OperatorPOWL(operator=Operator.XOR, children=[Climate_Design_Loop, skip])
Nutrient_Mix_XOR = OperatorPOWL(operator=Operator.XOR, children=[Nutrient_Mix_Loop, skip])
Energy_Audit_XOR = OperatorPOWL(operator=Operator.XOR, children=[Energy_Audit_Loop, skip])
Compliance_Check_XOR = OperatorPOWL(operator=Operator.XOR, children=[Compliance_Check_Loop, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[Site_Survey_XOR, Climate_Design_XOR, Nutrient_Mix_XOR, Energy_Audit_XOR, Compliance_Check_XOR, Staff_Briefing, Feedback_Loop])
root.order.add_edge(Site_Survey_XOR, Climate_Design_XOR)
root.order.add_edge(Climate_Design_XOR, Nutrient_Mix_XOR)
root.order.add_edge(Nutrient_Mix_XOR, Energy_Audit_XOR)
root.order.add_edge(Energy_Audit_XOR, Compliance_Check_XOR)
root.order.add_edge(Compliance_Check_XOR, Staff_Briefing)
root.order.add_edge(Staff_Briefing, Feedback_Loop)