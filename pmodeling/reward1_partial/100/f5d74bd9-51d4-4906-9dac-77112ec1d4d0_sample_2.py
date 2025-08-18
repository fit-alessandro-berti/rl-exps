import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
Site_Review = Transition(label='Site Review')
Impact_Study = Transition(label='Impact Study')
Design_Plan = Transition(label='Design Plan')
Structure_Mod = Transition(label='Structure Mod')
Hydroponics_Setup = Transition(label='Hydroponics Setup')
Crop_Select = Transition(label='Crop Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Control = Transition(label='Pest Control')
Sensor_Install = Transition(label='Sensor Install')
Staff_Train = Transition(label='Staff Train')
Compliance_Audit = Transition(label='Compliance Audit')
Packaging_Dev = Transition(label='Packaging Dev')
Logistics_Plan = Transition(label='Logistics Plan')
Community_Engage = Transition(label='Community Engage')
Sustainability_Check = Transition(label='Sustainability Check')

# Define silent transitions (no action)
skip = SilentTransition()

# Define the process structure
xor = OperatorPOWL(operator=Operator.XOR, children=[
    OperatorPOWL(operator=Operator.LOOP, children=[Site_Review, Impact_Study, Design_Plan, Structure_Mod]),
    OperatorPOWL(operator=Operator.LOOP, children=[Hydroponics_Setup, Crop_Select, Nutrient_Mix, Pest_Control, Sensor_Install, Staff_Train, Compliance_Audit, Packaging_Dev, Logistics_Plan, Community_Engage, Sustainability_Check])
])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, xor)