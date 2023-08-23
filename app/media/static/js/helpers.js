
const OMDB = "https://www.omdbapi.com/?i=tt3896198&apikey=";
const TMDB = "https://api.themoviedb.org/3/movie/"
const TMDB_CREDITS = "&append_to_response=credits"
const POSTER_URL = "https://image.tmdb.org/t/p/original/"
const defaultLink = "http://tinyurl.com/missing-tv"

async function omdbAPIKey() {
	console.debug("omdbAPIKey");
	try {
		const res = await axios.get("/api/OMDB_API_KEY");
		const API_KEY = res.data;
		// return only the value of the object
		return Object.values(API_KEY);
	} catch (error) {
		console.error(error);
	}
}

async function tmdbApiKey() {
    console.log("tmdbApiKey")
    try {
        const res = await axios.get("/api/TMDB_API_KEY")
        const API_KEY = res.data
		let key = API_KEY.key
		return Object.values(API_KEY);
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

async function getMovie(movieTitle) {
	console.debug("getMovie");
	try {
		const API_KEY = await omdbAPIKey();
		const res = await axios.get(`${OMDB}${API_KEY}&t=${movieTitle}`);
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

async function getShows(showTitle) {
	console.debug("getShows");
	try {
		const API_KEY = await tmdbApiKey();
		const res = await axios.get(`https://api.themoviedb.org/3/search/tv?api_key=${API_KEY}&query=${showTitle}`);
		let show = res.data
		return show = {
			title : show.name,
				poster : `${POSTER_URL}${show.poster_path}`,
				overview : show.overview,
				first_air_date : show.first_air_date,
				genre_ids : show.genre_ids,
				id : show.id,
				original_language : show.original_language,
				original_name : show.original_name,
				origin_country : show.origin_country,
				popularity : show.popularity,
				vote_average : show.vote_average,
				vote_count : show.vote_count
		}
	} catch (error) {
		console.log(error);
	}
}

