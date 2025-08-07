import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root of the process
root = StrictPartialOrder(nodes=[
    site_assess, load_testing, climate_study, medium_prep, bed_install, irrigation_setup,
    crop_select, pest_control, community_meet, monitor_deploy, waste_cycle, yield_forecast,
    market_link, workshop_plan, tech_integrate
])

# The order of activities can be defined based on the process flow
# For simplicity, we assume a linear sequence here
# In a real scenario, the order might be more complex and would need to be defined explicitly
# For example, if there are dependencies, we could use root.order.add_edge(...) to define them

# Here, we assume a linear sequence for simplicity
root.order.add_edge(site_assess, load_testing)
root.order.add_edge(site_assess, climate_study)
root.order.add_edge(site_assess, medium_prep)
root.order.add_edge(site_assess, bed_install)
root.order.add_edge(site_assess, irrigation_setup)
root.order.add_edge(site_assess, crop_select)
root.order.add_edge(site_assess, pest_control)
root.order.add_edge(site_assess, community_meet)
root.order.add_edge(site_assess, monitor_deploy)
root.order.add_edge(site_assess, waste_cycle)
root.order.add_edge(site_assess, yield_forecast)
root.order.add_edge(site_assess, market_link)
root.order.add_edge(site_assess, workshop_plan)
root.order.add_edge(site_assess, tech_integrate)

# The final result is saved in the 'root' variable