# base
class FyException(Exception):
	def __init__(s, message):
		s.message = '\n;;;;;\n'
		s.message += s.__class__.__name__.replace('_', ' ')
		s.message += '\n'
		s.message += str(message)

	def __str__(s):
		return s.message

# exception
class a_function_cannot_be_dotted(FyException):
	pass

class cannot_indent_on_first_line(FyException):
	pass

class cannot_find_attribute_in_class(FyException):
	pass

class cannot_find_attribute_setter_in_class(FyException):
	pass

class cannot_find_targetted_ast(FyException):
	pass
	
class cannot_mix_args_and_kwargs(FyException):
	pass

class cannot_overwrite_spec(FyException):
	pass

class cannot_resolve_modifier(FyException):
	pass

class cannot_set_reference_with_a_property_setter(FyException):
	pass

class cannot_find_class_definition_in_module(FyException):
	pass

class compilation_error(FyException):
	pass

class else_without_if_elif_where_or_elwhere(FyException):
	pass

class error_in_interpolant(FyException):
	pass

class guid_override_error(FyException):
	pass

class indentation_increased_by_more_than_one_level(FyException):
	pass

class indentation_without_colon(FyException):
	pass

class inconsistent_mro(FyException):
	pass

class intrinsic_type_cannot_be_dotted(FyException):
	pass

class invalid_url(FyException):
		pass
		
class left_element_in_aliased_import_is_not_an_url(FyException):
	pass

class interpretation_error(FyException):
	pass

class lexical_interpolation_is_only_on_routine_or_class(FyException):
	pass
	
class linking_error(FyException):
	pass

class mark_newlinex_lexing_error(FyException):
	pass

class mixed_indentation(FyException):
	pass

class nb_of_arguments_mismatch(FyException):
	pass

class no_element_specified_in_slice_import(FyException):
	pass

class no_fortran_compiler_found(FyException):
	pass

class only_aliased_namespace_star_or_slice_import_are_allowed(FyException):
	pass	

class only_attribute_or_method_can_be_inherited(FyException):
		pass
		
class only_star_import_allowed_for_shared_library(FyException):
	pass	

class only_star_or_slice_import_allowed_for_fortran(FyException):
	pass

class python_import_error(FyException):
	pass

class space_tab_mixed(FyException):
	pass

class syntax_error(FyException):
	pass

class unbalanced_parenthesis(FyException):
	pass

class fml_error(FyException):
	pass

class module_not_found(FyException):
	pass

class name_not_found_in_fython_module(FyException):
	pass

class package_not_found(FyException):
	pass

class resolution_error(FyException):
	pass
	
class string_format_error(FyException):
	pass

class unknown_identifier(FyException):
	pass

class unknown_print_mode(FyException):
	pass
