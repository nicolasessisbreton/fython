
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '5B46638E919CCEBCA535E626C60A23DF'
    
_lr_action_items = {'$end':([1,2,3,4,5,],[0,-3,-2,-1,-4,]),'SYMBOL':([0,1,2,3,4,5,],[2,2,-3,-2,-1,-4,]),'COUNT':([2,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'chemical_equation':([0,],[1,]),'species':([0,1,],[3,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> chemical_equation","S'",1,None,None,None),
  ('chemical_equation -> chemical_equation species','chemical_equation',2,'p_species_list','dalke_1.py',40),
  ('chemical_equation -> species','chemical_equation',1,'p_species','dalke_1.py',44),
  ('species -> SYMBOL','species',1,'p_single_species','dalke_1.py',49),
  ('species -> SYMBOL COUNT','species',2,'p_single_species','dalke_1.py',50),
]
