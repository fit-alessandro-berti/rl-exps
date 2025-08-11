import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
begin_onboarding = Transition(label='Begin onboarding process')
identify_need = Transition(label='Identify need for new hire')
post_job_description = Transition(label='Post job description')
screen_resumes = Transition(label='Screen resumes')
create_job_description = Transition(label='Create job description')
conduct_initial_phone_interviews = Transition(label='Conduct initial phone interviews')
conduct_virtual_interview = Transition(label='Conduct a virtual interview')
conduct_in_person_interview = Transition(label='Conduct an in-person interview')
extend_offer = Transition(label='Extend offer')
negotiate_salary = Transition(label='Negotiate salary')
complete_paperwork = Transition(label='Complete paperwork')
complete_orientation = Transition(label='Complete orientation')
complete_training = Transition(label='Complete training')
choose_candidate = Transition(label='Choose candidate')
invite_candidates = Transition(label='Invite candidates for interviews')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    begin_onboarding,
    identify_need,
    post_job_description,
    screen_resumes,
    create_job_description,
    conduct_initial_phone_interviews,
    conduct_virtual_interview,
    conduct_in_person_interview,
    extend_offer,
    negotiate_salary,
    complete_paperwork,
    complete_orientation,
    complete_training,
    choose_candidate,
    invite_candidates
])

# Define the dependencies
root.order.add_edge(identify_need, post_job_description)
root.order.add_edge(post_job_description, screen_resumes)
root.order.add_edge(screen_resumes, create_job_description)
root.order.add_edge(create_job_description, conduct_initial_phone_interviews)
root.order.add_edge(conduct_initial_phone_interviews, conduct_virtual_interview)
root.order.add_edge(conduct_initial_phone_interviews, conduct_in_person_interview)
root.order.add_edge(conduct_virtual_interview, extend_offer)
root.order.add_edge(conduct_in_person_interview, extend_offer)
root.order.add_edge(extend_offer, negotiate_salary)
root.order.add_edge(negotiate_salary, complete_paperwork)
root.order.add_edge(complete_paperwork, complete_orientation)
root.order.add_edge(complete_orientation, complete_training)
root.order.add_edge(complete_training, choose_candidate)
root.order.add_edge(choose_candidate, invite_candidates)