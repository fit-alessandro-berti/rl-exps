from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for maintenance
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance, waste_manage])

# Define the exclusive choice between staff training and crop planting
staff_or_crop = OperatorPOWL(operator=Operator.XOR, children=[staff_train, crop_planting])

# Define the partial order
root = StrictPartialOrder(nodes=[site_assess, structure_check, soil_test, climate_eval, permit_obtain, design_layout, seed_sourcing, irrigation_set, nutrient_mix, pest_control, sensor_install, staff_or_crop, yield_monitor, market_setup, maintenance_loop])
root.order.add_edge(site_assess, structure_check)
root.order.add_edge(site_assess, soil_test)
root.order.add_edge(site_assess, climate_eval)
root.order.add_edge(site_assess, permit_obtain)
root.order.add_edge(structure_check, design_layout)
root.order.add_edge(structure_check, irrigation_set)
root.order.add_edge(soil_test, nutrient_mix)
root.order.add_edge(climate_eval, pest_control)
root.order.add_edge(permit_obtain, sensor_install)
root.order.add_edge(design_layout, staff_or_crop)
root.order.add_edge(irrigation_set, yield_monitor)
root.order.add_edge(nutrient_mix, market_setup)
root.order.add_edge(pest_control, maintenance_loop)