console.log("hello from inside the models.js file");
const OMDBAPI = "http://www.omdbapi.com/?i=tt3896198&apikey=";
// const TMDB = "https://api.themoviedb.org/3/movie/550?api_key="
// https://api.themoviedb.org/3/movie/150540?api_key=###&append_to_response=credits
const TMDB = "https://api.themoviedb.org/3/movie/"
const TMDB_CREDITS = "&append_to_response=credits"
const POSTER_URL = "https://image.tmdb.org/t/p/original/"
async function getAPIKey() {
	console.debug("getAPIKey");
	try {
		const res = await axios.get("/api/OMDB_API_KEY");
		const API_KEY = res.data;
		return API_KEY;
	} catch (error) {
		console.error(error);
	}
}

async function tmdbApiKey() {
    console.log("tmdbApiKey")
    try {
        const res = await axios.get("/api/TMDB_API_KEY")
        const API_KEY = res.data
        return API_KEY
    } catch (error) {
        console.error(error)
    };
}

async function getCast(movieTitle) {
    console.debug("getCast")
    try {
        const API_KEY = await tmdbApiKey()
        const movie = await getMovie(movieTitle)
        const movieId = movie.imdbID
        const res = await axios.get(`${TMDB}/${movieId}?api_key=${API_KEY}&append_to_response=credits`)
        let cast = res.data.credits.cast
        let mappedCast = cast.map(cast => {
            return {
                name : cast.name,
                character : cast.character,
                id : cast.id,
                profile_path : `${POSTER_URL}${cast.profile_path}`,
                original_name : cast.original_name
            }})
        return mappedCast
    } catch (error) {
        console.error(error)
    }
}
getCast("Star Trek Beyond")

async function getActor(actorId) {
    console.debug("getActor")
    // use this function to look up an actor by their id to see other and shows that they have been in
}

async function getMovie(movieTitle) {
	console.debug("getMovie");
	try {
		const API_KEY = await getAPIKey();
		const res = await axios.get(`${OMDBAPI}${API_KEY}&t=${movieTitle}`);
		let movie = res.data;
		return (movie = {
			title: movie.Title,
			year: movie.Year,
			rated: movie.Rated,
			released: movie.Released,
			runtime: movie.Runtime,
			genre: movie.Genre,
			director: movie.Director,
			metascore: movie.Metascore,
			imdbRating: movie.imdbRating,
			plot: movie.Plot,
			poster: movie.Poster,
			genre: movie.Genre,
			actors: movie.Actors,
			imdbID: movie.imdbID,
		});
	} catch (error) {
		console.log(error);
	}
}

async function getActors(title) {
	console.debug("getActors");
	try {
        
	} catch (error) {
        console.error(error);
    }
}
