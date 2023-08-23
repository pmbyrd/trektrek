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
        $(".actor-cards").empty();
        console.log(cast);
        for (let actor of cast) {
            let $actorCard = $(`
                <li class="actor-card">
                    <img src="${actor.profile_path}" class="smaller-img" alt="...">
                    <div>
                        <p class="card-text"><b><a href="/media/performer/${actor.name}">${actor.name}</a></b></p>
                        <p class="card-text"><a href="/universe/characters/${actor.character}">${actor.character}</a></p>
                    </div>
                </li>
            `);
            $(".actor-cards").append($actorCard);

        }        
    } catch (error) {
        console.error(error);
    }
}

$(document).ready(function () {
    displayMovie(movieTitle);
    displayCast(movieTitle);
});