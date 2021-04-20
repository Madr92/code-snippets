set terminal pdf
set output 'd2d.pdf'
set title 'Bitcoin Verdopplungszeit'
set xdata time
set key outside
set timefmt '%Y.%m.%d'
set format x '%Y.%m'
set xtics rotate by -35
set ylabel 'Verdopplungszeit [Tage]'
set ytics nomirror
set y2tics 
set y2label 'Bitcoin Preis [EUR]'
plot 'data.txt' u 1:2 axes x1y1 w l linecolor rgb 'black' title 'd2d','test.txt' u 1:3 axes x1y2 w l linecolor rgb 'red' title 'Preis'
