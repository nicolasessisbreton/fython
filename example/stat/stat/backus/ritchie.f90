module ritchie
	real, bind(c) :: c = 10

	contains

		subroutine compile() bind(c)
			write(*, *) 'c is ', c
		end subroutine

end module