//local dev-Section
        let fetchRezepteLocal = () => fetch('rezepte.json')
            .then(response => response.json())
            .then(json => json.recipes.map(num => [num.recipe_id, num.title]))

        let displayLocal = idTitlePairs => {
            idTitlePairs.forEach((pair,i) => {
                let view = document.querySelector(".view")
                let recipe = document.createElement("div")
                view.appendChild(recipe)
                let para1 = document.createElement("p")
                recipe.appendChild(para1)
                let id = document.createTextNode(pair[0])
                para1.appendChild(id)
                let para2 = document.createElement("p")
                view.appendChild(para2)
                let name = document.createTextNode(pair[1])
                recipe.appendChild(para2)
                para2.appendChild(name)
            })
        }  

fetchRezepteLocal()
.then(res => console.log(res))
    