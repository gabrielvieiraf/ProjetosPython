<h1>Integração da API do Movidesk com PYTHON e requests</h1>

<h2>TICKETS</h2>

<h3>A API utiliza o protocolo aberto OData. Os filtros possíveis são:</h3>

<li> <strong>$filter:</strong> A expressão especificada com esse filtro é avaliada para cada item do retorno da consulta e somente os itens em que o resultado da expressão for verdadeiro serão incluídos no retorno final;</li>
<li> <strong>$orderby:</strong> Permite que os itens do retorno da consulta sejam ordenados de forma ascendente (asc) ou descendente (desc). Se não for especificado asc ou desc, o padrão será asc;</li>
<li> <strong>$top:</strong> Permite especificar o número de itens que devem ser incluídos no retorno da consulta;</li>
<li> <strong>$skip:</strong> Permite especificar a quantidade de itens que devem ser ignorados e não incluídos no retorno da consulta;</li>
<li> <strong>$select:</strong> Permite especificar propriedades especificas dos itens que devem ser preenchidas no retorno da consulta;</li>
<li> <strong>$expand:</strong> Permite expandir as coleções filhas dos itens consultados.</li>
