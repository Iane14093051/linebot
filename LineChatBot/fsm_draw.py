from transitions.extensions import GraphMachine
from functools import partial


class Model:

    def clear_state(self, deep=False, force=False):
        print("Clearing state ...")
        return True


model = Model()
machine = GraphMachine(model=model, states=[ 'choose',
    'choose',
        'help_old_people',
        'location',
        'lose_money_money',
        'lose_money_time',
        'lose_money_result',
        'information'
        ],
                       transitions=[
                           {'trigger': 'advance', 'source': 'user', 'dest': 'choose', 'conditions': 'is_going_to_choose'},
        {'trigger': 'advance', 'source': 'choose', 'dest': 'help_old_people', 'conditions': 'is_going_to_help_old_people'},
        {'trigger': 'advance', 'source': 'choose', 'dest': 'location', 'conditions': 'is_going_to_location'},
         {'trigger': 'advance', 'source': 'choose', 'dest': 'information', 'conditions': 'is_going_to_information'},
        
        
        {'trigger': 'advance', 'source': 'choose', 'dest': 'lose_money_money', 'conditions': 'is_going_to_lose_money_money'},
        
        
        {'trigger': 'advance', 'source': 'lose_money_money', 'dest': 'lose_money_time', 'conditions':'is_going_to_lose_money_time'},
        
        {'trigger': 'advance', 'source': 'lose_money_time', 'dest': 'lose_money_result', 'conditions': 'is_going_to_lose_money_result'},
        
        
        
        
          {'trigger': 'advance', 'source': 'help_old_people', 'dest': 'choose', 'conditions': 'go_back'},
          {'trigger': 'advance', 'source': 'location', 'dest': 'choose', 'conditions': 'go_back'},
          {'trigger': 'advance', 'source':  'lose_money_result', 'dest': 'choose', 'conditions': 'go_back'},
          {'trigger': 'advance', 'source':  'information', 'dest': 'choose', 'conditions': 'go_back'},
                       ],
                       initial='user', show_conditions=True)

model.get_graph().draw('my_state_diagram.png', prog='dot')
