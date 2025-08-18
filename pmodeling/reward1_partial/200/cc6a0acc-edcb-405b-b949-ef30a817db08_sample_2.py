from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
site_assessment = StrictPartialOrder(nodes=[site_survey, load_test, soil_sample, water_check], order={site_survey: load_test, load_test: soil_sample, soil_sample: water_check})
structural_analysis = StrictPartialOrder(nodes=[site_assessment, design_plan], order={site_assessment: design_plan})
soil_water_testing = StrictPartialOrder(nodes=[structural_analysis, soil_sample, water_check], order={structural_analysis: soil_sample, soil_sample: water_check})
modular_bed_installation = StrictPartialOrder(nodes=[soil_water_testing, bed_setup], order={soil_water_testing: bed_setup})
climate_control_setup = StrictPartialOrder(nodes=[modular_bed_installation, irrigation_install, climate_setup], order={modular_bed_installation: irrigation_install, irrigation_install: climate_setup})
crop_selection = StrictPartialOrder(nodes=[climate_control_setup, seed_selection], order={climate_control_setup: seed_selection})
pest_management = StrictPartialOrder(nodes=[crop_selection, pest_control], order={crop_selection: pest_control})
community_engagement = StrictPartialOrder(nodes=[pest_management, community_meet], order={pest_management: community_meet})
ongoing_maintenance = StrictPartialOrder(nodes=[community_engagement, waste_manage, yield_report], order={community_engagement: waste_manage, waste_manage: yield_report})

# Define the root node
root = ongoing_maintenance