from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
site_assess = Transition(label='Site Assess')
load_testing = Transition(label='Load Testing')
climate_study = Transition(label='Climate Study')
medium_prep = Transition(label='Medium Prep')
bed_install = Transition(label='Bed Install')
irrigation_setup = Transition(label='Irrigation Setup')
crop_select = Transition(label='Crop Select')
pest_control = Transition(label='Pest Control')
community_meet = Transition(label='Community Meet')
monitor_deploy = Transition(label='Monitor Deploy')
waste_cycle = Transition(label='Waste Cycle')
yield_forecast = Transition(label='Yield Forecast')
market_link = Transition(label='Market Link')
workshop_plan = Transition(label='Workshop Plan')
tech_integrate = Transition(label='Tech Integrate')

# Define the partial order
root = StrictPartialOrder(nodes=[site_assess, load_testing, climate_study, medium_prep, bed_install, irrigation_setup, crop_select, pest_control, community_meet, monitor_deploy, waste_cycle, yield_forecast, market_link, workshop_plan, tech_integrate])

# Define the dependencies between activities
root.order.add_edge(site_assess, load_testing)
root.order.add_edge(load_testing, climate_study)
root.order.add_edge(climate_study, medium_prep)
root.order.add_edge(medium_prep, bed_install)
root.order.add_edge(bed_install, irrigation_setup)
root.order.add_edge(irrigation_setup, crop_select)
root.order.add_edge(crop_select, pest_control)
root.order.add_edge(pest_control, community_meet)
root.order.add_edge(community_meet, monitor_deploy)
root.order.add_edge(monitor_deploy, waste_cycle)
root.order.add_edge(waste_cycle, yield_forecast)
root.order.add_edge(yield_forecast, market_link)
root.order.add_edge(market_link, workshop_plan)
root.order.add_edge(workshop_plan, tech_integrate)

# The final POWL model is stored in the variable 'root'