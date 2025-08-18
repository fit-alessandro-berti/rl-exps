from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
system_design = Transition(label='System Design')
permit_filing = Transition(label='Permit Filing')
foundation_prep = Transition(label='Foundation Prep')
frame_build = Transition(label='Frame Build')
irrigation_setup = Transition(label='Irrigation Setup')
lighting_install = Transition(label='Lighting Install')
climate_control = Transition(label='Climate Control')
nutrient_mix = Transition(label='Nutrient Mix')
crop_planting = Transition(label='Crop Planting')
pest_scouting = Transition(label='Pest Scouting')
data_monitoring = Transition(label='Data Monitoring')
waste_sorting = Transition(label='Waste Sorting')
energy_audit = Transition(label='Energy Audit')
community_meet = Transition(label='Community Meet')
yield_analysis = Transition(label='Yield Analysis')

# Define the process tree structure
root = StrictPartialOrder(
    nodes=[site_survey, structural_audit, system_design, permit_filing, foundation_prep, frame_build, irrigation_setup, lighting_install, climate_control, nutrient_mix, crop_planting, pest_scouting, data_monitoring, waste_sorting, energy_audit, community_meet, yield_analysis],
    order=[
        (site_survey, structural_audit),
        (structural_audit, system_design),
        (system_design, permit_filing),
        (permit_filing, foundation_prep),
        (foundation_prep, frame_build),
        (frame_build, irrigation_setup),
        (irrigation_setup, lighting_install),
        (lighting_install, climate_control),
        (climate_control, nutrient_mix),
        (nutrient_mix, crop_planting),
        (crop_planting, pest_scouting),
        (pest_scouting, data_monitoring),
        (data_monitoring, waste_sorting),
        (waste_sorting, energy_audit),
        (energy_audit, community_meet),
        (community_meet, yield_analysis)
    ]
)

# Print the root of the POWL model
print(root)