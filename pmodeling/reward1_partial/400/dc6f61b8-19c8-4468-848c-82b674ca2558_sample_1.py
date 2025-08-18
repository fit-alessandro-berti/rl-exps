import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define activities
site_survey = Transition(label='Site Survey')
energy_partner = Transition(label='Energy Partner')
permit_filing = Transition(label='Permit Filing')
hydro_unit = Transition(label='Hydro Unit')
ai_setup = Transition(label='AI Setup')
nutrient_plan = Transition(label='Nutrient Plan')
system_install = Transition(label='System Install')
crop_testing = Transition(label='Crop Testing')
data_analysis = Transition(label='Data Analysis')
community_meet = Transition(label='Community Meet')
yield_adjust = Transition(label='Yield Adjust')
carbon_audit = Transition(label='Carbon Audit')
logistics_plan = Transition(label='Logistics Plan')
quality_check = Transition(label='Quality Check')
scale_review = Transition(label='Scale Review')

# Add activities to the root model
root.add_transition(site_survey)
root.add_transition(energy_partner)
root.add_transition(permit_filing)
root.add_transition(hydro_unit)
root.add_transition(ai_setup)
root.add_transition(nutrient_plan)
root.add_transition(system_install)
root.add_transition(crop_testing)
root.add_transition(data_analysis)
root.add_transition(community_meet)
root.add_transition(yield_adjust)
root.add_transition(carbon_audit)
root.add_transition(logistics_plan)
root.add_transition(quality_check)
root.add_transition(scale_review)

# Define dependencies between activities
root.add_edge(site_survey, energy_partner)
root.add_edge(energy_partner, permit_filing)
root.add_edge(permit_filing, hydro_unit)
root.add_edge(hydro_unit, ai_setup)
root.add_edge(ai_setup, nutrient_plan)
root.add_edge(nutrient_plan, system_install)
root.add_edge(system_install, crop_testing)
root.add_edge(crop_testing, data_analysis)
root.add_edge(data_analysis, community_meet)
root.add_edge(community_meet, yield_adjust)
root.add_edge(yield_adjust, carbon_audit)
root.add_edge(carbon_audit, logistics_plan)
root.add_edge(logistics_plan, quality_check)
root.add_edge(quality_check, scale_review)

# Print the root model
print(root)