console.log('movies.js loaded');

const $moviesContainer = $(".movies")
let $movieCard = $(".movie-card")
const $moviesList = $(".movies-list")



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
        // $moviesContainer.empty();
        for (let movieTitle of movies) {
            let movieData = await getMovie(movieTitle)
            
            $movieCard = $(`
            <div class="card mb-4" style="width: 18rem;">
                <img src="${movieData.poster}" class="card-img-top" alt="...">
                <div class="card-body">
                    <p class="card-text">${movieData.plot}</p>
                    <p class="card-text">Genres: ${movieData.genre}</p>
                    <p class="card-text">Directo: ${movieData.director}</p>
                    <p class="card-text">Release date: ${movieData.released}</p>
                    <p class="card-text">Runtime: ${movieData.runtime}</p>
                    <p class="card-text">Metascore: ${movieData.metascore}/100</p>
                   
                    <a href="/media/movie/${movieData.title}" class="btn btn-primary">${movieData.title}</a>
                </div>
            </div>
            `)
            $(".movies-list").append($movieCard)
        }       
    } catch (error) {
        console.log(error)
    }
    
}



$(document).ready(displayMovies())
// displayMovies()



