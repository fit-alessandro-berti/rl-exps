import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
env_control = Transition(label='Env Control')
hydro_setup = Transition(label='Hydro Setup')
crop_select = Transition(label='Crop Select')
iot_install = Transition(label='IoT Install')
sensor_calibrate = Transition(label='Sensor Calibrate')
water_cycle = Transition(label='Water Cycle')
nutrient_mix = Transition(label='Nutrient Mix')
lighting_adjust = Transition(label='Lighting Adjust')
staff_train = Transition(label='Staff Train')
waste_manage = Transition(label='Waste Manage')
energy_audit = Transition(label='Energy Audit')
harvest_plan = Transition(label='Harvest Plan')
delivery_setup = Transition(label='Delivery Setup')
market_align = Transition(label='Market Align')

root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    env_control,
    hydro_setup,
    crop_select,
    iot_install,
    sensor_calibrate,
    water_cycle,
    nutrient_mix,
    lighting_adjust,
    staff_train,
    waste_manage,
    energy_audit,
    harvest_plan,
    delivery_setup,
    market_align
])

# Define dependencies as needed based on the process flow
# For example, site survey might come before structural check
root.order.add_edge(site_survey, structural_check)
# ... add more dependencies as per the process flow

# You can add more dependencies if needed, e.g., env_control after site_survey
# root.order.add_edge(site_survey, env_control)

# Similarly, add other dependencies based on the process flow