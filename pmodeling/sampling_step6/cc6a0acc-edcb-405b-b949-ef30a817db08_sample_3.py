from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_sample = Transition(label='Soil Sample')
water_check = Transition(label='Water Check')
design_plan = Transition(label='Design Plan')
bed_setup = Transition(label='Bed Setup')
irrigation_install = Transition(label='Irrigation Install')
climate_setup = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
planting_phase = Transition(label='Planting Phase')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_prep = Transition(label='Harvest Prep')
community_meet = Transition(label='Community Meet')
waste_manage = Transition(label='Waste Manage')
yield_report = Transition(label='Yield Report')

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[site_survey, load_test, soil_sample, water_check, design_plan, bed_setup, irrigation_install, climate_setup, seed_selection, planting_phase, pest_control, growth_monitor, harvest_prep, community_meet, waste_manage, yield_report])

# Since all activities are concurrent, there are no dependencies to add.
# If you need to define any dependencies, you can do so here by adding edges to the 'root.order' attribute.
# For example, if 'load_test' must precede 'soil_sample', you would add:
# root.order.add_edge(load_test, soil_sample)

# The 'root' variable now contains the POWL model for the process.