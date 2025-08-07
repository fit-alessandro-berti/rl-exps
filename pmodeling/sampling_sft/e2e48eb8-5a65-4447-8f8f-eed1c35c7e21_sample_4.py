import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
climate_study    = Transition(label='Climate Study')
soil_prep        = Transition(label='Soil Prep')
seed_selection   = Transition(label='Seed Selection')
irrigation_setup = Transition(label='Irrigation Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
sensor_install   = Transition(label='Sensor Install')
pest_monitor     = Transition(label='Pest Monitor')
data_analysis    = Transition(label='Data Analysis')
regulation_review= Transition(label='Regulation Review')
community_meet   = Transition(label='Community Meet')
harvest_plan     = Transition(label='Harvest Plan')
packaging_design = Transition(label='Packaging Design')
distribution_map = Transition(label='Distribution Map')
feedback_loop    = Transition(label='Feedback Loop')
maintenance_sched= Transition(label='Maintenance Schedule')

# Loop for continuous pest monitoring and data analysis
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pest_monitor, data_analysis]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, climate_study,
    soil_prep, seed_selection,
    irrigation_setup, nutrient_mix,
    sensor_install, monitor_loop,
    regulation_review, community_meet,
    harvest_plan, packaging_design,
    distribution_map, feedback_loop,
    maintenance_sched
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(structural_check, soil_prep)
root.order.add_edge(climate_study, soil_prep)
root.order.add_edge(soil_prep, seed_selection)
root.order.add_edge(soil_prep, irrigation_setup)
root.order.add_edge(soil_prep, nutrient_mix)
root.order.add_edge(soil_prep, sensor_install)
root.order.add_edge(soil_prep, monitor_loop)
root.order.add_edge(monitor_loop, regulation_review)
root.order.add_edge(monitor_loop, community_meet)
root.order.add_edge(regulation_review, harvest_plan)
root.order.add_edge(regulation_review, packaging_design)
root.order.add_edge(regulation_review, distribution_map)
root.order.add_edge(regulation_review, feedback_loop)
root.order.add_edge(regulation_review, maintenance_sched)