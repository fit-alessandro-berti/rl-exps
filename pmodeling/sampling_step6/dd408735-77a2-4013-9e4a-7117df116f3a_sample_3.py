import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the partial order workflow
root = StrictPartialOrder(nodes=[site_assess, structure_check, soil_test, climate_eval, permit_obtain, design_layout, seed_sourcing, irrigation_set, nutrient_mix, pest_control, sensor_install, staff_train, crop_planting, yield_monitor, market_setup, maintenance, waste_manage])