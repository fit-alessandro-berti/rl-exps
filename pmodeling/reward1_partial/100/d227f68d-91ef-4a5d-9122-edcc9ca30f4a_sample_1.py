from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permits_check = Transition(label='Permits Check')
foundation_prep = Transition(label='Foundation Prep')
frame_assembly = Transition(label='Frame Assembly')
hydro_setup = Transition(label='Hydro Setup')
climate_setup = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
system_calibration = Transition(label='System Calibration')
pest_control = Transition(label='Pest Control')
automation_link = Transition(label='Automation Link')
staff_training = Transition(label='Staff Training')
yield_tracking = Transition(label='Yield Tracking')
distribution_plan = Transition(label='Distribution Plan')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_layout,
        permits_check,
        foundation_prep,
        frame_assembly,
        hydro_setup,
        climate_setup,
        seed_selection,
        nutrient_mix,
        system_calibration,
        pest_control,
        automation_link,
        staff_training,
        yield_tracking,
        distribution_plan
    ],
    order={
        site_survey: [design_layout],
        design_layout: [permits_check],
        permits_check: [foundation_prep],
        foundation_prep: [frame_assembly],
        frame_assembly: [hydro_setup],
        hydro_setup: [climate_setup],
        climate_setup: [seed_selection],
        seed_selection: [nutrient_mix],
        nutrient_mix: [system_calibration],
        system_calibration: [pest_control],
        pest_control: [automation_link],
        automation_link: [staff_training],
        staff_training: [yield_tracking],
        yield_tracking: [distribution_plan]
    }
)

# Print the root to verify
print(root)