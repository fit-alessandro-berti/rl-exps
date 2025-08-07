from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_sample = Transition(label='Soil Sample')
climate_check = Transition(label='Climate Check')
crop_select = Transition(label='Crop Select')
irrigation_plan = Transition(label='Irrigation Plan')
energy_setup = Transition(label='Energy Setup')
pest_control = Transition(label='Pest Control')
permit_obtain = Transition(label='Permit Obtain')
stakeholder_meet = Transition(label='Stakeholder Meet')
bed_construction = Transition(label='Bed Construction')
seed_planting = Transition(label='Seed Planting')
water_schedule = Transition(label='Water Schedule')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
yield_report = Transition(label='Yield Report')

# Define silent activities
skip = SilentTransition()

# Define sub-processes
site_assessment = OperatorPOWL(operator=Operator.XOR, children=[site_survey, load_test])
soil_analysis = OperatorPOWL(operator=Operator.XOR, children=[soil_sample, climate_check])
crop_selection = OperatorPOWL(operator=Operator.XOR, children=[crop_select, energy_setup])
pest_management = OperatorPOWL(operator=Operator.XOR, children=[pest_control, permit_obtain])
community_engagement = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, waste_recycle])
maintenance = OperatorPOWL(operator=Operator.XOR, children=[bed_construction, seed_planting])
irrigation_system = OperatorPOWL(operator=Operator.XOR, children=[irrigation_plan, water_schedule])
yield_monitoring = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, harvest_plan])

# Define loops and partial orders
site_assessment_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_assessment])
soil_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_analysis])
crop_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[crop_selection])
pest_management_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_management])
community_engagement_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_engagement])
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance])
irrigation_system_loop = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_system])
yield_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitoring])

# Define the root process
root = StrictPartialOrder(nodes=[
    site_assessment_loop,
    soil_analysis_loop,
    crop_selection_loop,
    pest_management_loop,
    community_engagement_loop,
    maintenance_loop,
    irrigation_system_loop,
    yield_monitoring_loop
])

# Add dependencies between nodes
root.order.add_edge(site_assessment_loop, soil_analysis_loop)
root.order.add_edge(soil_analysis_loop, crop_selection_loop)
root.order.add_edge(crop_selection_loop, pest_management_loop)
root.order.add_edge(pest_management_loop, community_engagement_loop)
root.order.add_edge(community_engagement_loop, maintenance_loop)
root.order.add_edge(maintenance_loop, irrigation_system_loop)
root.order.add_edge(irrigation_system_loop, yield_monitoring_loop)

# Save the final result in the variable 'root'