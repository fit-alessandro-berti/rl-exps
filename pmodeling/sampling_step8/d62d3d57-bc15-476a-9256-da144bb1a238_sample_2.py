import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the exclusive choice (XOR) for crop selection and automated nutrient delivery
xor = OperatorPOWL(operator=Operator.XOR, children=[crop_select, nutrient_mix])

# Define the loop for pest monitoring via AI sensors
loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[site_survey, structure_assess, system_design, xor, loop, enviro_setup, irrigation_plan, sensor_install, ai_calibration, staff_train, yield_analyze, market_align, launch_farm])

# Add edges between the nodes
root.order.add_edge(site_survey, structure_assess)
root.order.add_edge(structure_assess, system_design)
root.order.add_edge(system_design, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, enviro_setup)
root.order.add_edge(enviro_setup, irrigation_plan)
root.order.add_edge(irrigation_plan, sensor_install)
root.order.add_edge(sensor_install, ai_calibration)
root.order.add_edge(ai_calibration, staff_train)
root.order.add_edge(staff_train, yield_analyze)
root.order.add_edge(yield_analyze, market_align)
root.order.add_edge(market_align, launch_farm)