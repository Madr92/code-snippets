#Dies ist das Skript für das Erstellen der pdf-Datei aus den Daten, die das Skript erstellt!

set terminal pdf
set output 'dominance.pdf'
set title 'Bitcoin Dominanz (Top 3 Coins)'
set xlabel 'Zeit'
set ylabel 'Dominanz in %'
set xdata time
set timefmt '%Y.%m.%d %H:%M:%S'
set format x '%Y.%m.%d'
plot 'data.txt' u 1:3 w l notitle
