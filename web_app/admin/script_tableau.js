const send = () =>{
    event.preventDefault()
    console.log(event)

    const user = {}
    const formulaire = event.target

    for(input of fomrulaire) {
        if input.id !=="" {
            //stocke l'id de user et affiche la valeur de l'id
        user[input.id]=input.value

        }

    }

    console.log(value)
//permet de récupérer la réponse et le JSON qui est dedans après requête dans postman
    fetch(http)('http://127.0.0.1:5000/utilisateur').then(resp => resp.json()).then(json=>renderusers(json)) 
}

document.querySelector("#nouvel_utilisateur").addEventListener('submit', send)