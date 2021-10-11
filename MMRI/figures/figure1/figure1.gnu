set terminal pdf
set output 'figure1.pdf'
set multiplot
set origin 0,0.5
set size 0.5,0.5
set xdata time
set timefmt '%Y-%m-%d'
set format x '%Y-%m'
set xtics rotate by -45
plot 'mmri.txt' u 1:3  w l linecolor rgb 'red' title 'TNX'

set origin 0,0
set size 0.5,0.5
#set ytics 70,20,170
set xdata time
set timefmt '%Y-%m-%d'
set format x '%Y-%m'
set xtics rotate by -45
plot 'mmri.txt' u 1:2  w l linecolor rgb 'black' title 'DXY'


set origin 0.525,0
set size 0.45,1
set xdata time
set timefmt '%Y-%m-%d'
set format x '%Y-%m'
set xtics rotate by -45
set yrange [0:1200]
set object rect from '1973-11-01',0 to '1975-03-01',1200  fc rgb 'grey'
set object rect from '1980-01-01',0 to '1980-07-01',1200  fc rgb 'grey'
set object rect from '1981-07-01',0 to '1982-11-01',1200  fc rgb 'grey'
set object rect from '1990-07-01',0 to '1991-02-01',1200  fc rgb 'grey'
set object rect from '2001-03-01',0 to '2001-11-01',1200  fc rgb 'grey'
set object rect from '2007-12-01',0 to '2009-06-01',1200  fc rgb 'grey'
set object rect from '2020-02-01',0 to '2020-04-01',1200  fc rgb 'grey'
plot 'mmri.txt' u 1:4  w l linecolor rgb 'blue' title 'MMRI'
unset multiplot
