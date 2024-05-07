function verificar() {
    var nac = document.querySelector('#txtnac')
    var res = document.querySelector('#res')

    res.innerHTML(`Seu país é ${nac}`)

    if (nac == 'Brasil') {
        res.innerHTML += 'Você é brasileiro!'
    } else {
        res.innerHTML += 'Você é estrangeiro!'
    }
}

/* var país = 'Brasil'
console.log(`Vivendo em ${país},`)
if (país == 'Brasil') {
    console.log('Você é brasileiro.')
} else {
    console.log('Você é estrangeiro.')
} */