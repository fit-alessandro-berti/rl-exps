import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define partial order
root = StrictPartialOrder(
    nodes=[site_survey, structural_check, env_control, hydro_setup, crop_select, iot_install, sensor_calibrate, 
           water_cycle, nutrient_mix, lighting_adjust, staff_train, waste_manage, energy_audit, harvest_plan, 
           delivery_setup, market_align],
    order={
        site_survey: [structural_check],
        structural_check: [env_control],
        env_control: [hydro_setup],
        hydro_setup: [crop_select],
        crop_select: [iot_install],
        iot_install: [sensor_calibrate],
        sensor_calibrate: [water_cycle],
        water_cycle: [nutrient_mix],
        nutrient_mix: [lighting_adjust],
        lighting_adjust: [staff_train],
        staff_train: [waste_manage],
        waste_manage: [energy_audit],
        energy_audit: [harvest_plan],
        harvest_plan: [delivery_setup],
        delivery_setup: [market_align]
    }
)