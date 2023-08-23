console.log('series.js loaded');

async function getSeries() {
    try {
        const res = await axios.get("/api/series")
        let series = res.data
        const titles = series.map(series => series.title)
        console.log(titles)
        return titles
    } catch (error) {
        console.log(error)
    }
}

let titles = getSeries()

async function displaySeries() {
    console.log('displaySeries');
    try {
        let shows = await getSeries();
        for (let showTitle of shows) {
            let showData = await getMovie(showTitle)
            $showCard = $(`
            <div class="show-card">
            <h3> <a href="/media/show/${showData.title}" class="btn btn-primary">${showData.title}</a></h3>
            <img src="${showData.poster}" class="card-img-top" alt="...">
            <p>${showData.plot}</p>
            </div>
            `)
            console.log($showCard)
            $(".series-list").append($showCard)
        }
        if (shows.length === 0) {
            $(".series-list").append(`<p>Sorry, no shows found</p>`)
        }
        $(".series-list").length === shows.length
        $(".series").show()
        } catch (error) {
            console.log(error)
        }
    }


$(document).ready(displaySeries())
