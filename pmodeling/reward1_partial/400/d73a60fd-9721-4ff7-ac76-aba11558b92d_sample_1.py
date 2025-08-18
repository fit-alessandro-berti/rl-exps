import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_audit,
    system_design,
    permit_filing,
    foundation_prep,
    frame_build,
    irrigation_setup,
    lighting_install,
    climate_control,
    nutrient_mix,
    crop_planting,
    pest_scouting,
    data_monitoring,
    waste_sorting,
    energy_audit,
    community_meet,
    yield_analysis
])

# Define dependencies
root.order.add_edge(site_survey, structural_audit)
root.order.add_edge(structural_audit, system_design)
root.order.add_edge(system_design, permit_filing)
root.order.add_edge(permit_filing, foundation_prep)
root.order.add_edge(foundation_prep, frame_build)
root.order.add_edge(frame_build, irrigation_setup)
root.order.add_edge(irrigation_setup, lighting_install)
root.order.add_edge(lighting_install, climate_control)
root.order.add_edge(climate_control, nutrient_mix)
root.order.add_edge(nutrient_mix, crop_planting)
root.order.add_edge(crop_planting, pest_scouting)
root.order.add_edge(pest_scouting, data_monitoring)
root.order.add_edge(data_monitoring, waste_sorting)
root.order.add_edge(waste_sorting, energy_audit)
root.order.add_edge(energy_audit, community_meet)
root.order.add_edge(community_meet, yield_analysis)

print(root)