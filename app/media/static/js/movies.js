console.log('movies.js loaded');

async function getMovies() {
    try {
        //this call is to my own backend
        const res = await axios.get('/api/movies')
        const movies = res.data
        const titles = movies.map(movie => movie.title)
        return titles
    } catch (error) {
        console.log(error)
    }
}

async function displayMovies() {
    console.debug('displayMovies');
    try {
        let movies = await getMovies();
        //map over each movie and create a card for each movie
        for (let movieTitle of movies) {
            let movieData = await getMovie(movieTitle)
            $movieCard = $(`
            <div class="movie-card">
            <h3> <a href="/media/movie/${movieData.title}" class="btn btn-primary">${movieData.title}</a></h3>
                <img src="${movieData.poster}" class="card-img-top" alt="...">
                <div class="card-body">
                    <p class="plot-text">${movieData.plot}</p>
                    <p class="card-text">Genres: ${movieData.genre}</p>
                    <p class="card-text">Director: ${movieData.director}</p>
                    <p class="card-text">Release date: ${movieData.released}</p>
                    <p class="card-text">Runtime: ${movieData.runtime}</p>
                    <p class="card-text">Metascore: ${movieData.metascore}/100</p>
                </div>
            </div>
            `)
            $(".movies-list").append($movieCard)
        }       
    } catch (error) {
        console.log(error)
    }
}


$(document).ready(async () => {
    await displayMovies()
})



