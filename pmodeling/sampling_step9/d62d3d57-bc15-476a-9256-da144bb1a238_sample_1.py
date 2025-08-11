import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structure_assess = Transition(label='Structure Assess')
system_design = Transition(label='System Design')
crop_select = Transition(label='Crop Select')
permit_obtain = Transition(label='Permit Obtain')
enviro_setup = Transition(label='Enviro Setup')
irrigation_plan = Transition(label='Irrigation Plan')
sensor_install = Transition(label='Sensor Install')
ai_calibration = Transition(label='AI Calibration')
staff_train = Transition(label='Staff Train')
nutrient_mix = Transition(label='Nutrient Mix')
pest_monitor = Transition(label='Pest Monitor')
yield_analyze = Transition(label='Yield Analyze')
market_align = Transition(label='Market Align')
launch_farm = Transition(label='Launch Farm')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[launch_farm, site_survey])
xor = OperatorPOWL(operator=Operator.XOR, children=[launch_farm, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)