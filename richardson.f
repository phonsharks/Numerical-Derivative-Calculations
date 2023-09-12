program richardson
    implicit none
    integer, parameter :: n = 5
    integer :: i, j
    real :: xo, h, ri(n,n), l, k, m, f, exact

    h = 0.2; xo = 2.0; k = n; m = 0
    exact = (xo+1)*exp(xo)

    do i = 1, n
        do j = 1, k
            l = 2**(j-1)
            h = 0.2
            h = h/l
            ri(j+m,i) = h
            ri(j,1) = (f(xo+h)-f(xo-h))/(2*h)
        end do
        m = m + 1
        k = k - 1
    end do

    do j = 2, n
        do i = j, n
            ri(i,j)=ri(i,j-1)+(ri(i,j-1)-ri(i-1,j-1))/(4**(j-1)-1)!Richardson Theorem
        end do
    end do

    write(*,*)"            Extrapolation table for Richardson is shown bellow"
    write(*,*)"            =================================================="
    write(*,*)"     O(h2)     ","      O(h4)   ","      O(h6)     ","     O(h8)     ","     O(h10)     "
    write(*,*)"   --------    ","    --------  ","    --------    ","   --------    ","   ---------    "
    k = n
    do i= 1, k
        write(*,'(5f15.8)')(ri(i,j), j = 1, i)!For table
        k = k + 1
    end do


!   write(*,'(2/, A80)')"Order of (h)       approximate value       exact result       relative error"
!	write(*,'(I10, F25.8, F23.8, F20.8)')6, ri(n,3), exact, abs(ri(n,3)-exact)
!   write(*,'(I10, F25.8, F23.8, F20.8)')8, ri(n,4), exact, abs(ri(n,4)-exact)
!    write(*,'(I10, F25.8, F23.8, F20.8)')10, ri(n,n), exact, abs(ri(n,n)-exact)

end program

function f(x)
    real :: x, f

    f = x*exp(x)

end function
