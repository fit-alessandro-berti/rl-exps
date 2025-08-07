import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_assess     = Transition(label='Site Assess')
load_testing    = Transition(label='Load Testing')
climate_study   = Transition(label='Climate Study')
medium_prep     = Transition(label='Medium Prep')
bed_install     = Transition(label='Bed Install')
irrigation_setup= Transition(label='Irrigation Setup')
crop_select     = Transition(label='Crop Select')
pest_control    = Transition(label='Pest Control')
community_meet  = Transition(label='Community Meet')
workshop_plan   = Transition(label='Workshop Plan')
monitor_deploy  = Transition(label='Monitor Deploy')
tech_integrate  = Transition(label='Tech Integrate')
waste_cycle     = Transition(label='Waste Cycle')
yield_forecast  = Transition(label='Yield Forecast')
market_link     = Transition(label='Market Link')

# Silent transition for loop exit
skip = SilentTransition()

# Define the loop body: Pest Control -> Monitor Deploy -> Tech Integrate -> Waste Cycle
body = StrictPartialOrder(nodes=[pest_control, monitor_deploy, tech_integrate, waste_cycle])
body.order.add_edge(pest_control, monitor_deploy)
body.order.add_edge(monitor_deploy, tech_integrate)
body.order.add_edge(tech_integrate, waste_cycle)

# Define the loop: do Pest Control, then either exit or do the body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, body])

# Assemble the full partial order
root = StrictPartialOrder(nodes=[
    site_assess, load_testing, climate_study,
    medium_prep, bed_install, irrigation_setup,
    crop_select, loop,
    community_meet, workshop_plan,
    yield_forecast, market_link
])

# Define the control-flow edges
root.order.add_edge(site_assess, load_testing)
root.order.add_edge(load_testing, climate_study)
root.order.add_edge(climate_study, medium_prep)
root.order.add_edge(medium_prep, bed_install)
root.order.add_edge(bed_install, irrigation_setup)
root.order.add_edge(irrigation_setup, crop_select)
root.order.add_edge(crop_select, loop)
root.order.add_edge(loop, community_meet)
root.order.add_edge(community_meet, workshop_plan)
root.order.add_edge(workshop_plan, yield_forecast)
root.order.add_edge(yield_forecast, market_link)