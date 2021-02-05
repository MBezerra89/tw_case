# tw_case

A ideia é ter um script principal que irá chamar os outros scripts "coleta de tws, input no bd, ajustes de arquivos e logs para coleta de metricas".

Estou usando como base imagens Docker oficiais, para APP Ubuntu Server, BD Mysql 8.0, Graylog, Grafana.

Script Principal ## em desenvolvimento.
executa o coleta tws ... salvando a saida em um arquivo de log.
Input BD, irá ler esse arquivo linha a linha, aplicar os filtros e salvar resultado em variaveis, para realizar o input nas colunas de forma que facilite o consumo das informações e métricas.

Agradeço a  atenção.
