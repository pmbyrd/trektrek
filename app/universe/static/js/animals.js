console.log("Hellos from inside animals.js");
const baseURL = "http://127.0.0.1:5000/";

const $animalContainer = $(".animals");

$animalContainer.append("Hello from animals.js");

// get the souped animals from the backend
async function get_sample_animals() {
	try {
		const response = await axios.get(`${baseURL}/universe/animals/samples`);
		console.log(response)
		const animals = JSON.parse(response.data);
		console.table(animals);
		return animals;
	} catch (error) {
		console.error(error);
	}
}

get_sample_animals();

async function getAnimals() {
	try {
		const response = await axios.get(`${baseURL}/api/animals`);
		const animals = response.data.map((animal) => {
			return {
				id: animal.uid,
				name: animal.name,
				canine: animal.canine,
				feline: animal.feline,
				avian: animal.avian,
				earthAnimal: animal.earthAnimal,
				earthInsect: animal.earthInsect,
			};
		});
		return animals;
		//map over the animals and return the ids
	} catch (error) {
		console.error(error);
	}
}
getAnimals();

// sort the animals by type
async function sortAnimals() {
	const sortedAnimals = {};
	try {
		const animals = await getAnimals();
		//try returning avian as a separate array
		// const avian = [...animals.filter((animal) => animal.avian === true)]
		const avian = [...animals.filter((animal) => animal.avian === true)];
		const canine = animals.filter((animal) => animal.canine === true);
		const feline = animals.filter((animal) => animal.feline === true);
		const earthAnimal = animals.filter((animal) => animal.earthAnimal === true);
		const earthInsect = animals.filter((animal) => animal.earthInsect === true);
		// add each array to the sortedAnimals object as a key
		//create a sorted animals object
		sortedAnimals.avian = avian;
		sortedAnimals.canine = canine;
		sortedAnimals.feline = feline;
		sortedAnimals.earthAnimal = earthAnimal;
		sortedAnimals.earthInsect = earthInsect;

		return sortedAnimals;
	} catch (error) {
		console.error(error);
	}
}
// sample each and return five random animals

async function sampleAnimals(animals) {
	try {
		animals = await sortAnimals();
		for (const key in animals) {
			animals[key] = animals[key].sample(5);
		}
		return animals;
	} catch (error) {
		console.error(error);
	}
}

//post the sample to the backend so it can get the infor to do a search with beautiful soup
const sampleAnimalsResults = Promise.resolve(sampleAnimals()).then(function (
	result
) {
	return result;
});

// async function postSampleAnimals() {
// 	try {
// 		const result = await sampleAnimalsResults; // Wait for the sampleAnimalsResults promise to resolve
// 		const response = await axios.post(`${baseURL}/universe/animals/results`, {
// 			data: result,
// 			Headers: {
// 				"Content-Type": "application/json",
// 			},
// 		}
// 		);
// 		console.log(response);
// 	} catch (error) {
// 		console.error(error, error.message);
// 	}
// }

// postSampleAnimals();

Array.prototype.sample = function (n) {
	let result = new Array(n),
		len = this.length,
		taken = new Array(len);
	if (n > len)
		throw new RangeError("getRandom: more elements taken than available");
	while (n--) {
		let x = Math.floor(Math.random() * len);
		result[n] = this[x in taken ? taken[x] : x];
		taken[x] = --len in taken ? taken[len] : len;
	}
	return result;
};

async function renderAnimals() {
	try {
		console.log("renderAnimals");
		const animals = await sampleAnimals();
		console.log(animals);
		//render a template of each animal key as an h3 with that key as the class name
		//render a template of each animal as a card
		$animalContainer.empty();
		for (const key in animals) {
			let $animalType = $(`<h3 class="${key}">${key}</h3>`);
			$animalContainer.append($animalType);
			for (const animal of animals[key]) {
				let $animalCard = $(`
				<div class="card" style="width: 18rem;">
					<div class="card-body">
						<h5 class="card-title">${animal.name}</h5>
						`);
				$animalType.append($animalCard);
			}
		}
	} catch (error) {
		console.error(error);
	}
}

// renderAnimals();
