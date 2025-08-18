import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
site_survey = Transition(label='Site Survey')
regulation_check = Transition(label='Regulation Check')
modular_design = Transition(label='Modular Design')
material_sourcing = Transition(label='Material Sourcing')
energy_integration = Transition(label='Energy Integration')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
system_assembly = Transition(label='System Assembly')
automation_config = Transition(label='Automation Config')
crop_seeding = Transition(label='Crop Seeding')
growth_monitoring = Transition(label='Growth Monitoring')
waste_handling = Transition(label='Waste Handling')
community_meet = Transition(label='Community Meet')
data_analysis = Transition(label='Data Analysis')
feedback_loop = Transition(label='Feedback Loop')
yield_forecast = Transition(label='Yield Forecast')

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[site_survey, regulation_check, modular_design, material_sourcing,
           energy_integration, climate_setup, nutrient_mix, system_assembly,
           automation_config, crop_seeding, growth_monitoring, waste_handling,
           community_meet, data_analysis, feedback_loop, yield_forecast],
    order={
        (site_survey, regulation_check): None,
        (regulation_check, modular_design): None,
        (modular_design, material_sourcing): None,
        (material_sourcing, energy_integration): None,
        (energy_integration, climate_setup): None,
        (climate_setup, nutrient_mix): None,
        (nutrient_mix, system_assembly): None,
        (system_assembly, automation_config): None,
        (automation_config, crop_seeding): None,
        (crop_seeding, growth_monitoring): None,
        (growth_monitoring, waste_handling): None,
        (waste_handling, community_meet): None,
        (community_meet, data_analysis): None,
        (data_analysis, feedback_loop): None,
        (feedback_loop, yield_forecast): None
    }
)

print(root)