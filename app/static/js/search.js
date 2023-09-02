console.log("search.js loaded successfully");
$(document).ready(function () {
	search();
});

async function search() {
	try {
		// prevent default form submission
		$("#search-form").submit(async function (event) {
			event.preventDefault();
			let term = $("#search").val();
			let response = await axios.get('/search', {
                params: {
                    search: term
                }
            });
			
		});
	} catch (error) {
		console.error(error);
	}
}
