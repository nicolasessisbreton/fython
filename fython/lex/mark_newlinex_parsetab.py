
# mark_newlinex_parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'bofx eofx lpar rpar lket rket newline code\n\tsource\t:\tbofx\n\t\n\tsource \t: \tsource element\n\t\n\telement : \tcode\n\t\t\t| \tnewline\n\t\t\t| \tpar\n\t\t\t|\tket\n\t\n\tsource\t:\tsource eofx\t\n\t\n\tparR \t: \tlpar\n\t\n\tparR \t: \tparR element\n\t\n\tpar : parR rpar\n\t\n\tketR \t: \tlket\n\t\n\tketR \t: \tketR element\n\t\n\tket : ketR rket\n\t'
    
_lr_action_items = {'bofx':([0,],[1,]),'rket':([4,6,7,10,11,12,13,15,16,],[-6,-4,-5,16,-11,-3,-10,-12,-13,]),'$end':([1,2,4,5,6,7,8,12,13,16,],[-1,0,-6,-2,-4,-5,-7,-3,-10,-13,]),'lpar':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[-1,9,9,-6,-2,-4,-5,-7,-8,9,-11,-3,-10,-9,-12,-13,]),'lket':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[-1,11,11,-6,-2,-4,-5,-7,-8,11,-11,-3,-10,-9,-12,-13,]),'rpar':([3,4,6,7,9,12,13,14,16,],[13,-6,-4,-5,-8,-3,-10,-9,-13,]),'newline':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[-1,6,6,-6,-2,-4,-5,-7,-8,6,-11,-3,-10,-9,-12,-13,]),'eofx':([1,2,4,5,6,7,8,12,13,16,],[-1,8,-6,-2,-4,-5,-7,-3,-10,-13,]),'code':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[-1,12,12,-6,-2,-4,-5,-7,-8,12,-11,-3,-10,-9,-12,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'parR':([2,3,10,],[3,3,3,]),'ket':([2,3,10,],[4,4,4,]),'element':([2,3,10,],[5,14,15,]),'ketR':([2,3,10,],[10,10,10,]),'source':([0,],[2,]),'par':([2,3,10,],[7,7,7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> source","S'",1,None,None,None),
  ('source -> bofx','source',1,'p_bofx','mark_newlinex.py',134),
  ('source -> source element','source',2,'p_source','mark_newlinex.py',140),
  ('element -> code','element',1,'p_source_unary','mark_newlinex.py',146),
  ('element -> newline','element',1,'p_source_unary','mark_newlinex.py',147),
  ('element -> par','element',1,'p_source_unary','mark_newlinex.py',148),
  ('element -> ket','element',1,'p_source_unary','mark_newlinex.py',149),
  ('source -> source eofx','source',2,'p_eofx','mark_newlinex.py',155),
  ('parR -> lpar','parR',1,'p_parR','mark_newlinex.py',162),
  ('parR -> parR element','parR',2,'p_par_cont','mark_newlinex.py',168),
  ('par -> parR rpar','par',2,'p_par','mark_newlinex.py',174),
  ('ketR -> lket','ketR',1,'p_ketR','mark_newlinex.py',180),
  ('ketR -> ketR element','ketR',2,'p_ket_cont','mark_newlinex.py',186),
  ('ket -> ketR rket','ket',2,'p_ket','mark_newlinex.py',192),
]
