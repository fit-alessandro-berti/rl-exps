import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_assess = Transition(label='Site Assess')
load_test = Transition(label='Load Testing')
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

# Define the community engagement sub-process: Workshop Plan then Community Meet
community_po = StrictPartialOrder(nodes=[workshop_plan, community_meet])
community_po.order.add_edge(workshop_plan, community_meet)

# Define the monitoring & integration sub-process: Monitor Deploy then Tech Integrate
monitor_po = StrictPartialOrder(nodes=[monitor_deploy, tech_integrate])
monitor_po.order.add_edge(monitor_deploy, tech_integrate)

# Define the yield & market sub-process: Yield Forecast then Market Link
yield_po = StrictPartialOrder(nodes=[yield_forecast, market_link])
yield_po.order.add_edge(yield_forecast, market_link)

# Root process: Site Assess -> Load Testing -> Climate Study -> Medium Prep -> Bed Install -> Irrigation Setup
# Then choose either Community Engagement or the Monitoring & Integration sub-process
# Finally, do Crop Select, Pest Control, Waste Cycle, and both Yield & Market sub-processes
root = StrictPartialOrder(nodes=[
    site_assess, load_test, climate_study, medium_prep, bed_install,
    irrigation_setup, community_meet, monitor_deploy, tech_integrate,
    crop_select, pest_control, waste_cycle, yield_forecast, market_link
])

root.order.add_edge(site_assess, load_test)
root.order.add_edge(load_test, climate_study)
root.order.add_edge(climate_study, medium_prep)
root.order.add_edge(medium_prep, bed_install)
root.order.add_edge(bed_install, irrigation_setup)

# Exclusive choice between community engagement and monitoring & integration
community_choice = OperatorPOWL(operator=Operator.XOR, children=[community_meet, monitor_po])

root.order.add_edge(irrigation_setup, community_choice)

# After community choice, do the rest
root.order.add_edge(community_choice, crop_select)
root.order.add_edge(community_choice, pest_control)
root.order.add_edge(community_choice, waste_cycle)
root.order.add_edge(community_choice, yield_po)