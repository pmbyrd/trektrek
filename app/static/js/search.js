console.log("search.js loaded successfully");
$(document).ready(function () {
	searchPost();
});

// async function search() {
// 	try {
// 		// prevent default form submission
// 		$("#search-form").submit(async function (event) {
// 			event.preventDefault();
// 			let term = $("#search").val();
// 			console.log(term);
// 			let response = await axios.get('/search', {
//                 params: {
//                     search: term
//                 }
//             });
// 			console.log(response);
// 		});
// 	} catch (error) {
// 		console.error(error);
// 	}
// }

async function searchPost() {
	try {
		// prevent default form submission
		$("#search-form").submit(async function (event) {
			event.preventDefault();
			let term = $("#search").val();
			let searchType = $("#search_type").val();
			if (term.trim() === "") {
				displayMessages("Please enter a search term");
			}
			// if the the section option is "all", then return early
			else if (searchType === "all") {
				displayMessages("Please select a search option");
			} else {
				let response = await axios.post("/search-post", {
					params: {
						search: term,
						field: searchType,
					},
				});
				let results = response.data.results[0];
				$(".results").empty();
				// for each result append a link to the results name
				if (searchType === "characters") {
					for (let result of results) {
						let $result = `
							<li><a href="/universe/characters/${result.name}">${result.name}</a></li>
						`;
						$(".results").append($result);
					}
				} else if (searchType === "performers") {
					for (let result of results) {
						let $result = `
							<li><a href="/media/performer/${result.name}">${result.name}</a></li>
						`;
						$(".results").append($result);
					}
				}
			}
			console.log(term, searchType);
		});
	} catch (error) {
		console.error(error);
	}
}

function displayMessages(str) {
	// only show the message for 3 seconds
	$(".errors").append(`<p class="go-mars">${str}</p>`);
	console.log("displaying message");
	setTimeout(() => {
		$(".errors").empty();
	}, 3000);
}
