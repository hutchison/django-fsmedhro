/*
 * Durchsucht alle von `selector` betroffenen Elemente, ob `query` (nach trim
 * und toLowerCase) im html-Text vorhanden ist und führt bei einem Treffer
 * f_match und sonst f_miss auf die Elemente aus.
 *
 * Bsp:
 * 	filter(".fragentext", v, elem => $(elem).parents('.frage').show(), elem => $(elem).parents('.frage').hide());
 * */
function filter(selector, query, f_match, f_miss) {
	query = query.trim().toLowerCase();
	$(selector).each(function() {
		if ($(this).html().toLowerCase().search(query) >= 0) {
			f_match(this);
		} else {
			f_miss(this);
		}
	});
}
