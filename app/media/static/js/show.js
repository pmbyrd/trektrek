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
			return episodes;
		}
	} catch (error) {
		console.error(error);
	}
}

async function getEpisode(episodeId) {
	try {
		if (episodeId) {
			let response = await axios.get(
				`http://api.tvmaze.com/episodes/${episodeId}/guestcast`
			);
			let guestCast = response.data.map(function (value) {
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
			return guestCast;
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
                <div class="pics-left">
                        <img src="${show.image}" class="" alt="${show.name}">
                        <p class="caption">${show.summary}</p>
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
                <li class="actor-cast-card col">
                    <div class="actor-card-container">
							<div class="actor-img-container">
							<img src="${actor.characterImage}" class="border pics" alt="...">
                            <p class="actor-name caption">Actor: <a href="/media/performer/${actor.name}">${actor.name}</p>
                        <p class="actor-name caption">Character: <a href="/universe/characters/${actor.name}">${actor.character}</p>
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
                <li class="season-li" data-id=${season.id}>
					<div>
                		<h3 class="season-number"">Season ${season.number}</h3>
                		<img src="${season.image}" class="card-img-top" alt="...">
                		<p>Premiere Date: ${season.premiereDate}</p>
                		<p>End Date: ${season.endDate}</p>
						<div class="button"><a href="">Episodes</a></div>
                		<div class="episodes-container" season-data-id=${season.id}>
                		</div>
               		</div>
                </li>
                `);
			$(".season-cards").append($seasonCard);
		}
	} catch (error) {
		console.error(error);
	}
}

async function displayEpisodes() {
    console.debug("displayEpisodes");
    $(".season-cards").on("click", ".button", async function (evt) {
		evt.preventDefault();
		let seasonId = $(this).closest(".season-li").data("id"); // Use closest to find the closest ancestor with the specified class
		$(".season-cards").removeClass("flexbox");
		// test appending to the div that was clicked
		let episodes = await getEpisodes(seasonId);
		for (let episode of episodes) {
			let $episodeCard = $(`
			<div class="episode pics-left flexbox" data-id="${episode.id}">
				<img src="${episode.image}" class="border col" alt="Screenshot from ${episode.name}">
				<div class="episode-info col">
					<p class="caption">Episode ${episode.number}</p>
					<p class="caption">${episode.name}</p>
					<p class="caption">Airdate: ${episode.airdate}</p>
					<p class="caption">${episode.summary}</p>
					<div class="guest-cast-button button"><a href="">Guest Cast</a></div>
					<div class="guest-cast-container" episode-data-id=${episode.id}>
				</div>
			</div>
			
			`)
			$(this).closest(".season-li").addClass("flexbox");
			$(this).closest(".season-li").append($episodeCard);
		}
	});
}

async function displayGuestCast() {
	console.debug("displayGuestCast");
    $(".season-cards").on("click", ".guest-cast-button", async function (evt) {
		console.log("guest cast button clicked");
		evt.preventDefault();
		console.log($(this).closest(".episode").data("id"));
		let episodeId = $(this).closest(".episode").data("id");
		let guestCast = await getEpisode(episodeId);
		// console.log(guestCast); NOTE this is an array of objects
		for (let actor of guestCast) {
			let $guestCastCard = $(`
			<div class="guest-cast-card">
				<img src="${actor.characterImage}" class="border pics" alt="...">
				<p class="caption">Actor: <a href="/media/performer/${actor.name}">${actor.name}</p>
				<p class="caption">Character: <a href="/universe/characters/${actor.name}">${actor.character}</p>
			</div>
			`);
			$(this).closest(".episode").addClass("flexbox");
			$(this).closest(".episode").append($guestCastCard);
		}
	});
}



$(document).ready(() => {
	displayShow(title);
	displaySeasons(title);
	displayCast(title);
	displayEpisodes();
	displayGuestCast();
});
