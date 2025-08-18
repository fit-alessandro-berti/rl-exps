from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_assess = Transition(label='Site Assess')
structure_check = Transition(label='Structure Check')
soil_test = Transition(label='Soil Test')
climate_eval = Transition(label='Climate Eval')
permit_obtain = Transition(label='Permit Obtain')
design_layout = Transition(label='Design Layout')
seed_sourcing = Transition(label='Seed Sourcing')
irrigation_set = Transition(label='Irrigation Set')
nutrient_mix = Transition(label='Nutrient Mix')
pest_control = Transition(label='Pest Control')
sensor_install = Transition(label='Sensor Install')
staff_train = Transition(label='Staff Train')
crop_planting = Transition(label='Crop Planting')
yield_monitor = Transition(label='Yield Monitor')
market_setup = Transition(label='Market Setup')
maintenance = Transition(label='Maintenance')
waste_manage = Transition(label='Waste Manage')

skip = SilentTransition()

# Define the workflow
site_assess_then_structure_check = OperatorPOWL(operator=Operator.XOR, children=[site_assess, structure_check])
soil_test_then_climate_eval = OperatorPOWL(operator=Operator.XOR, children=[soil_test, climate_eval])
permit_obtain_then_design_layout = OperatorPOWL(operator=Operator.XOR, children=[permit_obtain, design_layout])
seed_sourcing_then_irrigation_set = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, irrigation_set])
nutrient_mix_then_pest_control = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, pest_control])
sensor_install_then_staff_train = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, staff_train])
crop_planting_then_yield_monitor = OperatorPOWL(operator=Operator.XOR, children=[crop_planting, yield_monitor])
market_setup_then_maintenance = OperatorPOWL(operator=Operator.XOR, children=[market_setup, maintenance])
waste_manage_then_skip = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, skip])

root = StrictPartialOrder(nodes=[
    site_assess_then_structure_check,
    soil_test_then_climate_eval,
    permit_obtain_then_design_layout,
    seed_sourcing_then_irrigation_set,
    nutrient_mix_then_pest_control,
    sensor_install_then_staff_train,
    crop_planting_then_yield_monitor,
    market_setup_then_maintenance,
    waste_manage_then_skip
])

root.order.add_edge(site_assess_then_structure_check, soil_test_then_climate_eval)
root.order.add_edge(soil_test_then_climate_eval, permit_obtain_then_design_layout)
root.order.add_edge(permit_obtain_then_design_layout, seed_sourcing_then_irrigation_set)
root.order.add_edge(seed_sourcing_then_irrigation_set, nutrient_mix_then_pest_control)
root.order.add_edge(nutrient_mix_then_pest_control, sensor_install_then_staff_train)
root.order.add_edge(sensor_install_then_staff_train, crop_planting_then_yield_monitor)
root.order.add_edge(crop_planting_then_yield_monitor, market_setup_then_maintenance)
root.order.add_edge(market_setup_then_maintenance, waste_manage_then_skip)