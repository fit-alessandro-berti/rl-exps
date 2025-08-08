import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    site_survey,
    structure_assess,
    system_design,
    crop_select,
    permit_obtain,
    enviro_setup,
    irrigation_plan,
    sensor_install,
    ai_calibration,
    staff_train,
    nutrient_mix,
    pest_monitor,
    yield_analyze,
    market_align,
    launch_farm
])

# Define the dependencies between activities
root.order.add_edge(site_survey, structure_assess)
root.order.add_edge(structure_assess, system_design)
root.order.add_edge(system_design, crop_select)
root.order.add_edge(crop_select, permit_obtain)
root.order.add_edge(permit_obtain, enviro_setup)
root.order.add_edge(enviro_setup, irrigation_plan)
root.order.add_edge(irrigation_plan, sensor_install)
root.order.add_edge(sensor_install, ai_calibration)
root.order.add_edge(ai_calibration, staff_train)
root.order.add_edge(staff_train, nutrient_mix)
root.order.add_edge(nutrient_mix, pest_monitor)
root.order.add_edge(pest_monitor, yield_analyze)
root.order.add_edge(yield_analyze, market_align)
root.order.add_edge(market_align, launch_farm)

print(root)