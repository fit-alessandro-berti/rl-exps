import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Modules = Transition(label='Design Modules')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
LED_Tuning = Transition(label='LED Tuning')
Seed_Automation = Transition(label='Seed Automation')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Yield_Forecast = Transition(label='Yield Forecast')
Energy_Audit = Transition(label='Energy Audit')
Waste_System = Transition(label='Waste System')
Community_Meet = Transition(label='Community Meet')
Compliance_Check = Transition(label='Compliance Check')
Crop_Packing = Transition(label='Crop Packing')
Logistics_Plan = Transition(label='Logistics Plan')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Design_Modules, Climate_Setup, Nutrient_Mix, LED_Tuning, Seed_Automation, Growth_Monitor, Pest_Control, Yield_Forecast, Energy_Audit, Waste_System, Community_Meet, Compliance_Check, Crop_Packing, Logistics_Plan])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)