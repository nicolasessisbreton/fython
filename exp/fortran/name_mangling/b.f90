
module b
use a._

! integer :: x

contains

subroutine f()
	integer y
	y = a_mp_x_ + 1 + x
end subroutine

end module
