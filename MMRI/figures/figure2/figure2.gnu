set terminal pdf font "Helvetica, 10"
set output 'figure2.pdf'
set contour
set grid
set dgrid3d
set pm3d
set key outside
set xlabel 'DXY'
set xtics 70,20,170
set ylabel 'TNX'
set zlabel 'MMRI' rotate by 90
set cntrparam levels auto 8
splot 'mmri.txt' u 2:3:4 w l title 'MMRI surface plot'
