import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their names
site_survey = Transition(label='Site Survey')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
system_assembly = Transition(label='System Assembly')
climate_setup = Transition(label='Climate Setup')
nutrient_prep = Transition(label='Nutrient Prep')
irrigation_test = Transition(label='Irrigation Test')
lighting_config = Transition(label='Lighting Config')
energy_install = Transition(label='Energy Install')
sensor_setup = Transition(label='Sensor Setup')
automation_deploy = Transition(label='Automation Deploy')
crop_seeding = Transition(label='Crop Seeding')
waste_plan = Transition(label='Waste Plan')
staff_training = Transition(label='Staff Training')
community_outreach = Transition(label='Community Outreach')
yield_monitor = Transition(label='Yield Monitor')
maintenance_check = Transition(label='Maintenance Check')

# Define the workflow structure
root = StrictPartialOrder(
    nodes=[
        site_survey,
        permit_review,
        design_layout,
        system_assembly,
        climate_setup,
        nutrient_prep,
        irrigation_test,
        lighting_config,
        energy_install,
        sensor_setup,
        automation_deploy,
        crop_seeding,
        waste_plan,
        staff_training,
        community_outreach,
        yield_monitor,
        maintenance_check
    ],
    order={
        # Define dependencies between activities
        site_survey: [permit_review, design_layout],
        permit_review: [design_layout],
        design_layout: [system_assembly, climate_setup],
        system_assembly: [climate_setup],
        climate_setup: [nutrient_prep, irrigation_test, lighting_config, energy_install],
        nutrient_prep: [irrigation_test, lighting_config, energy_install],
        irrigation_test: [lighting_config, energy_install],
        lighting_config: [energy_install],
        energy_install: [sensor_setup, automation_deploy],
        sensor_setup: [automation_deploy],
        automation_deploy: [crop_seeding, waste_plan],
        crop_seeding: [staff_training, community_outreach],
        staff_training: [community_outreach],
        community_outreach: [yield_monitor, maintenance_check],
        yield_monitor: [maintenance_check],
        maintenance_check: [site_survey]
    }
)

# Example usage:
# print(pm4py.format_dataframe(root, format='powl'))