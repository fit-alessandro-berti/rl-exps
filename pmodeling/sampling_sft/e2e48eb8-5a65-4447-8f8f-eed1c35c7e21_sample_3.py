import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey       = Transition(label='Site Survey')
structural_check  = Transition(label='Structural Check')
climate_study     = Transition(label='Climate Study')
soil_prep         = Transition(label='Soil Prep')
seed_selection    = Transition(label='Seed Selection')
irrigation_setup  = Transition(label='Irrigation Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
sensor_install    = Transition(label='Sensor Install')
pest_monitor      = Transition(label='Pest Monitor')
data_analysis     = Transition(label='Data Analysis')
regulation_review = Transition(label='Regulation Review')
community_meet    = Transition(label='Community Meet')
harvest_plan      = Transition(label='Harvest Plan')
packaging_design  = Transition(label='Packaging Design')
distribution_map  = Transition(label='Distribution Map')
feedback_loop     = Transition(label='Feedback Loop')
maintenance_sched = Transition(label='Maintenance Schedule')

# Define the loop body (from pest monitor to feedback loop)
body = StrictPartialOrder(nodes=[data_analysis, regulation_review, community_meet])
body.order.add_edge(pest_monitor, data_analysis)
body.order.add_edge(data_analysis, regulation_review)
body.order.add_edge(regulation_review, community_meet)

# LOOP operator: do pest_monitor, then optionally do body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, climate_study, soil_prep, seed_selection,
    irrigation_setup, nutrient_mix, sensor_install, loop,
    harvest_plan, packaging_design, distribution_map, feedback_loop, maintenance_sched
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(structural_check, soil_prep)
root.order.add_edge(climate_study, soil_prep)
root.order.add_edge(soil_prep, seed_selection)
root.order.add_edge(seed_selection, irrigation_setup)
root.order.add_edge(irrigation_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_install)
root.order.add_edge(sensor_install, loop)
root.order.add_edge(loop, harvest_plan)
root.order.add_edge(harvest_plan, packaging_design)
root.order.add_edge(packaging_design, distribution_map)
root.order.add_edge(distribution_map, feedback_loop)
root.order.add_edge(feedback_loop, maintenance_sched)