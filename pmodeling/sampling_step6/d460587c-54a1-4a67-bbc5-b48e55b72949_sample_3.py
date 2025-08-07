import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
load_testing = Transition(label='Load Testing')
soil_sampling = Transition(label='Soil Sampling')
water_testing = Transition(label='Water Testing')
system_design = Transition(label='System Design')
solar_setup = Transition(label='Solar Setup')
crop_planning = Transition(label='Crop Planning')
stakeholder_meet = Transition(label='Stakeholder Meet')
material_order = Transition(label='Material Order')
system_install = Transition(label='System Install')
environmental_audit = Transition(label='Environmental Audit')
growth_monitoring = Transition(label='Growth Monitoring')
pest_control = Transition(label='Pest Control')
market_launch = Transition(label='Market Launch')

# Define the root of the partial order
root = StrictPartialOrder(nodes=[site_survey, permit_filing, load_testing, soil_sampling, water_testing, system_design, solar_setup, crop_planning, stakeholder_meet, material_order, system_install, environmental_audit, growth_monitoring, pest_control, market_launch])

# Define the dependencies between activities
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(site_survey, load_testing)
root.order.add_edge(site_survey, soil_sampling)
root.order.add_edge(site_survey, water_testing)
root.order.add_edge(site_survey, system_design)
root.order.add_edge(site_survey, solar_setup)
root.order.add_edge(site_survey, crop_planning)
root.order.add_edge(site_survey, stakeholder_meet)
root.order.add_edge(site_survey, material_order)
root.order.add_edge(site_survey, system_install)
root.order.add_edge(site_survey, environmental_audit)
root.order.add_edge(site_survey, growth_monitoring)
root.order.add_edge(site_survey, pest_control)
root.order.add_edge(site_survey, market_launch)

print(root)