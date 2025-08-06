from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions (empty labels)
skip = SilentTransition()

# Define the loop nodes
yield_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_analyze, market_align])

# Define the exclusive choice nodes
site_loop = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structure_assess])
system_loop = OperatorPOWL(operator=Operator.XOR, children=[system_design, crop_select])
enviro_loop = OperatorPOWL(operator=Operator.XOR, children=[permit_obtain, enviro_setup])
irrigation_loop = OperatorPOWL(operator=Operator.XOR, children=[irrigation_plan, sensor_install])
ai_loop = OperatorPOWL(operator=Operator.XOR, children=[ai_calibration, staff_train])
nutrient_loop = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, pest_monitor])
pest_loop = OperatorPOWL(operator=Operator.XOR, children=[pest_monitor, yield_analyze])
market_loop = OperatorPOWL(operator=Operator.XOR, children=[market_align, launch_farm])

# Create the root POWL model
root = StrictPartialOrder(nodes=[site_loop, system_loop, enviro_loop, irrigation_loop, ai_loop, nutrient_loop, pest_loop, market_loop, yield_loop])
root.order.add_edge(site_loop, system_loop)
root.order.add_edge(system_loop, enviro_loop)
root.order.add_edge(enviro_loop, irrigation_loop)
root.order.add_edge(irrigation_loop, ai_loop)
root.order.add_edge(ai_loop, nutrient_loop)
root.order.add_edge(nutrient_loop, pest_loop)
root.order.add_edge(pest_loop, market_loop)
root.order.add_edge(market_loop, yield_loop)
root.order.add_edge(yield_loop, market_loop)

# Print the root POWL model
print(root)