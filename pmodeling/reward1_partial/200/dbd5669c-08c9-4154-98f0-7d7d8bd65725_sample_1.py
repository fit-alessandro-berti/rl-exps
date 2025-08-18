from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
unit_assembly = Transition(label='Unit Assembly')
system_wiring = Transition(label='System Wiring')
sensor_install = Transition(label='Sensor Install')
water_testing = Transition(label='Water Testing')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
planting_setup = Transition(label='Planting Setup')
climate_control = Transition(label='Climate Control')
pest_management = Transition(label='Pest Management')
data_calibration = Transition(label='Data Calibration')
yield_analysis = Transition(label='Yield Analysis')
community_meet = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
expansion_plan = Transition(label='Expansion Plan')

# Define the partial order (workflow) with dependencies
root = StrictPartialOrder(
    nodes=[site_survey, design_layout, material_sourcing, unit_assembly, system_wiring, sensor_install,
           water_testing, nutrient_mix, seed_selection, planting_setup, climate_control, pest_management,
           data_calibration, yield_analysis, community_meet, compliance_check, expansion_plan],
    order={
        site_survey: [design_layout],
        design_layout: [material_sourcing, unit_assembly],
        material_sourcing: [unit_assembly],
        unit_assembly: [system_wiring, sensor_install],
        system_wiring: [sensor_install],
        sensor_install: [water_testing, nutrient_mix],
        water_testing: [nutrient_mix],
        nutrient_mix: [seed_selection],
        seed_selection: [planting_setup],
        planting_setup: [climate_control, pest_management],
        climate_control: [pest_management],
        pest_management: [data_calibration],
        data_calibration: [yield_analysis],
        yield_analysis: [community_meet, compliance_check],
        community_meet: [compliance_check],
        compliance_check: [expansion_plan]
    }
)

print(root)