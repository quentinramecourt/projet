const register = event => {
    event.preventDefault()
    console.log(event)
      for(let elem of event.target)
         console.log(elem.value)

}






document.querySelector("#enregistrement").addEventListener('submit',send)

