import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Site Assessment and Initial Evaluation
site_assessment = OperatorPOWL(operator=Operator.XOR, children=[site_survey, load_test])

# Structural Analysis and Soil Testing
structural_analysis = OperatorPOWL(operator=Operator.XOR, children=[soil_sample, water_check])

# Modular Bed Installation
modular_bed_installation = OperatorPOWL(operator=Operator.LOOP, children=[bed_setup, irrigation_install, climate_setup])

# Crop Selection and Pest Management
crop_selection = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, planting_phase, pest_control])

# Growth Monitoring and Harvest Preparation
growth_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, harvest_prep])

# Community Engagement and Waste Management
community_engagement = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, waste_manage])

# Yield Reporting
yield_reporting = OperatorPOWL(operator=Operator.LOOP, children=[yield_report])

# Finalizing the Process
finalization = OperatorPOWL(operator=Operator.LOOP, children=[community_engagement, yield_reporting])

root = StrictPartialOrder(nodes=[site_assessment, structural_analysis, modular_bed_installation, crop_selection, growth_monitoring, finalization])
root.order.add_edge(site_assessment, structural_analysis)
root.order.add_edge(structural_analysis, modular_bed_installation)
root.order.add_edge(modular_bed_installation, crop_selection)
root.order.add_edge(crop_selection, growth_monitoring)
root.order.add_edge(growth_monitoring, finalization)