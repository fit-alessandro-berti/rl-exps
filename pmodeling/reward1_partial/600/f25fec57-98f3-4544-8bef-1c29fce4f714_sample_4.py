import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
structure_design = Transition(label='Structure Design')
system_install = Transition(label='System Install')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_config = Transition(label='Climate Config')
ai_integration = Transition(label='AI Integration')
nutrient_sourcing = Transition(label='Nutrient Sourcing')
waste_planning = Transition(label='Waste Planning')
staff_training = Transition(label='Staff Training')
crop_seeding = Transition(label='Crop Seeding')
growth_monitoring = Transition(label='Growth Monitoring')
quality_testing = Transition(label='Quality Testing')
harvest_scheduling = Transition(label='Harvest Scheduling')
distribution_plan = Transition(label='Distribution Plan')
data_analysis = Transition(label='Data Analysis')

# Define the partial order graph
root = StrictPartialOrder(nodes=[site_survey, permit_filing, structure_design, system_install, hydroponic_setup, climate_config, ai_integration, nutrient_sourcing, waste_planning, staff_training, crop_seeding, growth_monitoring, quality_testing, harvest_scheduling, distribution_plan, data_analysis])

# Define the dependencies (edges) between the activities
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, structure_design)
root.order.add_edge(structure_design, system_install)
root.order.add_edge(system_install, hydroponic_setup)
root.order.add_edge(hydroponic_setup, climate_config)
root.order.add_edge(climate_config, ai_integration)
root.order.add_edge(ai_integration, nutrient_sourcing)
root.order.add_edge(nutrient_sourcing, waste_planning)
root.order.add_edge(waste_planning, staff_training)
root.order.add_edge(staff_training, crop_seeding)
root.order.add_edge(crop_seeding, growth_monitoring)
root.order.add_edge(growth_monitoring, quality_testing)
root.order.add_edge(quality_testing, harvest_scheduling)
root.order.add_edge(harvest_scheduling, distribution_plan)
root.order.add_edge(distribution_plan, data_analysis)

print(root)