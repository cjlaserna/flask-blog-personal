const form = document.getElementById('form');
form.addEventListener('submit', function(e) {
	e.preventDefault();

	const payload = new FormData(form);
	
	fetch('./api/timeline_post', {
	method: 'POST',
	body: payload,
	})
	.then(() => window.location.reload());
})
