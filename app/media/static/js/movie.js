console.log("hello from inside the movie.js file")
let movieTitle = $(".movie-title").text()

async function displayMovie(movieTitle) {
    console.debug("displayMovie");
    try {
        let movie = await getMovie(movieTitle);
        $movieCard = $(`
            <div class="card">
                <div class="img-conatiner">
                    <img src="${movie.poster}" class="card-img-top" alt="...">
                </div>
                <div class="card-body-container">
                    <p class="card-text">${movie.plot}</p>
                </div>
                `)
        $(".movie-card-container").append($movieCard)
    } catch (error) {
        console.error(error);
    }
}

async function displayCast(movieTitle) {
    console.debug("displayCast");
    try {
        let cast = await getCast(movieTitle);
        for (let actor of cast) {
            let $actorCard = $(`
                <li class="actor-card col">
                    <img src="${actor.profile_path}" class="smaller-img" alt="...">
                    <div>
                        <p class="card-text"><b><a href="/media/performer/${actor.name}">Actor: ${actor.name}</a></b></p>
                        <p class="card-text"><a href="/universe/characters/${actor.character}">Character: ${actor.character}</a></p>
                    </div>
                </li>
            `);
            $(".actor-cards").append($actorCard);
        }  
    } catch (error) {
        console.error(error);
    }
}

async function showTags(movieTitle){
    try {
        let tags = await getTags(movieTitle)
        // turn the results of the movie's plot into an array of words
        let movie = await getMovie(movieTitle);
        let plot = movie.plot;
        let plotWords = plot.split(' ');
        // Convert each word to lowercase
        plotWords = plotWords.map(word => word.toLowerCase());
        // Loop over the tags and see if any of them are in the plot
        for (let tag of tags) {
            tag.name = tag.name.toLowerCase();
            if (plotWords.includes(tag.name)) {
                console.log(tag.name);
                let $tag = $(`
                    <li class="tag button col">
                        <a href="/users/tags/${tag.id}">${tag.name}</a>
                    </li>
                `)
                $(".tags").append($tag);
            }
        }
    } catch (error) {
        console.error(error)
    }
}

async function getTags() {
    try {
        let res = await axios.get('/api/tags');
        let tags = res.data.map(tag => ({
            id: tag.id,
            name: tag.name
        }));
        console.log(tags);
        return tags;
    } catch (error) {
        console.error(error);
    }
}


$(document).ready(function () {
    displayMovie(movieTitle);
    displayCast(movieTitle);
    showTags(movieTitle)
});