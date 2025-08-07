import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structure_assess = Transition(label='Structure Assess')
system_design    = Transition(label='System Design')
crop_select      = Transition(label='Crop Select')
permit_obtain    = Transition(label='Permit Obtain')
enviro_setup     = Transition(label='Enviro Setup')
irrigation_plan  = Transition(label='Irrigation Plan')
sensor_install   = Transition(label='Sensor Install')
ai_calibration   = Transition(label='AI Calibration')
staff_train      = Transition(label='Staff Train')
nutrient_mix     = Transition(label='Nutrient Mix')
pest_monitor     = Transition(label='Pest Monitor')
yield_analyze    = Transition(label='Yield Analyze')
market_align     = Transition(label='Market Align')
launch_farm      = Transition(label='Launch Farm')

# Define the main production cycle as a partial order
cycle = StrictPartialOrder(nodes=[
    crop_select,
    irrigation_plan,
    nutrient_mix,
    pest_monitor,
    yield_analyze
])
cycle.order.add_edge(crop_select, irrigation_plan)
cycle.order.add_edge(irrigation_plan, nutrient_mix)
cycle.order.add_edge(nutrient_mix, pest_monitor)
cycle.order.add_edge(pest_monitor, yield_analyze)

# Loop: repeat the production cycle until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[cycle, SilentTransition()])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_assess,
    system_design,
    permit_obtain,
    enviro_setup,
    sensor_install,
    ai_calibration,
    staff_train,
    loop,
    market_align,
    launch_farm
])
root.order.add_edge(site_survey, structure_assess)
root.order.add_edge(structure_assess, system_design)
root.order.add_edge(system_design, permit_obtain)
root.order.add_edge(permit_obtain, enviro_setup)
root.order.add_edge(enviro_setup, sensor_install)
root.order.add_edge(sensor_install, ai_calibration)
root.order.add_edge(ai_calibration, staff_train)
root.order.add_edge(staff_train, loop)
root.order.add_edge(loop, market_align)
root.order.add_edge(market_align, launch_farm)