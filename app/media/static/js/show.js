console.log('show.js loaded')

const title = $("#show-title").text()
console.log(title)


async function getShowsByTerm(searchQuery) {
	// ADD: Remove placeholder & make request to TVMaze search shows API.
	//the JSON will need to be parsed
	const response = await axios.get(`http://api.tvmaze.com/search/shows?q=${searchQuery}`)
	// I want to store the the key value pairs for each show to be handled later
	console.log(response)
	const shows = response.data.map(function(value) {
	  const show = value.show 
	  return {
		id: show.id,
		name: show.name,
		summary: show.summary,
		externals: [show.externals.imdb, show.externals.thetvdb, show.externals.tvrage],
        genres: show.genres,
		image: show.image ? show.image.medium : defaultLink  //handle for if a link is no available
	  }
	  
	})
	console.log(shows)
	console.log(shows[0].externals[0])
	return show = shows[0]
  }


async function getCastTvMaze(id) {
    const res = await getShowsByTerm(title)
    id = res.id
    const response = await axios.get(`http://api.tvmaze.com/shows/${id}/cast`)
    const cast = response.data.map(function(value) {
        return {
            name: value.person.name,
            character: value.character.name,
            image: value.person.image ? value.person.image.medium : defaultLink,
            characterImage: value.character.image ? value.character.image.medium : defaultLink
        }
    })
    return cast
}

async function getSeasons(id) {
    const res = await getShowsByTerm(title)
    id = res.id
    const response = await axios.get(`http://api.tvmaze.com/shows/${id}/seasons`)
    const seasons = response.data.map(function(value) {
        return {
            number: value.number,
            image: value.image ? value.image.medium : defaultLink,
            premiereDate: value.premiereDate,
            endDate: value.endDate
        }
    })
    console.log(seasons)
    return seasons
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
            `)
        $(".show-card-container").append($showCard)
        console.log($(".show-card-container"))
    } catch (error) {
        console.error(error);
    }
}

async function displayCast(title) {
    console.debug("displayCast");
    try {
        let cast = await getCastTvMaze(title);
        let $castCard = $(`
            <li class="actor-cast-card">
                <div class="actor-card-container">
                    <div class="actor-img-container">
                        <img src="${cast.image}" class="card-img-top" alt="...">
                        <p class="actor-name">Actor: ${cast.name}</p>
                    </div>
                    <div class="actor-img-container">
                    <img src="${cast.characterImage}" class="card-img-top" alt="...">
                    <p class="actor-name">Character: ${cast.character}</p>
                </div>
                </div>
            </li>
        `)
        $(".cast-card-container").append($castCard)
    } catch (error) {
        console.error(error);
    }
}


                    

$(document).ready(() => {
    displayShow(title)
    displayCast(title)
})