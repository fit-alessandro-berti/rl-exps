import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) using their exact names
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

# Define the partial order with the defined transitions
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_filing,
    structure_design,
    system_install,
    hydroponic_setup,
    climate_config,
    ai_integration,
    nutrient_sourcing,
    waste_planning,
    staff_training,
    crop_seeding,
    growth_monitoring,
    quality_testing,
    harvest_scheduling,
    distribution_plan,
    data_analysis
])

# Since there is no explicit order defined in the problem statement, we assume the order is sequential for simplicity
# If there were dependencies, they would be added to the 'order' attribute of the StrictPartialOrder object

print(root)