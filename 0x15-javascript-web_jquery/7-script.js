$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (ddata) {
	$('DIV#character').text(data.name);
});
