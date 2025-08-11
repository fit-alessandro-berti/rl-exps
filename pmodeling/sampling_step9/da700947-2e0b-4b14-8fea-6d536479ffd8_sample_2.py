import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[Site_Survey, skip])

# Define loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[Structural_Audit, Climate_Design])

# Define the root model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root model
print(root)