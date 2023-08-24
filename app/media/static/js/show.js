console.log("show.js loaded");

const title = $("#show-title").text();
console.log(title);

async function getShowsByTerm(searchQuery) {
	// ADD: Remove placeholder & make request to TVMaze search shows API.
	//the JSON will need to be parsed
	const response = await axios.get(
		`http://api.tvmaze.com/search/shows?q=${searchQuery}`
	);
	// I want to store the the key value pairs for each show to be handled later
	const shows = response.data.map(function (value) {
		const show = value.show;
		return {
			id: show.id,
			name: show.name,
			summary: show.summary,
			externals: [
				show.externals.imdb,
				show.externals.thetvdb,
				show.externals.tvrage,
			],
			genres: show.genres,
			image: show.image ? show.image.medium : defaultLink, //handle for if a link is no available
		};
	});
	return (show = shows[0]);
}

async function getCastTvMaze(id) {
	const res = await getShowsByTerm(title);
	id = res.id;
	const response = await axios.get(`http://api.tvmaze.com/shows/${id}/cast`);
	const cast = response.data.map(function (value) {
		return {
			id: value.person.id,
			name: value.person.name,
			character: value.character.name,
			image: value.person.image ? value.person.image.medium : defaultLink,
			characterImage: value.character.image
				? value.character.image.medium
				: defaultLink,
		};
	});
	return cast;
}

async function getSeasons(id) {
	try {
		const res = await getShowsByTerm(title);
		id = res.id;
		const response = await axios.get(
			`http://api.tvmaze.com/shows/${id}/seasons`
		);
		const seasons = response.data.map(function (value) {
			return {
				id: value.id,
				number: value.number,
				image: value.image ? value.image.medium : defaultLink,
				premiereDate: value.premiereDate,
				endDate: value.endDate,
			};
		});
		return seasons;
	} catch (error) {
		console.error(error);
	}
}
// get the show by title
//from that show get the id
//use the show season id to get the episodes
async function getEpisodes(seasonId) {
	try {
		if (seasonId) {
			let response = await axios.get(
				`http://api.tvmaze.com/seasons/${seasonId}/episodes?embed=guestcast`
			);
			let episodes = response.data.map(function (value) {
				let guestcastCharacters = value._embedded.guestcast.map(
					(guest) => guest.character.name
				);

				return {
					id: value.id,
					name: value.name,
					season: value.season,
					number: value.number,
					airdate: value.airdate,
					airtime: value.airtime,
					airstamp: value.airstamp,
					runtime: value.runtime,
					image: value.image ? value.image.medium : defaultLink,
					summary: value.summary,
					guestcast: guestcastCharacters, // Set guestcast to the array of character names
				};
			});
			console.log(episodes);
			return episodes;
		}
	} catch (error) {
		console.error(error);
	}
}

async function displayShow(title) {
	console.debug("displayShow");
	try {
		let show = await getShowsByTerm(title);
		// debugger
		let $showCard = $(`
                <div class="card">
                    <div class="img-conatiner">
                        <img src="${show.image}" class="card-img-top" alt="...">
                    </div>

                    <div class="card-body-container">
                        <p class="card-text">${show.summary}</p>
                    </div>
            `);
		$(".show-card-container").append($showCard);
	} catch (error) {
		console.error(error);
	}
}

async function displayCast(title) {
	console.debug("displayCast");
	try {
		let cast = await getCastTvMaze(title);
		for (let actor of cast) {
			let $castCard = $(`
                <li class="actor-cast-card">
                    <div class="actor-card-container">
                        <div class="actor-img-container">
                            <img src="${actor.image}" class="card-img-top" alt="...">
                            <p class="actor-name">Actor: <a href="/media/performer/${actor.name}">${actor.name}</p>
                        </div>
                        <div class="actor-img-container">
                        <img src="${actor.characterImage}" class="card-img-top" alt="...">
                        <p class="actor-name">Character: <a href="/universe/characters/${actor.name}">${actor.character}</p>
                    </div>
                    </div>
                </li>
            `);
			$(".actor-cards").append($castCard);
		}
	} catch (error) {
		console.error(error);
	}
}

async function displaySeasons(title) {
	console.debug("displaySeasons");
	try {
		let seasons = await getSeasons(title);
		for (let season of seasons) {
			let $seasonCard = $(`
                <li class="season-li">
                <h3 class="season-number"">Season ${season.number}</h3>
                <img src="${season.image}" class="card-img-top" alt="...">
                <p>Premiere Date: ${season.premiereDate}</p>
                <p>End Date: ${season.endDate}</p>
                <div class="episodes-container" data-id=${season.id}>
                <div class="button"><a href="">Episodes</a></div>
                </div>
                <ul class="episodes-ul">
                </ul>
                </li>

      </div>
                `);
			$(".season-cards").append($seasonCard);
		}
	} catch (error) {
		console.error(error);
	}
}

async function displayEpisodes() {
	console.debug("displayEpisodes");
	// Show an episodes list when the user clicks on the episodes button
	$(".season-cards").on("click", ".button", async function (evt) {
		evt.preventDefault();
		let seasonId = $(evt.target).closest(".episodes-container").data("id");
		console.log(seasonId);
		// if the button is clicked on pass in the season id to get the episodes
		let episodes = await getEpisodes(seasonId);
		console.log(episodes);
		$(".episodes-ul").empty();
		for (let episode of episodes) {
			let $episode = $(`
                <li class="episode-li" data-id=${episode.id}>
                    <span>Episode ${episode.number}: </span>
                    <span class="episode-name"><b>${episode.name}<b></span>
            `);
			if (seasonId === $(evt.target).closest(".episodes-container").data("id")) {
				$(".episodes-ul").append($episode);
			}
		}
	});
}

$(document).ready(() => {
	displayShow(title);
	displaySeasons(title);
	displayCast(title);
	displayEpisodes();
});
