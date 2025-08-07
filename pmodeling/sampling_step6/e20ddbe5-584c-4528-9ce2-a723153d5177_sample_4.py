from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

# Define the activities as POWL transitions
site_analysis = Transition(label='Site Analysis')
load_test = Transition(label='Load Test')
sunlight_map = Transition(label='Sunlight Map')
medium_select = Transition(label='Medium Select')
hydro_design = Transition(label='Hydro Design')
procure_seeds = Transition(label='Procure Seeds')
install_irrigation = Transition(label='Install Irrigation')
setup_climate = Transition(label='Setup Climate')
create_schedule = Transition(label='Create Schedule')
pest_control = Transition(label='Pest Control')
monitor_growth = Transition(label='Monitor Growth')
adjust_systems = Transition(label='Adjust Systems')
harvest_crops = Transition(label='Harvest Crops')
package_produce = Transition(label='Package Produce')
engage_community = Transition(label='Engage Community')
host_workshops = Transition(label='Host Workshops')

# Define the partial order of activities
root = StrictPartialOrder(nodes=[site_analysis, load_test, sunlight_map, medium_select, hydro_design, procure_seeds, install_irrigation, setup_climate, create_schedule, pest_control, monitor_growth, adjust_systems, harvest_crops, package_produce, engage_community, host_workshops])

# Add dependencies between activities if needed
# For example, if Site Analysis must precede Load Test, add the edge:
# root.order.add_edge(site_analysis, load_test)

# You can further customize the dependencies based on the actual process flow