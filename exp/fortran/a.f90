
module a

contains 

subroutine g()
	integer x(10)
	write(*, *) size(x), size(x+10+8)
end subroutine

end module
