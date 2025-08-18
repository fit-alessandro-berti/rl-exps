import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_to_design_layout = OperatorPOWL(operator=Operator.XOR, children=[permits_check, skip])
design_layout_to_foundation_prep = OperatorPOWL(operator=Operator.XOR, children=[foundation_prep, skip])
foundation_prep_to_frame_assembly = OperatorPOWL(operator=Operator.XOR, children=[frame_assembly, skip])
frame_assembly_to_hydro_setup = OperatorPOWL(operator=Operator.XOR, children=[hydro_setup, skip])
hydro_setup_to_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])
climate_setup_to_seed_selection = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, skip])
seed_selection_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
nutrient_mix_to_system_calibration = OperatorPOWL(operator=Operator.XOR, children=[system_calibration, skip])
system_calibration_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
pest_control_to_automation_link = OperatorPOWL(operator=Operator.XOR, children=[automation_link, skip])
automation_link_to_staff_training = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
staff_training_to_yield_tracking = OperatorPOWL(operator=Operator.XOR, children=[yield_tracking, skip])
yield_tracking_to_distribution_plan = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, skip])

root = StrictPartialOrder(nodes=[
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
])

root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, foundation_prep)
root.order.add_edge(foundation_prep, frame_assembly)
root.order.add_edge(frame_assembly, hydro_setup)
root.order.add_edge(hydro_setup, climate_setup)
root.order.add_edge(climate_setup, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, system_calibration)
root.order.add_edge(system_calibration, pest_control)
root.order.add_edge(pest_control, automation_link)
root.order.add_edge(automation_link, staff_training)
root.order.add_edge(staff_training, yield_tracking)
root.order.add_edge(yield_tracking, distribution_plan)

print(root)