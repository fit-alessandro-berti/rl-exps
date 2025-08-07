import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey       = Transition(label='Site Survey')
structural_check  = Transition(label='Structural Check')
env_control       = Transition(label='Env Control')
hydro_setup       = Transition(label='Hydro Setup')
crop_select       = Transition(label='Crop Select')
iot_install       = Transition(label='IoT Install')
sensor_calibrate  = Transition(label='Sensor Calibrate')
water_cycle       = Transition(label='Water Cycle')
nutrient_mix      = Transition(label='Nutrient Mix')
lighting_adjust   = Transition(label='Lighting Adjust')
staff_train       = Transition(label='Staff Train')
waste_manage      = Transition(label='Waste Manage')
energy_audit      = Transition(label='Energy Audit')
harvest_plan      = Transition(label='Harvest Plan')
delivery_setup    = Transition(label='Delivery Setup')
market_align      = Transition(label='Market Align')

# Loop for continuous monitoring and adjustment
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[SensorCalibrate, WaterCycle, NutrientMix, LightingAdjust]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    env_control,
    hydro_setup,
    crop_select,
    iot_install,
    monitor_loop,
    staff_train,
    waste_manage,
    energy_audit,
    harvest_plan,
    delivery_setup,
    market_align
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, env_control)
root.order.add_edge(env_control, hydro_setup)
root.order.add_edge(hydro_setup, crop_select)
root.order.add_edge(crop_select, iot_install)
root.order.add_edge(iot_install, monitor_loop)
root.order.add_edge(monitor_loop, staff_train)
root.order.add_edge(staff_train, waste_manage)
root.order.add_edge(staff_train, energy_audit)
root.order.add_edge(waste_manage, harvest_plan)
root.order.add_edge(energy_audit, harvest_plan)
root.order.add_edge(harvest_plan, delivery_setup)
root.order.add_edge(delivery_setup, market_align)