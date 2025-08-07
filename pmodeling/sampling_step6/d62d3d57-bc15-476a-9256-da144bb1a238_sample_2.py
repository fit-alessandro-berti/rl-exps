import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their labels
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

# Define the partial order
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

# Add dependencies if any (if not, no additional edges are needed)
# Example: root.order.add_edge(site_survey, structure_assess)
# ... Add other dependencies as needed ...

# Print the root (POWL model)
print(root)