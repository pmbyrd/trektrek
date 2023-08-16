console.log("hello from inside the movie.js file")
let movieTitle = $(".movie-title").text()

async function displayMovie(movieTitle) {
    console.debug("displayMovie");
    try {
        let movie = await getMovie(movieTitle);
        $movieCard = $(`
            <div class="card" style="width: 18rem;">
                <img src="${movie.poster}" class="card-img-top" alt="...">
                <div class="card-body">
                <h5 class="card-title">${movie.title}</h5>
                <p class="card-text">${movie.plot}</p>
                `)
        $(".movie-card").append($movieCard)
    } catch (error) {
        console.error(error);
    }
}

async function displayCast(movieTitle) {
    console.debug("displayCast");
    try {
        let cast = await getCast(movieTitle);
        console.log(cast);
        for (let actor of cast) {
            let $actorCard = $(`
                <div class="actor-card">
                    <img src="${actor.profile_path}" class="smaller-img" alt="...">
                    <div>
                        <p class="card-text"><b><a href="/media/performer/${actor.name}">${actor.name}</a></b></p>
                        <p class="card-text"><a href="/universe/character/${actor.character}">${actor.character}</a></p>
                    </div>
                </div>
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