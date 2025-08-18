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

# Define control-flow operators
site_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, structural_audit])
permit_filing_loop = OperatorPOWL(operator=Operator.LOOP, children=[permit_filing])
foundation_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[foundation_prep])
frame_build_loop = OperatorPOWL(operator=Operator.LOOP, children=[frame_build])
irrigation_loop = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_setup])
lighting_loop = OperatorPOWL(operator=Operator.LOOP, children=[lighting_install])
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control])
nutrient_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])
crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_planting])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_scouting])
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitoring])
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_sorting])
energy_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit])
community_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet])
yield_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_analysis])

# Define partial order
root = StrictPartialOrder(nodes=[
    site_audit_loop,
    permit_filing_loop,
    foundation_prep_loop,
    frame_build_loop,
    irrigation_loop,
    lighting_loop,
    climate_loop,
    nutrient_loop,
    crop_loop,
    pest_loop,
    data_loop,
    waste_loop,
    energy_loop,
    community_loop,
    yield_loop
])

# Define dependencies
root.order.add_edge(site_audit_loop, permit_filing_loop)
root.order.add_edge(permit_filing_loop, foundation_prep_loop)
root.order.add_edge(foundation_prep_loop, frame_build_loop)
root.order.add_edge(frame_build_loop, irrigation_loop)
root.order.add_edge(irrigation_loop, lighting_loop)
root.order.add_edge(lighting_loop, climate_loop)
root.order.add_edge(climate_loop, nutrient_loop)
root.order.add_edge(nutrient_loop, crop_loop)
root.order.add_edge(crop_loop, pest_loop)
root.order.add_edge(pest_loop, data_loop)
root.order.add_edge(data_loop, waste_loop)
root.order.add_edge(waste_loop, energy_loop)
root.order.add_edge(energy_loop, community_loop)
root.order.add_edge(community_loop, yield_loop)

print(root)