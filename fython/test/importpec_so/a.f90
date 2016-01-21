module a

	contains

		function x_a() result(r) bind(c)
			real r
			r = 10
		end function

end module