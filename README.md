# FSM

Автомат доволі лінійний, проте містить багато зовнішних подій які впливають на подальші
Послідовність станів:

-> start -> _sleeping -> _awake -> _on_lesson -> _free_in_ucu -> _gym -> _home -> _go_to_bed -> end

Є також шлях _awake -> _free_in_ucu

## Є два параметра:
1. Година
2. Енергія

## Стани:
1. _sleeping - може проснутися рандомно о 10 або 8 ранку
2. _awake - іде на пару якщо встав о 8, просто їде в УКУ якщо о 10
3. _on_lesson - може рандомно захотіти проявити себе на парі, що забере 20 енергії
4. _free_in_ucu - на цей момент завжди 20 дня. Може на вибір порозважатися з друзями (+2 години + 10 енергії), поїсти в трапезній (+20 енергії +2 години), зробити домашнє (+4 години -40 енергії)
5. _gym - завжди туди переходить після 18 години, дається можливість тренувати три групи м'язів, дві забирають по  20 енергії, одна 50. Витрачає завжди 3 години
6. _home - якщо дз не зроблене і енергія > 50, зробить її потративши 4 години і 40 енергії, якшо нема енергії, то витрачає час дарма і йде спати за 2 години, якщо дз зроблене і раніше ніж 21 вечора, розважається і назбирує 20 енергії, інакше іде спати.
7. _go_to_bed - виводяться підсумки дня і закінчується автомат
