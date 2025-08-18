from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Define the exclusive choice for the pest monitoring
pest_monitoring = OperatorPOWL(operator=Operator.XOR, children=[pest_monitor, feedback_loop])

# Define the loop for data analysis
data_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, regulation_review])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, structural_check, climate_study, soil_prep, seed_selection, irrigation_setup, nutrient_mix, sensor_install, pest_monitoring, data_analysis_loop, community_meet, harvest_plan, packaging_design, distribution_map, maintenance_schedule])

# Define the dependencies
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(site_survey, soil_prep)
root.order.add_edge(structural_check, soil_prep)
root.order.add_edge(climate_study, soil_prep)
root.order.add_edge(soil_prep, seed_selection)
root.order.add_edge(seed_selection, irrigation_setup)
root.order.add_edge(irrigation_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_install)
root.order.add_edge(sensor_install, pest_monitoring)
root.order.add_edge(pest_monitoring, data_analysis_loop)
root.order.add_edge(data_analysis_loop, regulation_review)
root.order.add_edge(regulation_review, community_meet)
root.order.add_edge(community_meet, harvest_plan)
root.order.add_edge(harvest_plan, packaging_design)
root.order.add_edge(packaging_design, distribution_map)
root.order.add_edge(distribution_map, maintenance_schedule)

print(root)