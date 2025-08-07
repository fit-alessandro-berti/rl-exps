import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey    = Transition(label='Site Survey')
impact_study   = Transition(label='Impact Study')
structure_chk  = Transition(label='Structure Check')
soil_test      = Transition(label='Soil Testing')
system_design  = Transition(label='System Design')
seed_sel       = Transition(label='Seed Selection')
irrigation     = Transition(label='Irrigation Setup')
lighting       = Transition(label='Lighting Install')
pest_ctrl      = Transition(label='Pest Control')
community_meet = Transition(label='Community Meet')
regulation_chk = Transition(label='Regulation Review')
waste_plan     = Transition(label='Waste Plan')
crop_monitor   = Transition(label='Crop Monitor')
harvest_prep   = Transition(label='Harvest Prep')
market_launch  = Transition(label='Market Launch')

# Define the monitoring loop: repeatedly monitor crops until exit
monitor_body = StrictPartialOrder(nodes=[crop_monitor, harvest_prep, market_launch])
monitor_body.order.add_edge(crop_monitor, harvest_prep)
monitor_body.order.add_edge(harvest_prep, market_launch)

monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_body, monitor_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, impact_study, structure_chk, soil_test, system_design,
    seed_sel, irrigation, lighting, pest_ctrl, community_meet,
    regulation_chk, waste_plan, monitor_loop
])

# Add the sequential dependencies
root.order.add_edge(site_survey, impact_study)
root.order.add_edge(impact_study, structure_chk)
root.order.add_edge(structure_chk, soil_test)
root.order.add_edge(soil_test, system_design)
root.order.add_edge(system_design, seed_sel)
root.order.add_edge(seed_sel, irrigation)
root.order.add_edge(irrigation, lighting)
root.order.add_edge(lighting, pest_ctrl)
root.order.add_edge(pest_ctrl, community_meet)
root.order.add_edge(community_meet, regulation_chk)
root.order.add_edge(regulation_chk, waste_plan)
root.order.add_edge(waste_plan, monitor_loop)