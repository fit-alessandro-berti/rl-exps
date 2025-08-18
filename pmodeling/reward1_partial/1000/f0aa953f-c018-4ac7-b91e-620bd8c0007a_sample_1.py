from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_assembly = Transition(label='System Assembly')
climate_setup = Transition(label='Climate Setup')
light_calibration = Transition(label='Light Calibration')
seed_selection = Transition(label='Seed Selection')
seedling_prep = Transition(label='Seedling Prep')
nutrient_mix = Transition(label='Nutrient Mix')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
data_integration = Transition(label='Data Integration')
waste_routing = Transition(label='Waste Routing')
energy_audit = Transition(label='Energy Audit')
regulation_check = Transition(label='Regulation Check')
operational_test = Transition(label='Operational Test')
community_outreach = Transition(label='Community Outreach')

# Define the process model
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_layout,
        system_assembly,
        climate_setup,
        light_calibration,
        seed_selection,
        seedling_prep,
        nutrient_mix,
        irrigation_setup,
        sensor_install,
        data_integration,
        waste_routing,
        energy_audit,
        regulation_check,
        operational_test,
        community_outreach
    ],
    order={
        site_survey: [design_layout],
        design_layout: [system_assembly],
        system_assembly: [climate_setup],
        climate_setup: [light_calibration],
        light_calibration: [seed_selection],
        seed_selection: [seedling_prep],
        seedling_prep: [nutrient_mix],
        nutrient_mix: [irrigation_setup],
        irrigation_setup: [sensor_install],
        sensor_install: [data_integration],
        data_integration: [waste_routing],
        waste_routing: [energy_audit],
        energy_audit: [regulation_check],
        regulation_check: [operational_test],
        operational_test: [community_outreach]
    }
)

# Add any additional dependencies or transitions as needed