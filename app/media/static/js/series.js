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
            console.log(showTitle)
            let showData = await getMovie(showTitle)
            console.log(showData)
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
        } catch (error) {
            console.log(error)
        }
    }

    //     for (let showTitle of shows) {
    //         let showData = await getShows(showTitle)
    //         $showCard = $(`
    //         <div class="show-card">
    //         <h3> <a href="/media/series/${showData.title}" class="btn btn-primary">${showData.title}</a></h3>
    //             <img src="${showData.poster}" class="card-img-top" alt="...">
    //             <div class="card-body">
    //                 <p class="plot-text">${showData.plot}</p>
    //               </div>
    //         </div>
    //         `)
    //         console.log($showCard)
    //         $(".series-list").append($showCard)
    //     }
    // } catch (error) {
    //     console.log(error)
    // }


$(document).ready(displaySeries())
