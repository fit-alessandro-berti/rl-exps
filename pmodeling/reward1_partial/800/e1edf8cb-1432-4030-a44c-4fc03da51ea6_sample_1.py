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

skip = SilentTransition()

site_survey_and_env_control = OperatorPOWL(operator=Operator.XOR, children=[site_survey, env_control])
structural_check_and_hydro_setup = OperatorPOWL(operator=Operator.XOR, children=[structural_check, hydro_setup])
crop_select_and_iot_install = OperatorPOWL(operator=Operator.XOR, children=[crop_select, iot_install])
sensor_calibrate_and_water_cycle = OperatorPOWL(operator=Operator.XOR, children=[sensor_calibrate, water_cycle])
nutrient_mix_and_lighting_adjust = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, lighting_adjust])
staff_train_and_waste_manage = OperatorPOWL(operator=Operator.XOR, children=[staff_train, waste_manage])
energy_audit_and_harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, harvest_plan])
delivery_setup_and_market_align = OperatorPOWL(operator=Operator.XOR, children=[delivery_setup, market_align])

root = StrictPartialOrder(nodes=[
    site_survey_and_env_control,
    structural_check_and_hydro_setup,
    crop_select_and_iot_install,
    sensor_calibrate_and_water_cycle,
    nutrient_mix_and_lighting_adjust,
    staff_train_and_waste_manage,
    energy_audit_and_harvest_plan,
    delivery_setup_and_market_align
])

root.order.add_edge(site_survey_and_env_control, structural_check_and_hydro_setup)
root.order.add_edge(structural_check_and_hydro_setup, crop_select_and_iot_install)
root.order.add_edge(crop_select_and_iot_install, sensor_calibrate_and_water_cycle)
root.order.add_edge(sensor_calibrate_and_water_cycle, nutrient_mix_and_lighting_adjust)
root.order.add_edge(nutrient_mix_and_lighting_adjust, staff_train_and_waste_manage)
root.order.add_edge(staff_train_and_waste_manage, energy_audit_and_harvest_plan)
root.order.add_edge(energy_audit_and_harvest_plan, delivery_setup_and_market_align)