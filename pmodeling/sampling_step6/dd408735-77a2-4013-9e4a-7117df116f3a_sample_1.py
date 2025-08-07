import pm4py
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_assess, structure_check, soil_test, climate_eval, permit_obtain,
    design_layout, seed_sourcing, irrigation_set, nutrient_mix, pest_control,
    sensor_install, staff_train, crop_planting, yield_monitor, market_setup,
    maintenance, waste_manage
])

# Add dependencies (partial order)
# For simplicity, we assume that each activity depends on the previous one
# This is a simplification and in a real scenario, dependencies would be more complex
for i in range(len(root.nodes) - 1):
    root.order.add_edge(root.nodes[i], root.nodes[i + 1])

# The 'root' variable now contains the POWL model for the process