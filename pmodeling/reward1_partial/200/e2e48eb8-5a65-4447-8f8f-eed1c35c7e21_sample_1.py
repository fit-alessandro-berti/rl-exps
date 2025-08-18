import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
climate_study = Transition(label='Climate Study')
soil_prep = Transition(label='Soil Prep')
seed_selection = Transition(label='Seed Selection')
irrigation_setup = Transition(label='Irrigation Setup')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_install = Transition(label='Sensor Install')
pest_monitor = Transition(label='Pest Monitor')
data_analysis = Transition(label='Data Analysis')
regulation_review = Transition(label='Regulation Review')
community_meet = Transition(label='Community Meet')
harvest_plan = Transition(label='Harvest Plan')
packaging_design = Transition(label='Packaging Design')
distribution_map = Transition(label='Distribution Map')
feedback_loop = Transition(label='Feedback Loop')
maintenance_schedule = Transition(label='Maintenance Schedule')

loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_check, climate_study])
loop_soil_prep = OperatorPOWL(operator=Operator.LOOP, children=[soil_prep, sensor_install])
loop_pest_monitor = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitor, data_analysis, regulation_review, community_meet, harvest_plan])
loop_packaging_design = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, distribution_map, feedback_loop, maintenance_schedule])

root = StrictPartialOrder(nodes=[loop_site_survey, loop_soil_prep, loop_pest_monitor, loop_packaging_design])
root.order.add_edge(loop_site_survey, loop_soil_prep)
root.order.add_edge(loop_soil_prep, loop_pest_monitor)
root.order.add_edge(loop_pest_monitor, loop_packaging_design)