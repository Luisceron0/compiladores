grammar CSVFilter;

prog: stat+ ;

stat
    : loadStat
    | filterStat
    | printStat
    ;

loadStat: 'load' STRING ';' ;
filterStat: 'filter' 'column' STRING OPERATOR INT ';' ;
printStat: 'print' ';' ;

OPERATOR: '>' | '<' | '==' ;
STRING: '"' (~["\r\n])* '"' ;
INT: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;