submodule (m2) m3

contains

module procedure std_deviation
	call cube_mean(x, y, z, u)
	r=x-u

end procedure


end submodule